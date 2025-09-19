import java.util.*;

lass Main {
    public static void main(String[] args) {
    
        List<String> tuplas = new ArrayList<>();
        for (int i = 1; i <= 5; i++) {
            tuplas.add("(" + i + ", " + (i * i) + ")");
        }
        System.out.println(" Tuplas: " + tuplas);
    }
}