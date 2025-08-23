import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Ingresa la calificación 0-100:");
        int calificacion = input.nextInt();
        if (calificacion >= 60) {
            System.out.println("Aprobado ");
        } else {
            System.out.println("Reprobado ");
        }
    }
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Ingresa la calificación 0-100:");
        int calificacion = input.nextInt();
        if (calificacion >= 90) {
            System.out.println("Aprobado con honores");
        } else if (calificacion >= 60) {
            System.out.println("Aprobado ");
        } else {
            System.out.println("Reprobado");
        }
    }
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Ingresa la calificación (0-100):");
        int calificacion = input.nextInt();
        System.out.println(calificacion >= 60 ? "Aprobado " : "Reprobado ");
    }
}
