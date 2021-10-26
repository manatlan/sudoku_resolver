import java.nio.file.Files;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import java.nio.file.Paths;
import java.io.IOException;

class Sudoku {

    public static Set<Character> interset(String g,int x, int y) {
        Set<Character> s = freeset(horiz(g,y));
        s.retainAll( freeset(vertiz(g,x)) );
        s.retainAll( freeset(square(g,x,y)) );
        return s;
    }

    public static Set<Character> freeset(String g) {
        Set<Character> s = g.chars().mapToObj(e->(char)e).collect(Collectors.toSet());
        Set<Character> sf = "123456789.".chars().mapToObj(e->(char)e).collect(Collectors.toSet());
        sf.removeAll(s);
        return sf;
    }

    public static String resolv(String g) {
        int i=g.indexOf(".");
        if(i>=0) {
            for(Character elem : interset(g,i%9,(int)i/9)) {
                String ng=resolv( g.substring(0,i) + elem + g.substring(i+1,g.length()) );
                if(ng!=null)
                    return ng;
            }
            return null;
        }
        else
            return g;
    }
    public static String square(String g, int x, int y) {
        x=(int)(x/3)*3;
        y=(int)(y/3)*3;
        return g.substring(y*9+x,y*9+x+3) + g.substring(y*9+x+9,y*9+x+12) + g.substring(y*9+x+18,y*9+x+21);
    }

    public static String horiz(String g, int y) {
        int ligne=y*9;
        return g.substring(ligne, ligne+9);
    }
    public static String vertiz(String g, int x) {
        String result = "";
        for(int y=0;y<9;y++){
            int ligne=y*9;
            result+= g.substring(x+ligne,x+ligne+1);
        }
        return result;
    }

    public static void main (String[] args) throws IOException{
        // String g="2.48........7.5....13.....9..7.......26....3.3...26.4...9..845.87.....16....6.2..";

        // System.out.println(horiz(g,0));
        // System.out.println(vertiz(g,0));
        // System.out.println(square(g,0,0));
        // System.out.println(freeset("123"));
        // System.out.println(interset(g,1,1));
        // System.out.println(g);
        // System.out.println(resolv(g));

        int c=0;
        for(String g: Files.readAllLines(Paths.get("g_simples.txt"))) {
            System.out.println(resolv(g));
            c+=1;
            if(c>100) break;
        }
    }
}