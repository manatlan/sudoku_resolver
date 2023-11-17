#!/usr/bin/python3
import subprocess,sys,os,glob,re,json,statistics,re,fnmatch,time,shutil,platform,multiprocessing
"""
See doc :
https://github.com/manatlan/sudoku_resolver/blob/master/make.md
"""

TESTFILES="sudoku*.*"   # pattern for tested files

LANGS=dict(
    mojo=dict(	
        e="mojo",
    	c="$0 run $1",
        ext="mojo",
    ),
    nim=dict(	
        e="nim",
    	c="$0 r -d:danger $1",
        ext="nim",
    ),
    java=dict(
        e="java",
    	c="$0 $1",
        ext="java",
    ),
    node=dict(	
        e="node",
    	c="$0 $1",
        ext="js",
    ),
    py3=dict(	
        e="python3",
    	c="$0 -uOO $1",
        ext="py",
    ),
    rust=dict(	
        e="rustc",
    	c="$0 -C opt-level=3 -C target-cpu=native $1 -o exe && ./exe",
        ext="rs",
    ),
    gcc=dict(	
        e="gcc",
    	c="$0 $1 -o exe && ./exe",
        ext="c",
    ),


    #specifics ......................................................
    codon=dict(	
        e="~/.codon/bin/codon",
    	c="$0 run -release $1",
        ext="py",
    ),
    pypy=dict(	
        e="~/Téléchargements/pypy3.10-v7.3.13-linux64/bin/pypy3",
    	c="$0 -uOO $1",
        ext="py",
    ),
    py37=dict(	
        e="python3.7",
    	c="$0 -uOO $1",
        ext="py",
    ),

)
#########################################################################
## helpers
#########################################################################
rr=lambda x: round(x,2)

def myprint(*a,**k):
    k["flush"]=True
    print(*a,**k)

todict = lambda x: dict( [[i.strip() for i in line.split(":",1) if ":" in line] for line in x.splitlines() if line.strip()] )

def get_info_host() -> str:
    s=f"PLATFORM : {platform.processor()}/{platform.platform()} with {multiprocessing.cpu_count()} cpus"
    try:
        cp=subprocess.run(["cat","/proc/cpuinfo"],text=True,capture_output=True)
        if cp.returncode==0:
            d=todict(cp.stdout)
            s+=f"""\nCPUINFO  : {d['vendor_id']} "{d['model name']}" ({d['bogomips']} bogomips)"""
        cp=subprocess.run(["cat","/proc/meminfo"],text=True,capture_output=True)
        if cp.returncode==0:
            d=todict(cp.stdout)
            s+=f"""\nMEMINFO  : {d['MemTotal']}"""
    except:
        s+="(can't get more info from host)"
    return s

def update():
    """ update the global dict LANGS, to current supported lang of the host"""
    for k,v in list(LANGS.items()):
        if os.path.isfile(os.path.expanduser(v['e'])):
            cmd=os.path.expanduser(v['e'])
        else:
            cmd=shutil.which(v['e'])
        if cmd:
            LANGS[k]['e']=cmd.strip()
            cp=subprocess.run([LANGS[k]['e'],"--version"],text=True,capture_output=True)
            LANGS[k]['v']=cp.stdout.splitlines()[0]
        else:
            print(f"*WARNING* no {k} lang (you can install '{v['e']}')!")
            del LANGS[k]

def help():
    print(f"USAGE TEST: {os.path.relpath(__file__)} <file|folder> ... <option>")
    print(f"USAGE STAT: {os.path.relpath(__file__)} stats <file|folder> ... <option>")
    print("Tool to test and sort results from differents interpreters/languages")
    print("On the host:")
    print(get_info_host())
    print()
    print("Where <option> can be, to force a specific one:")
    for k,v in LANGS.items():
        print(f" --{k:5s} : {v['v']}")
        print(f"           {v['c'].replace('$0',v['e']).replace('$1','<file>')}")

#########################################################################
## run/batch methods
#########################################################################

def batch(files:list, opts:"list|None") -> int:
    """execute files, and if opts, restrict to lang from 'opts'"""
    found=False
    for file in files:
        if fnmatch.fnmatch(os.path.basename(file),TESTFILES):
            ext=file.split(".")[-1]
            for k,v in LANGS.items():
                if v.get("ext") == ext:
                    if opts and k not in opts:
                        continue
                    found=True
                    run( file,k )        
    if not found:
        myprint(f"ERROR: didn't found a compiler for {file}")
        return -1
    else:
        return 0

