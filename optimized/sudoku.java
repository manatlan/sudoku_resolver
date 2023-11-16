import java.nio.file.Files;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.nio.file.Paths;
//INFO: the optimized algo, with strings (1956grids)

class Sudoku {

    //############################################### my resolver ;-) (backtracking)
    public static String sqr(String g, int x, int y) {
        x=(int)(x/3)*3;
        y=(int)(y/3)*3;
        return g.substring(y*9+x,y*9+x+3) + g.substring(y*9+x+9,y*9+x+12) + g.substring(y*9+x+18,y*9+x+21);
    }

    public static String col(String g, int x) {
        String result = "";
        for(int y=0;y<9;y++){
            final int ligne=y*9;
            result += g.substring(x+ligne,x+ligne+1);
        }
        return result;
    }

    public static String row(String g, int y) {
        final int ligne=y*9;
        return g.substring(ligne, ligne+9);
    }

    public static Set<Character> freeset(String g) {
        Set<Character> result = "123456789".chars().mapToObj(e->(char)e).collect(Collectors.toSet());
        final Set<Character> s = g.chars().mapToObj(e->(char)e).collect(Collectors.toSet());
        result.removeAll(s);
        return result;
    }

    public static Set<Character> free(String g, int x, int y) {
        return freeset(row(g,y) + col(g,x) + sqr(g,x,y));
    }

    public static String resolv_old(String g) {
        final int i=g.indexOf(".");
        if(i>=0) {
            for(Character elem : free(g,i%9,(int)i/9)) {
                final String ng=resolv( g.substring(0,i) + elem + g.substring(i+1,g.length()) );
                if(ng!=null)
                    return ng;
            }
            return null;
        }
        else
            return g;
    }

    public static String resolv(String g) {
        int ibest=-1;
        Set<Character> cbest = "123456789".chars().mapToObj(e->(char)e).collect(Collectors.toSet());
    
        for(int i=0;i<81;i++) {
            if(g.charAt(i)=='.') {
                Set<Character> c=free(g,i%9,(int)i/9);
                if(c.size() ==0)
                    return null;
                if(c.size() < cbest.size()) {
                    ibest = i;
                    cbest = c;
                }
                if(c.size()==1)
                    break;
            }
        }
    
        if(ibest>=0) {
            for(Character elem : cbest) {
                final String ng=resolv( g.substring(0,ibest) + elem + g.substring(ibest+1,g.length()) );
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
        final List<String> gg=Files.readAllLines(Paths.get("grids.txt"));

        final long t=System.currentTimeMillis();
        for(String g: gg) {
            final String rg=resolv(g);
            if( !(rg!=null && rg.indexOf(".")<0)) throw new Exception("not resolved ?!");
            System.out.println(rg);
        }
        System.out.println("Took: "+(( System.currentTimeMillis() - t)/1000.0)+"s");
    }
}
