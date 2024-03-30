#!/usr/bin/python3
import subprocess,sys,os,glob,re,json,statistics,re,fnmatch,time,shutil,platform,multiprocessing,datetime
import json,platform,statistics,os,datetime
import hashlib
import logging

"""
See doc :
https://github.com/manatlan/sudoku_resolver/blob/master/make.md
"""

LANGS=dict(
    go=dict(	
        e="go",
    	c=("$0 build -o ./sudoku $1 ","./sudoku"),
        ext="go",
    ),
    mojo=dict(	
        e="mojo",
    	c=("$0 build $1 -o ./sudoku","./sudoku"),
        ext="mojo",
    ),
    nim=dict(	
        e="nim",
    	c=("$0 compile -d:danger $1", "./sudoku"),
        ext="nim",
    ),
    java=dict(
        e="java",
    	c=("$0c $1","$0 Sudoku"),
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
    	c=("$0 -C opt-level=3 -C target-cpu=native $1 -o ./sudoku","./sudoku"),
        ext="rs",
    ),
    # gcc=dict(	
    #     e="gcc",
    # 	c="$0 $1 -o sudoku && ./sudoku",
    #     ext="c",
    # ),
    pypy=dict(	
        e="pypy3",
    	c="$0 -uOO $1",
        ext="py",
    ),

    #specifics ......................................................
    codon=dict(	
        e="~/.codon/bin/codon",
    	c=("$0 build -release $1 -o ./sudoku","./sudoku"),
        ext="py",
    ),
    py37=dict(
        e="python3.7",
    	c="$0 -uOO $1",
        ext="py",
    ),

)

#########################################################################
## Specific for tests here (about sudoku)
#########################################################################
NB_GRIDS=1956

TESTFILES="sudoku*.*"   # pattern for tested files

def do_the_test(lang,d,file,nb_grids=None) -> "float|None":
    grids=[i.strip() for i in open("grids.txt")][:nb_grids or NB_GRIDS]

    myprint()
    cmd_build,cmd_run = get_commandlines(d,file)
    if cmd_build:
        myprint(f"[{lang}]> {cmd_build} && {cmd_run} < grids.txt #({len(grids)})")
    else:
        myprint(f"[{lang}]> {cmd_run} < grids.txt #({len(grids)})")

    try:
        t,output=runcmd( "\n".join(grids), cmd_run, cmd_build )

        # clean fs by removing build outputs
        for i in ["sudoku","Sudoku.class"]:
            if os.path.isfile(i):
                os.unlink(i)

        results=[all( [i.count(x)==9 for x in "123456789"] ) for i in re.findall(r"[1-9]{81}",output)]

        if len(results)==len(grids) and all(results):
            print(f"--> OK : {t:.03f}s for {len(grids)} grids")
            return t
        else:
            print( output )
            print("!!! BAD RESULT !!!")
    except Exception as e:
        print("ERROR",e)
    return None

#########################################################################
## DB
#########################################################################
class Tests:
    def __init__(self,filename:str,data:dict):
        self.filename=filename
        self._modes=data["modes"]

    def __iter__(self):
        for mode,info in self._modes.items():
            tests=info["tests"]
            _sign=info.get("sign",None)
            if _sign and _sign != sign(self.filename,mode,str(NB_GRIDS)): continue
            yield mode,statistics.median(tests),len(tests),min(tests),max(tests)

    def filter(self,modes:list) -> list:
        ll=[]
        for mode,v,nb,vmin,vmax in self:
            if modes and mode not in modes: continue
            ll.append( (mode,v,nb,vmin,vmax) )
        return ll


