#!./make.py
//INFO: the simple algo, with strings (AI translation from java one)

// Import the necessary modules
const fs = require('fs');

function difference(setA, setB) {
  let _difference = new Set(setA);
  for (let elem of setB) {
    _difference.delete(elem);
  }
  return _difference;
}

// Define the Sudoku class
class Sudoku {

    //############################################### my resolver ;-) (backtracking)
    // Convert the `square()` method to JavaScript
    static sqr(g, x, y) {
        x = Math.floor(x / 3) * 3;
        y = Math.floor(y / 3) * 3;
        return g.substring(y * 9 + x, y * 9 + x + 3)
            + g.substring(y * 9 + x + 9, y * 9 + x + 12)
            + g.substring(y * 9 + x + 18, y * 9 + x + 21);
    }

    // Convert the `vertiz()` method to JavaScript
    static col(g, x) {
        let result = '';
        for (let y = 0; y < 9; y++) {
            const ligne = y * 9;
            result += g.substring(x + ligne, x + ligne + 1);
        }
        return result;
    }

    // Convert the `horiz()` method to JavaScript
    static row(g, y) {
        const ligne = y * 9;
        return g.substring(ligne, ligne + 9);
    }

    // Convert the `freeset()` method to JavaScript
    static freeset(g) {
        const result = new Set("123456789".split(''));
        const s = new Set(g.split(''));
        return difference(result,s)
    }

    // Convert the `interset()` method to JavaScript
    static free(g, x, y) {
        return this.freeset( this.row(g, y) + this.col(g, x) + this.sqr(g, x, y))
    }

    // Convert the `resolv()` method to JavaScript
    static resolv(g) {
        const i = g.indexOf('.');
        if (i >= 0) {
            for (const elem of this.free(g, i % 9, Math.floor(i / 9))) {
                const ng = this.resolv(g.substring(0, i) + elem + g.substring(i + 1, g.length));
                if (ng !== null)
                    return ng;
            }
            return null;
        } else
            return g;
   }
    //###############################################

    // Define the main method
    static main(args) {
        // Read the Sudoku puzzles from the file
        const puzzles = fs.readFileSync('grids.txt', 'utf-8').split('\n').slice(0, 100);

        // Start the timer
        const startTime = Date.now();

        // Solve each Sudoku puzzle
        for (const puzzle of puzzles) {
            const solvedPuzzle = this.resolv(puzzle);
            if (solvedPuzzle === null || solvedPuzzle.indexOf('.') >= 0) {
                throw new Error('Sudoku puzzle not solved!');
            }
            console.log(solvedPuzzle);
        }

        // Stop the timer and print the elapsed time
        console.log('Took: ' + ((Date.now() - startTime)/1000.0) + 's');
    }
}

// Call the main method
Sudoku.main();
