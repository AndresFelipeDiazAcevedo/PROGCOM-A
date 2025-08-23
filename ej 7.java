import java.util.*;

class Main {
    public static void main(String[] args) {
        System.out.println("Ingresa un año:");
        Scanner input = new Scanner(System.in);
        int año = input.nextInt();

        if (año % 4 == 0) {
            System.out.println("El año " + año + " es bisiesto ");
        } else {
            System.out.println("El año " + año + " no es bisiesto ");
        }
    }
    {
        System.out.println("Ingresa un año:");
        Scanner input = new Scanner(System.in);
        int año = input.nextInt();

        if (año % 400 == 0) {
            System.out.println("El año " + año + " es bisiesto ");
        } else if (año % 100 == 0) {
            System.out.println("El año " + año + " no es bisiesto ");
        } else if (año % 4 == 0) {
            System.out.println("El año " + año + " es bisiesto ");
        } else {
            System.out.println("El año " + año + " no es bisiesto ");
        }
    }
    {
        System.out.println("Ingresa un año:");
        Scanner input = new Scanner(System.in);
        int año = input.nextInt();

        System.out.println(año % 4 == 0 ? "El año " + año + " es bisiesto "
                                        : "El año " + año + " no es bisiesto ");
    }
}
