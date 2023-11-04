#!/usr/bin/python3
import subprocess,sys,os,glob,re,json
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
    py311=dict(	
        e="python3.11",
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
)
#########################################################################
## helpers
#########################################################################

def update():
    """ update the global dict LANGS, to current supported lang of the host"""
    for k,v in list(LANGS.items()):
        cp=subprocess.run(f"which {v['e']}",shell=True,text=True,capture_output=True)
        if cp.returncode==0:
            LANGS[k]['e']=cp.stdout.strip()
            cp=subprocess.run([LANGS[k]['e'],"--version"],text=True,capture_output=True)
            LANGS[k]['v']=cp.stdout.splitlines()[0]
        else:
            print(f"*WARNING* no {k} lang (you can install '{v['e']}')!")
            del LANGS[k]

def help():
    print(f"USAGE: {os.path.relpath(__file__)} <file> ... [<option> ...]")
    print("Where <file> is:")
    print(" * stats : generate stats")
    print(" * hstats : generate human stats")
    print(" * <file> : execute all compilers for this kind of file")
    print(" * <folder> : execute all compilers for files in this folder")
    print("Where <option> can be, to force a specific one:")
    for k,v in LANGS.items():
        print(f" --{k:5s} : {v['v']}")
        print(f"            {v['c'].replace('$0',v['e']).replace('$1','<file>')}")

#########################################################################
## run/batch methods
#########################################################################

def batch(files:list, opts:"list|None") -> int:
    """execute files, and if opts, restrict to lang from 'opts'"""
    found=False
    for file in files:
        ext=file.split(".")[-1]
        for k,v in LANGS.items():
            if v.get("ext") == ext:
                if opts and k not in opts:
                    continue
                found=True
                run( file,k )        
    if not found:
        print(f"ERROR: didn't found a compiler for {file}")
        return -1
    else:
        return 0

def run(file:str,lang:str) -> int:
    """ run file 'file' with the defined lang 'lang'"""
    file=os.path.relpath(file)
    d = LANGS.get(lang)
    if d:
        cmd=d["c"]
        cmd=cmd.replace("$0",d["e"])
        cmd=cmd.replace("$1",file)
        print(f"[{lang}]> {cmd}")
        cp=subprocess.run(cmd,shell=True,text=True,capture_output=True)
        if cp.returncode==0:
            if "/" in file:
                folder,file = os.path.dirname(file),os.path.basename(file)
                folder=os.path.join("outputs",folder)
            else:            
                folder="outputs"
                
            if not os.path.isdir(folder):
                os.makedirs(folder)

            foutput = f"{file}|{lang}|0|out"
            dest=os.path.join(folder,foutput)
            while os.path.isfile(dest):
                foutputs=foutput.split("|")
                foutput="|".join( [foutputs[0], foutputs[1], str( int(foutputs[2]) + 1), foutputs[3]])
                dest=os.path.join(folder,foutput)
            with open(dest,"w+") as fid:
                fid.write(cp.stdout)
            lines=cp.stdout.splitlines()
            print( lines[0])
            print( f"... {len(lines)} lines ...")
            for line in lines[-3:]:
                print( line )
            print()
            return 0
        else:
            print("ERROR")
            print(cp.stdout)
            print(cp.stderr)
            return cp.returncode
        return 0
    else:
        help()
        return -1

#########################################################################
## stats methods
#########################################################################
def getseconds(file:str) -> float:
    """get seconds in last line of the resulted file 'file')"""
    last_line = open(file).read().splitlines()[-1]
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

def analyze() -> dict:
    """analyze outputs results from outfput folder, and return json details"""
    d={}
    for i in glob.glob("outputs/*out")+glob.glob("outputs/*/*out"):
        file,mode,nb,_ = i[8:].split("|")
        fileinfo=d.setdefault(file,{})
        fileinfo["info"]=getinfo(file)
        info=fileinfo.setdefault(mode,{})
        info.setdefault("tests",[]).append(getseconds(i))
        info["moy"] = round( sum( info["tests"] ) / len(info["tests"]), 2)
        info["version"] = LANGS[mode]["v"]
    d={k:d[k] for k in sorted(d.keys())}
    return d

def print_human_stats(jzon:dict):
    """ print human readable stats"""
    legends=[]
    for k,v in jzon.items():
        tests=[]
        nb=-1
        for i in LANGS.keys():
            if i in v:
                nb=len(v[i]["tests"])
                tests.append( (i, v[i]["moy"]) )
                legends.append( (i,v[i]["version"] ))
        tests.sort(key=lambda x: x[1])
        print(f"{k} ({v['info']})")
        for k,v in tests:
            print(f" - {k:5s} : {v} seconds ({nb}tests)")
    print()
    print("with versions:")
    for k,v in sorted(list(set(legends))):
        print(f" * {k:5s} : {v}")



if __name__=="__main__":
    update()

    files=[]
    opts=[]
    for i in sys.argv[1:]:
        if i.startswith("--"):
            opts.append(i[2:].lower())
        else:
            if os.path.isdir(i):
                files.extend( glob.glob( os.path.join(i,TESTFILES) ) )
            else:
                files.append(i)

    for i in opts:
        if i not in LANGS.keys():
            print(f"ERROR : --{i} is not in {list(LANGS.keys())}")
            sys.exit(-1)

    if len(files)>=1:
        if len(files)==1:
            if files[0]=="stats":
                jzon=analyze()
                print(json.dumps(jzon,indent=2))
                ret=0
            elif files[0]=="hstats":
                jzon=analyze()
                print_human_stats(jzon)
                ret=0
            else:
                ret=batch( files, opts )
        else:
            ret=batch(files, opts )
    else:
        ret=run("?","?")   # just for help prints 
    sys.exit(ret)