class DB:
    def __init__(self,db:"dict|None"=None):
        self._db={} if db is None else db
        
    def add(self,filename:str,mode:str,sec:float, signature:str):
        info=self._db.setdefault(filename,{}).setdefault("modes",{}).setdefault(mode,{})

        if info.get("sign") == signature:
            info.setdefault("tests",[]).append( sec )
        else:
            info["tests"]=[ sec ]
        info["sign"]=signature

    def __str__(self):
        return json.dumps(self._db)

    def __iter__(self):
        for filename,data in sorted(self._db.items()):
            yield Tests(filename,data)

    def __add__(self,db):
        for filename,data in sorted(db._db.items()):
            for mode,info in sorted(data["modes"].items()):
                for test in info["tests"]:
                    self.add( filename, mode, test, info.get("sign"))
        return self


class HostTest(DB):
    def __init__(self):
        self.dbfile=f"db_{platform.node()}.json"
        if os.path.isfile( self.dbfile ):
            DB.__init__(self,json.load( open(self.dbfile,"r+") ))
        else:
            DB.__init__(self,{})

    def add(self,filename:str,mode:str,sec:float, once:str):
        DB.add(self,filename,mode,sec, sign(filename,mode,once) )
        with open(self.dbfile,"w+") as fid:
            fid.write(json.dumps(self._db,indent=2))

    def snapshot(self) -> str:
        """ generate a line string, containing (timestamp,db) as json str """
        """ (used to accumulate data in a file)"""
        timestamp=datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d%H%M%S')
        return json.dumps( (timestamp,self._db) )


class Snapshots(DB):    # results.txt
    def __init__(self,lines:str):
        DB.__init__(self)
        for line in lines.splitlines():
            timestamp,db=json.loads(line)
            self += DB(db)
        

def test_DB():
    db1=DB()
    db1.add("kiki.py","py3",12.0,"")
    db1.add("kiki.py","py3",20.0,"")
    db1.add("kiki2.py","node",20.0,"")
    assert db1._db['kiki.py']["modes"]["py3"]["tests"] == [12.0, 20.0]
    assert db1._db['kiki2.py']["modes"]["node"]["tests"] == [20.0]

    db2=DB()
    db2.add("kiki.py","py3",15.0,"")
    db2.add("kiki.py","py2",10.0,"")
    db2.add("kiki2.py","node",16.0,"")
    assert db2._db['kiki.py']['modes']['py3']["tests"] == [15.0]
    assert db2._db['kiki.py']['modes']['py2']["tests"] == [10.0]
    assert db2._db['kiki2.py']['modes']['node']["tests"] == [16.0]

    db3=db1+db2
    assert id(db1)==id(db3) # logic !
    assert db3._db['kiki.py']['modes']['py3']["tests"] == [12.0, 20.0, 15.0]
    assert db3._db['kiki.py']['modes']['py2']["tests"] == [10.0]
    assert db3._db['kiki2.py']['modes']['node']["tests"] == [20.0, 16.0]

    # assert db2 is not modified
    assert db2._db['kiki.py']['modes']['py3']["tests"] == [15.0]
    assert db2._db['kiki.py']['modes']['py2']["tests"] == [10.0]
    assert db2._db['kiki2.py']['modes']['node']["tests"] == [16.0]

    # and control summerization of db ...
    tt=list(db3)
    assert len(tt)==2
    # ... first file
    assert tt[0].filename == "kiki.py"
    assert list(tt[0]) == [('py3', 15.0, 3, 12.0, 20.0), ('py2', 10.0, 1, 10.0, 10.0)]
    # ... second file
    assert tt[1].filename == "kiki2.py"
    assert list(tt[1]) == [('node', 18.0, 2, 16.0, 20.0)]


#########################################################################
## helpers
#########################################################################
rr=lambda x: round(x,3)

todict = lambda x: dict( [[i.strip() for i in line.split(":",1) if ":" in line] for line in x.splitlines() if line.strip()] )


