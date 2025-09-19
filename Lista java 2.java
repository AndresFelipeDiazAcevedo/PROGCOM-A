import java.util.*;

class Main {
    public static void main(String[] args) {
   
        List<Integer> pares = new ArrayList<>();
        for (int i = 0; i <= 20; i++) {
            if (i % 2 == 0) pares.add(i);
        }
        System.out.println(" Pares del 0 al 20: " + pares);
    }
}