import java.util.*;

class Main {
    public static void main(String[] args) {
       
        Scanner input = new Scanner(System.in);
        System.out.println("Ingresa un numero:");
        int numero = input.nextInt();
        if (numero % 2 == 0) {
            System.out.println("El numero es par");
        } else {
            System.out.println("El numero es impar");
        }
    }
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Ingresa un número:");
        int numero = input.nextInt();
        if (numero % 2 == 0) {
            System.out.println("El numero es par");
        } else if (numero == 0) {
            System.out.println("Es 0 y puede que sea par");
        } else {
            System.out.println("El numero es impar ");
        }
    }
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Ingresa un numero:");
        int numero = input.nextInt();
        System.out.println(numero % 2 == 0 ? "El numero es par" : "El numero es impar");
    }
}