def myprint(*a,**k):
    k["flush"]=True
    print(*a,**k)

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
            # specific executable
            cmd=os.path.expanduser(v['e'])
        else:
            # guess executable
            cmd=shutil.which(v['e'])
            if cmd: 
                cmd=cmd.removesuffix(".exe")
        if cmd:
            # store the executable for this host
            LANGS[k]['e']=cmd.strip()

            try:
                # guess version
                cp=subprocess.run([LANGS[k]['e'],"--version"],text=True,capture_output=True)

                # store the version for this host
                LANGS[k]['v']=cp.stdout.splitlines()[0]
            except:
                try: # for go ;-(
                    # guess version
                    cp=subprocess.run([LANGS[k]['e'],"version"],text=True,capture_output=True)

                    # store the version for this host
                    LANGS[k]['v']=cp.stdout.splitlines()[0]
                except:
                    LANGS[k]['v']="???"

        else:
            print(f"*WARNING* no {k} lang (you can install '{v['e']}')!",file=sys.stderr)   # not in stdin !
            del LANGS[k]

def help():
    print(f"USAGE TEST: {os.path.relpath(__file__)} <file|folder> ... <option>")
    print(f"USAGE STAT: {os.path.relpath(__file__)} stats <file|folder> ... <option>")
    print("Tool to test and sort results from differents interpreters/languages")
    print("On the host:")
    print(get_info_host())
    print()
    print("Where <option> can be, to force a specific one:")

    print_info_comp("  --")
    
def print_info_comp(prefix=""):
    for k,v in sorted(LANGS.items()):
        cmd_build,cmd_run = get_commandlines(v,'<file>')
        print(f"{prefix}{k:5s} : {v['v']}")
        sprefix=" "*len(prefix)
        if cmd_build:
            print(f"{sprefix}        {cmd_build} && {cmd_run} < grids.txt")
        else:
            print(f"{sprefix}        {cmd_run} < grids.txt")



def sign(filename:str, mode:str, once:str) -> str:
    """Create a signature for the test based on
        - compilator (cmd line + version)
        - content of the file
        - and once
       -----------------------> md5
    """
    with open(filename, 'rb') as fid:
        compilator  = str(LANGS[mode]["v"]) + str(LANGS[mode]["c"])
        content=str( [i for i in fid if i.strip() and not i.strip().startswith( (b"#",b"//") ) ] )    # remove shebang/comments ;-)

        sign=content+compilator+once
        return hashlib.md5(sign.encode()).hexdigest()



def runcmd(input:str, cmd, pre_cmd=None, ):
    """ inject input in stdin of the command 'cmd' """
    """ in bash, could be : $ `cmd` < echo input """
    """ execute `pre_cmd` if defined (build phase)"""
    if pre_cmd:
        print("[build]",pre_cmd)
        cp = subprocess.run(pre_cmd,shell=True,text=True,capture_output=True)
        logging.info("runcmd: %s -> %s (pre cmd)",pre_cmd,cp.returncode)
        if cp.returncode!=0:
            raise Exception(f"ERROR runcmd: '{pre_cmd}'\n{cp.stderr}\n{cp.stdout}")
        
    print("[run]",cmd)
    t = time.monotonic()
    cp = subprocess.run(cmd,shell=True,text=True,input=input,capture_output=True)
    t = time.monotonic() - t
    logging.info("runcmd: %s -> %s (time:%s)",cmd,cp.returncode,t)
    if cp.returncode!=0:
        raise Exception(f"ERROR runcmd: '{cmd}'\n{cp.stderr}\n{cp.stdout}")
    return (t,cp.stdout)

#########################################################################
## run/batch methods
#########################################################################

def batch(files:list, opts:"list|None", nb_grids:int) -> int:
    """execute files, and if opts, restrict to lang from 'opts'"""
    file="?"
    found=False
    for file in files:
        if fnmatch.fnmatch(os.path.basename(file),TESTFILES):
            ext=file.split(".")[-1]
            for mode,langinfo in LANGS.items():
                if langinfo.get("ext") == ext:
                    if opts and mode not in opts:
                        continue
                    found=True
                    run( file,mode,nb_grids )        
    if not found:
        myprint(f"ERROR: didn't found a compiler for {file}")
        return -1
    else:
        return 0


