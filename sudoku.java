//java has a shebang mechanism fully dumb
//INFO: algo with strings
import java.util.Scanner;
import java.nio.file.Files;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.nio.file.Paths;

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
        int ibest=-1;
        String cbest = "123456789";
    
        for(int i=0;i<81;i++) {
            if(g.charAt(i)=='.') {
                String c=free(g,i%9,(int)i/9);
                if(c.length() ==0 )
                    return null;
                if(c.length() < cbest.length()) {
                    ibest = i;
                    cbest = c;
                }
                if(c.length()==1)
                    break;
            }
        }
    
        if(ibest>=0) {
            for(int j = 0; j < cbest.length(); j++) {
                final char elem=cbest.charAt(j);            
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
        // final List<String> gg=Files.readAllLines(Paths.get("grids.txt"));

        // for(String g: gg)
        //     System.out.println( resolv(g) );

        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext() )
            System.out.println(resolv(scanner.nextLine()));
    }
}

