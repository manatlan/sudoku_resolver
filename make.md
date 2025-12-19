# make.py

It's a "python3 script" to make the whole process easier (it replace the old `makefile`, by adding a lot of features)

To use it, on your own, you should add execute rights :

```
$ chmod +x make.py
```

It should be able to auto-detect compiler/interpreter availables on your computer, and get infos about the versions.
(all results are saved in an `outputs` folders)

## to get help

Just type

```
$ ./make.py
```

It will show you the command line options, and all detected languages and command lines.

## to run one version

Just type (example: the rust one)

```
$ ./make.py sudoku.rs
```

Just type (example: the python one)

```
$ ./make.py sudoku.py
```

Note, that it will run with every things that can run a python file (on my host : pypy, py3.7, py3.11, codon)

To force only one interpreter, specify the mode

```
$ ./make.py sudoku.py --pypy
```

It will run it against pypy only !

## to run every files

Just give the folder, so :

```
$ ./make.py .
```

Will run every sources

if you want to run the "specialized" versions :

```
$ ./make.py specialized
```

if you want to run the "specialized" versions, only mojo ones:

```
$ ./make.py specialized --mojo
```

## run all tests

Just type :
```
$ ./make.py . specialized
```

## to get stats

To output stats:
```
$ ./make.py stats
```

To output specifics stats of all mojo files:
```
$ ./make.py stats *.mojo
```

To output specifics stats of specialized versions:
```
$ ./make.py stats specialized/
```

## to get platform info

```
$ ./make.py info
```
