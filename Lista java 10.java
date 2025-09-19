import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);  

        
        List<Integer> temps = new ArrayList<>();

        System.out.println("Ingrese 10 temperaturas:");
        for (int i = 0; i < 10; i++) {
            int temp = sc.nextInt();  // bueno en este paso se lee el entero
            temps.add(temp);          // y ps aca se guarda
        }

        List<String> clima = new ArrayList<>();

        for (int t : temps) {
            if (t < 20) {
                clima.add("frío");
            } else if (t <= 27) {
                clima.add("templado");
            } else {
                clima.add("caliente");
            }
        }
        System.out.println("Clasificación del clima: " + clima);

    }
}
