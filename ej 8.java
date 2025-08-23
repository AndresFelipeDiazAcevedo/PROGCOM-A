import java.util.*;

class Main {
    public static void main(String[] args) {

        {
            Scanner input = new Scanner(System.in);
            System.out.print("Ingresa tu contraseña: ");
            String pass = input.nextLine();

            if (pass.length() < 8) {
                System.out.println("Contraseña inválida: debe tener mínimo 8 caracteres");
            } else {
                if (!pass.matches(".*[A-Z].*")) {
    // lo de pass matches es que algo coincida y ps en este caso lo de A y Z es que sea mayuscula, y ya lo de *" es pq hay algo antes o despues 
                    System.out.println("Contraseña inválida: debe tener al menos una letra mayúscula");
                } else {
                    if (!pass.matches(".*[0-9].*")) {
                        System.out.println("Contraseña inválida: debe tener al menos un número");
                    } else {
                        System.out.println("Contraseña válida ");
                    }
                }
            }
        }
        {
            Scanner input = new Scanner(System.in);
            System.out.print("Ingresa tu contraseña: ");
            String pass = input.nextLine();

            if (pass.length() < 8) {
                System.out.println("Contraseña inválida: debe tener mínimo 8 caracteres");
            } else if (!pass.matches(".*[A-Z].*")) {
                System.out.println("Contraseña inválida: debe tener al menos una letra mayúscula");
            } else if (!pass.matches(".*[0-9].*")) {
                System.out.println("Contraseña inválida: debe tener al menos un número");
            } else {
                System.out.println("Contraseña válida ");
            }
        }

        {
            Scanner input = new Scanner(System.in);
            System.out.print("Ingresa tu contraseña: ");
            String pass = input.nextLine();

            System.out.println(
                (pass.length() < 8) ? "Contraseña inválida: debe tener mínimo 8 caracteres" :(!pass.matches(".*[A-Z].*")) ? "Contraseña inválida: debe tener al menos una letra mayúscula" : (!pass.matches(".*[0-9].*")) ? "Contraseña inválida: debe tener al menos un número" :"Contraseña válida ✅");
        }
    }
}