import java.nio.file.Files;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.nio.file.Paths;
//INFO: the simple algo, with strings (100grids)

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

    public static String free(String g, int x, int y) {
        final String all="123456789";
        final String t27=row(g,y) + col(g,x) + sqr(g,x,y);
        String freeset="";
    
        for (int i = 0; i < 9; i++) {
            final char c=all.charAt(i);
            if(t27.indexOf( c )<0)
                freeset+=c;
        }
        return freeset;
    }

    public static String resolv(String g) {
        final int i=g.indexOf(".");
        if(i>=0) {
            String freeset=free(g,i%9,(int)i/9);
            for(int j = 0; j < freeset.length(); j++) {
                final char elem=freeset.charAt(j);
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
        final List<String> gg=Files.readAllLines(Paths.get("grids.txt")).subList(0, 100);

        for(String g: gg)
            System.out.println(resolv(g));
    }
}