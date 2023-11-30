#!./make.py
//INFO: the simple algo, with strings (AI translation from java one) (100grids)

// Import the necessary modules
const fs = require('fs');

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

    static free(g, x, y) {
        let t27= this.row(g, y) + this.col(g, x) + this.sqr(g, x, y);
        let all="123456789";
        let freeset="";
    
        for (let i = 0; i < 9; i++) {
            let c=all[i];
            if(t27.indexOf( c )<0)
                freeset+=c;
        }
        return freeset;    
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
        // Solve each Sudoku puzzle
        for (const puzzle of puzzles)
            console.log(this.resolv(puzzle));
    }
}

// Call the main method
Sudoku.main();
