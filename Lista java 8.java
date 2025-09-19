import java.util.*;

class Main {
    public static void main(String[] args) {
        
        String[] letras = {"a", "b"};
        int[] numeros = {1, 2, 3};
        List<String> combinaciones = new ArrayList<>();
        for (String l : letras) {
            for (int n : numeros) {
                combinaciones.add(l + n);
            }
        }
        System.out.println(" Combinaciones: " + combinaciones);
    
    }
}