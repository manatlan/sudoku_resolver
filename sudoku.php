<?php

declare(strict_types=1);

namespace Sudoku;

final class SudokuSolver
{
    public function sqr(string $g, int $x, int $y): string
    {
        $x = intdiv($x, 3) * 3;
        $y = intdiv($y, 3) * 3;

        return substr($g, $y * 9 + $x, 3)
            . substr($g, $y * 9 + $x + 9, 3)
            . substr($g, $y * 9 + $x + 18, 3);
    }

    public function col(string $g, int $x): string
    {
        $result = '';
        for ($y = 0; $y < 9; ++$y) {
            $result .= $g[$x + $y * 9];
        }

        return $result;
    }

    public function row(string $g, int $y): string
    {
        return substr($g, $y * 9, 9);
    }

    public function free(string $g, int $x, int $y): string
    {
        $all = '123456789';
        $t27 = $this->row($g, $y) . $this->col($g, $x) . $this->sqr($g, $x, $y);
        $freeset = '';

        for ($i = 0; $i < 9; ++$i) {
            $c = $all[$i];
            if (strpos($t27, $c) === false) {
                $freeset .= $c;
            }
        }

        return $freeset;
    }

    public function resolv(string $g): ?string
    {
        $ibest = -1;
        $cbest = '123456789';

        for ($i = 0; $i < 81; ++$i) {
            if ($g[$i] === '.') {
                $c = $this->free($g, $i % 9, intdiv($i, 9));
                if ($c === '') {
                    return null;
                }
                if (strlen($c) < strlen($cbest)) {
                    $ibest = $i;
                    $cbest = $c;
                }
                if (strlen($c) === 1) {
                    break;
                }
            }
        }

        if ($ibest >= 0) {
            for ($j = 0; $j < strlen($cbest); ++$j) {
                $elem = $cbest[$j];
                $ng = $this->resolv(substr($g, 0, $ibest) . $elem . substr($g, $ibest + 1));
                if ($ng !== null) {
                    return $ng;
                }
            }

            return null;
        }

        return $g;
    }
}

$solver = new SudokuSolver();

/*
$lines = array_slice(explode("\n", file_get_contents(__DIR__ . '/grids.txt')), 0, 1956);

foreach ($lines as $line) {
    echo $solver->resolv($line) . "\n";
}
*/

$f = fopen('php://stdin', 'r');

while(($line = fgets($f)) !== false) {
    echo $solver->resolv($line) . "\n";
}
