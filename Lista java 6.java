import java.util.*;

class Main {
    public static void main(String[] args) {
        
        List<String> parOImpar = new ArrayList<>();
        for (int i = 1; i <= 10; i++) {
            parOImpar.add(i % 2 == 0 ? "par" : "impar");
        }
        System.out.println(" Par o impar: " + parOImpar);
    }
}