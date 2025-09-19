import java.util.*;

class Main {
    public static void main(String[] args) {
         
        List<String> lenguajes = Arrays.asList("python", "java", "c++");
        List<String> mayusculas = new ArrayList<>();
        for (String l : lenguajes) {
            mayusculas.add(l.toUpperCase());
        }
        System.out.println(" Mayúsculas: " + mayusculas);
    }
}