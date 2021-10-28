import java.nio.file.Files;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.nio.file.Paths;

class Sudoku {

    //############################################### my resolver ;-) (backtracking)
    public static String square(String g, int x, int y) {
        x=(int)(x/3)*3;
        y=(int)(y/3)*3;
        return g.substring(y*9+x,y*9+x+3) + g.substring(y*9+x+9,y*9+x+12) + g.substring(y*9+x+18,y*9+x+21);
    }

    public static String vertiz(String g, int x) {
        String result = "";
        for(int y=0;y<9;y++){
            final int ligne=y*9;
            result += g.substring(x+ligne,x+ligne+1);
        }
        return result;
    }

    public static String horiz(String g, int y) {
        final int ligne=y*9;
        return g.substring(ligne, ligne+9);
    }

    public static Set<Character> freeset(String g) {
        Set<Character> result = "123456789".chars().mapToObj(e->(char)e).collect(Collectors.toSet());
        final Set<Character> s = g.chars().mapToObj(e->(char)e).collect(Collectors.toSet());
        result.removeAll(s);
        return result;
    }

    public static Set<Character> interset(String g, int x, int y) {
        Set<Character> result = freeset(horiz(g,y));
        result.retainAll( freeset(vertiz(g,x)) );
        result.retainAll( freeset(square(g,x,y)) );
        return result;
    }

    public static String resolv(String g) {
        final int i=g.indexOf(".");
        if(i>=0) {
            for(Character elem : interset(g,i%9,(int)i/9)) {
                final String ng=resolv( g.substring(0,i) + elem + g.substring(i+1,g.length()) );
                if(ng!=null)
                    return ng;
            }
            return null;
        }
        else
            return g;
    }
    //###############################################

    public static void main (String[] args) throws Exception{
        final List<String> gg=Files.readAllLines(Paths.get("g_simples.txt")).subList(0, 100);

        final long t=System.currentTimeMillis();
        for(String g: gg) {
            final String rg=resolv(g);
            if( !(rg!=null && rg.indexOf(".")<0)) throw new Exception("not resolved ?!");
            System.out.println(rg);
        }
        System.out.println("Took: "+( System.currentTimeMillis() - t)+"ms");
    }
}