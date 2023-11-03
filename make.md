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

It will show you the command line options

## to run one version

Just type (example: the rust one)

```
$ ./make.py sudoky.rs
```

Just type (example: the python one)

```
$ ./make.py sudoky.py
```

Note, that it will run with every things that can run a python file (on my host : pypy, py3.7, py3.11, codon)

To force only one interpreter, specify the mode

```
$ ./make.py sudoky.py --pypy
```

It will run it against pypy only !

## to run every files

Just give the folder, so :

```
$ ./make.py .
```

Will run every sources

if you want to run the "optimized" versions :

```
$ ./make.py optimized
```

if you want to run the "optimized" versions, only mojo ones:

```
$ ./make.py optimized --mojo
```

## run all tests

Just type :
```
$ ./make.py . optimized experiments
```

## to get stats

To output json stats:
```
$ ./make.py stats
```

To output humans readable stats:
```
$ ./make.py hstats
```
