import java.util.*;

class Main {
    public static void main(String[] args) {
        List<Integer> cuadrados = new ArrayList<>();
        for (int i = 1; i <= 10; i++) {
            cuadrados.add(i * i);
        }
        System.out.println("1) Cuadrados del 1 al 10: " + cuadrados);
    }
}