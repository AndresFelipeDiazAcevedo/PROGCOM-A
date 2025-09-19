import java.util.*;

class Main {
    public static void main(String[] args) {
        
        List<String> palabras = Arrays.asList("sol", "estrella", "mar", "planeta");
        List<String> largas = new ArrayList<>();
        for (String p : palabras) {
            if (p.length() > 4) {
                largas.add(p);
            }
        }
        System.out.println(" Palabras largas: " + largas);

    }
}