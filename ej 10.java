import java.util.*;

class Main {
    public static void main(String[] args) {
        int ClavePredeterminada = 2624;
        int Disponible = 1000000;

        Scanner input = new Scanner(System.in); 

        System.out.print("Ingrese la clave: ");
        int clave = input.nextInt();

        if (clave == ClavePredeterminada) {
            System.out.print("¿Qué valor desea retirar?: ");
            int dinero = input.nextInt();

            if (dinero <= Disponible) {
                System.out.println("Ha retirado correctamente " + dinero);
            } else {
                System.out.println("Saldo insuficiente");
            }
        } else {
            System.out.println("Clave incorrecta");
        }
        System.out.print("Ingrese la clave: ");
        clave = input.nextInt();

        if (clave == ClavePredeterminada) {
            System.out.print("¿Qué valor desea retirar?: ");
            int dinero = input.nextInt();

            if (dinero <= 0) {
                System.out.println("No se puede retirar dinero negativo");
            } else if (dinero <= Disponible) {
                System.out.println("Ha retirado correctamente " + dinero);
            } else {
                System.out.println("Saldo insuficiente");
            }
        } else {
            System.out.println("Clave incorrecta");
        }


        System.out.print("Ingrese la clave: ");
        clave = input.nextInt();
        String resultado;

        if (clave == ClavePredeterminada) {
            System.out.print("¿Qué valor desea retirar?: ");
            int dinero = input.nextInt();

            resultado = (dinero <= Disponible)? "Ha retirado correctamente " + dinero: "Saldo insuficiente";
        } else {
            resultado = "Clave incorrecta";
        }

        System.out.println(resultado);
    }
}

