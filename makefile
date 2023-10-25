mojo:	# 0.4.0 
	mojo run sudoku.mojo

nim:	# 1.6.14
	nim r -d:danger sudoku.nim

java:	# openjdk 22-ea 
	java sudoku.java

node:	# v18.13.0
	node sudoku.js

codon: 	# 0.16.3
	~/.codon/bin/codon run -release sudoku.py

pypy:
	~/Téléchargements/pypy3.10-v7.3.13-linux64/bin/pypy3 -uOO sudoku.py 

py37:
	python3.7 -uOO sudoku.py

py311:
	python3.11 -uOO sudoku.py

c:
	gcc sudoku.c && ./a.out


