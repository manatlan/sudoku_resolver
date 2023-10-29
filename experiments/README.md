Here are others versions for tests purposes:

- `sudoku_faster.mojo` is my attempt to optimize the original algo, with mojo/lang optimizations (not the algo!)
- `mojodojodev.mojo` is another algo from mojodojodev https://mojodojo.dev/guides/benchmarks/sudoku.html 
- `mojodojodev.py` is the py version of mojodojodev ^^ (a lot slower than my sudoku.py version)


Same algo + "choosing the most constrained digit each iteration" (a lot faster!!!!), **for the 1011 grids** :
- `sudoku_optim.rs` 7 seconds 
- `sudoku_optim.py` 14.7 seconds 
