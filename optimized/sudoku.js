#!./make.py
//INFO: the optimized algo, with strings (AI translation from java one) (1956grids)

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
        let ibest = -1;
        let cbest = '123456789';
    
        for (let i = 0; i < 81; i++) {
            if (g.charAt(i) === '.') {
                const c = this.free(g, i % 9, Math.floor(i / 9));
                if (c.length == 0) return null;
                if (c.length < cbest.length) {
                    ibest = i;
                    cbest = c;
                }
                if (c.length == 1) break;
            }
        }
    
        if (ibest >= 0) {
            for (let j = 0; j < cbest.length; j++) {
                const elem = cbest.charAt(j);
                const ng =
                    this.resolv(g.substring(0, ibest) + elem + g.substring(ibest + 1));
                if (ng != null) return ng;
            }
            return null;
        } else return g;
    }
    //###############################################

    // Define the main method
    static main(args) {
        // Read the Sudoku puzzles from the file
        const puzzles = fs.readFileSync('grids.txt', 'utf-8').split('\n').slice(0, 1956);
        // Solve each Sudoku puzzle
        for (const puzzle of puzzles)
            console.log(this.resolv(puzzle));
    }
}

// Call the main method
Sudoku.main();
