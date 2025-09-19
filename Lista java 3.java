import java.util.*;

class Main {
    public static void main(String[] args) {
        
        List<Integer> dobles = new ArrayList<>();
        for (int i = 1; i <= 5; i++) {
            dobles.add(i * 2);
        }
        System.out.println(" Dobles del 1 al 5: " + dobles);
    }
}