def get_commandlines(d:dict,file:str) -> tuple:
    subcmd = lambda cmd,p0,p1: cmd.replace('$0',p0).replace('$1',p1)

    if isinstance(d["c"],tuple):
        cmd_build,cmd_run=d["c"]
    else:
        cmd_build=None
        cmd_run=d["c"]

    if cmd_build: cmd_build=subcmd(cmd_build,d["e"],file)
    if cmd_run:   cmd_run=subcmd(cmd_run,d["e"],file)

    return cmd_build,cmd_run

def run(file:str,lang:str, nb_grids:int) -> int:
    """ run file 'file' with the defined lang 'lang'"""
    db=HostTest()
    file=os.path.relpath(file)
    d = LANGS.get(lang)
    if d:
        t=do_the_test(lang,d,file, nb_grids)
        if t is None:
            return -1
        else:
            if nb_grids==NB_GRIDS:
                db.add(file,lang,t,str(NB_GRIDS))
            else:
                print("NOT SAVED")
            return 0
    else:
        help()
        return -1

#########################################################################
## stats methods
#########################################################################
def getinfo(file:str) -> str:
    """get info from the source file 'file'"""
    contents = open(file).read().splitlines()
    for i in contents:
        if i.startswith("//INFO:"):
            return i[7:].strip()
        elif i.startswith("#INFO:"):
            return i[6:].strip()
    return "?"

def print_stats_info(db):
    for item in db:
        if item.filename in files:
            tests = item.filter( opts )
            if tests:
                myprint(f"\n{item.filename} : {getinfo(item.filename)}")
                for mode,value,nb,vmin,vmax in tests:
                    myprint(f"  - {mode:5s} : {value:.03f} seconds ({nb}x, {vmin:.03f}><{vmax:.03f})")

def stats(files:list, opts:list):
    """ stats will displat only stats for current file that have the same signature !!!!"""
    print_stats_info( HostTest() )

def stats_results(files:list, opts:list):
    """ stats will displat only stats for current file that have the same signature !!!!"""
    f="RESULTS.TXT"
    if os.path.isfile(f):
        results=open(f,"r+").read().strip()
        print_stats_info( Snapshots(results) )
    else:
        print(f"no {f} file !")

def snapshot() -> str:
    """used by commandline"""
    """$ ./make.py snapshot >> ACCUMULATED_RESULTS.txt """
    db=HostTest()
    return db.snapshot()

if __name__=="__main__":
    test_DB()
    update()
    nb_grids=NB_GRIDS

    args=sys.argv[1:]
    ret=0

    if args:
        nb=1
        if args[0]=="stats":
            mode="stats"
            args.pop(0)
            if not [i for i in args if not i.startswith("--")]:
                # not files given in input, assuming '.'
                args.insert(0,".")
        elif args[0]=="snapshot":
            print( snapshot() )
            sys.exit(0)
        elif args[0]=="info":
            print( get_info_host() )
            print()
            print_info_comp()
            sys.exit(0)
        elif args[0]=="RESULTS":
            mode="RESULTS"
            args.pop(0)
            if not [i for i in args if not i.startswith("--")]:
                # not files given in input, assuming '.'
                args.insert(0,".")

        elif re.match(r"(\d+)x",args[0]):
            nb=int(re.match(r"(\d+)x",args[0])[1])
            mode="test"
            args.pop(0)
        else:
            mode="test"

        files=[]
        opts=[]
        for i in args:
            if i.startswith("--"):
                opt=i[2:].lower()
                if opt.isnumeric():
                    nb_grids = int(opt)
                else:
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

        files=[os.path.relpath(i) for i in sorted(files)]

        if mode=="test":
            for i in range(nb):
                ret=batch(files, opts , nb_grids)
        elif mode=="stats":
            ret=stats(files, opts)
        elif mode=="RESULTS":
            stats_results(files, opts)
            ret=0
    else:
        help()
    sys.exit(ret)
