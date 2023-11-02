#!/usr/bin/python3
import subprocess,sys,os,glob,re,json

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



def help():
    print(f"USAGE: {os.path.relpath(__file__)} <file> [<option>]")
    print("Where <file> is:")
    print(" * all : execute all")
    print(" * stats : generate stats")
    print(" * <file> : execute all compilers for this kind of file")
    print(" * <folder> : execute all compilers for files in this folder")
    print("Where <option> can be, to force a specific one:")
    for k,v in LANGS.items():
        print(f" * {k:5s} : {v['v']}")
        print(f"           {v['c'].replace('$0',v['e']).replace('$1','<file>')}")


def batch(files):
    found=False
    for file in files:
        ext=file.split(".")[-1]
        for k,v in LANGS.items():
            if v.get("ext") == ext:
                found=True
                main( file,k )        
    if not found:
        print(f"ERROR: didn't found a compiler for {file}")
        return -1
    else:
        return 0

def main(file,lang) -> int:
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
    else:
        help()
        return -1

def getseconds(file):
    contents = open(file).read().splitlines()
    last=contents[-1]
    assert last.lower().startswith("took")
    return float(re.findall( r"[\d\.]+",last)[0])

def getinfo(file):
    contents = open(file).read().splitlines()
    for i in contents:
        if i.startswith("//INFO:"):
            return i[7:].strip()
        if i.startswith("#INFO:"):
            return i[6:].strip()
    return "?"

def analyse() -> dict:
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

def printmd(d):
    legends=[]
    for k,v in d.items():
        tests=[]
        for i in LANGS.keys():
            if i in v:
                tests.append( (i, v[i]["moy"]) )
                legends.append( (i,v[i]["version"] ))
        tests.sort(key=lambda x: x[1])
        print(f"{k} ({v['info']})")
        for k,v in tests:
            print(f" - {k:5s} : {v} seconds")
    print()
    print("with versions:")
    for k,v in sorted(list(set(legends))):
        print(f" * {k:5s} : {v}")


def update():
    for k,v in list(LANGS.items()):
        cp=subprocess.run(f"which {v['e']}",shell=True,text=True,capture_output=True)
        if cp.returncode==0:
            LANGS[k]['e']=cp.stdout.strip()
            cp=subprocess.run([LANGS[k]['e'],"--version"],text=True,capture_output=True)
            LANGS[k]['v']=cp.stdout.splitlines()[0]
        else:
            print(f"*WARNING* no {k} lang (you can install '{v['e']}')!")
            del LANGS[k]

if __name__=="__main__":
    update()

    if len(sys.argv)==3:
        ret=main( sys.argv[1],sys.argv[2] )
    elif len(sys.argv)==2:
        if sys.argv[1]=="all":
            files=glob.glob( os.path.join(".",TESTFILES) ) + glob.glob( os.path.join("optimized",TESTFILES) ) + glob.glob( os.path.join("experiments",TESTFILES) )
            ret=batch( files )
        elif sys.argv[1]=="stats":
            jzon=analyse()
            print(json.dumps(jzon,indent=2))
            ret=0
        elif sys.argv[1]=="hstats":
            jzon=analyse()
            printmd(jzon)
            ret=0
        elif os.path.isdir(sys.argv[1]):
            files=glob.glob( os.path.join(sys.argv[1],TESTFILES) )
            ret=batch( files )
        elif os.path.isfile(sys.argv[1]):
            files=[sys.argv[1]]
            ret=batch( files )
        else:
            print("WTF is",sys.argv[1])
            ret=-1
    else:
        ret=main("?","?")
    sys.exit(ret)
