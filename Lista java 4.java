import java.util.*;

class Main {
    public static void main(String[] args) {
        
        String palabra = "programacion";
        List<Character> vocales = new ArrayList<>();
        for (char c : palabra.toCharArray()) {
            if ("aeiou".indexOf(c) != -1) {
                vocales.add(c);
            }
        }
        System.out.println(" Vocales: " + vocales);
    }
}