def create_result(file,lang, output,cmd,version):
    folder,file = os.path.dirname(file) or ".",os.path.basename(file)
    dest = f"{folder}/.outputs/{file}|{lang}|0"

    if not os.path.isdir(os.path.dirname(dest)):
        os.makedirs(os.path.dirname(dest))

    while os.path.isfile(dest):
        parts=dest.split("|")
        dest="|".join( [parts[0], parts[1], str( int(parts[2]) + 1)])

    with open(dest,"w+") as fid:
        fid.write( json.dumps( dict(cmd=cmd,version=version,output=output), indent=4 ))

def run(file:str,lang:str) -> int:
    """ run file 'file' with the defined lang 'lang'"""
    file=os.path.relpath(file)
    d = LANGS.get(lang)
    if d:
        cmd=d["c"]
        cmd=cmd.replace("$0",d["e"])
        cmd=cmd.replace("$1",file)
        myprint(f"[{lang}]> {cmd}")
        cp=subprocess.run(cmd,shell=True,text=True,capture_output=True)
        if cp.returncode==0:
            create_result(file,lang, cp.stdout, cmd, d["v"])
            
            lines=cp.stdout.splitlines()
            myprint( lines[0])
            myprint( f"... {len(lines)} lines ...")
            for line in lines[-3:]:
                print( line )
            myprint()
            return 0
        else:
            myprint("ERROR")
            myprint(cp.stdout)
            myprint(cp.stderr)
            return cp.returncode
        return 0
    else:
        help()
        return -1

#########################################################################
## stats methods
#########################################################################
def getseconds(output:str) -> float:
    """get seconds in last line of the 'output')"""
    last_line = output.splitlines()[-1]
    assert last_line.lower().startswith("took")
    return float(re.findall( r"[\d\.]+",last_line)[0])

def getinfo(file:str) -> str:
    """get info from the source file 'file'"""
    contents = open(file).read().splitlines()
    for i in contents:
        if i.startswith("//INFO:"):
            return i[7:].strip()
        if i.startswith("#INFO:"):
            return i[6:].strip()
    return "?"

def stats(files:list, opts:list):
    for file in files:
        folder,filename = os.path.dirname(file) or ".",os.path.basename(file)
        results = sorted(glob.glob(f"{folder}/.outputs/{filename}|*"))
        if results:
            
            bymode={}
            for result in results:
                _,mode,nb = result.split("|")

                data=json.load( open(result,"r+") )
                seconds=getseconds(data["output"])
                bymode.setdefault(mode,[]).append(seconds)

            if opts and (mode not in opts): continue
            myprint("\n",file,":",getinfo(file))

            for mode, tests in bymode.items():
                if opts and (mode not in opts): continue
                moy= rr( statistics.median(tests) )
                myprint(f"  - {mode:5s} : {moy} seconds ({len(tests)}x, {rr(min(tests)):.02f}><{rr(max(tests)):.02f})")


if __name__=="__main__":
    update()
    args=sys.argv[1:]

    if args:
        if args[0]=="stats":
            mode="stats"
            args.pop(0)
            if not [i for i in args if not i.startswith("--")]:
                # not files given in input, assuming '.'
                args.insert(0,".")

        elif re.match("(\d+)x",args[0]):
            nb=int(re.match("(\d+)x",args[0])[1])
            mode="test"
            args.pop(0)
        else:
            nb=1
            mode="test"

        files=[]
        opts=[]
        for i in args:
            if i.startswith("--"):
                opt=i[2:].lower()
                if opt not in LANGS.keys():
                    myprint(f"ERROR : --{opt} is not in {list(LANGS.keys())}")
                    sys.exit(-1)
                else:
                    opts.append(opt)
            else:
                if os.path.isdir(i):
                    files.extend( glob.glob( os.path.join(i,TESTFILES) ) )
                elif os.path.isfile(i):
                    files.append(i)
                else:
                    myprint(f"ERROR : {i} not found")
                    sys.exit(-1)

        if mode=="test":
            t=time.monotonic()
            for i in range(nb):
                ret=batch(files, opts )
            myprint(f"(total time: %ss)" % rr(time.monotonic()-t))
        else:
            ret=stats(files, opts)
    else:
        ret=run("?","?")   # just for help prints 
    sys.exit(ret)
