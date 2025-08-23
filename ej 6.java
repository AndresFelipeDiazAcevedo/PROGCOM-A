import java.util.*;

class Main {
    public static void main(String[] args) {
        System.out.println("Ingresa tres números:");
        Scanner input = new Scanner(System.in);
        byte a = input.nextByte();
        byte b = input.nextByte();
        byte c = input.nextByte();

// si pongo +a o asi es para que de esa forma salga el numero y no a o b o c y asi 
        if (a > b) {
            if (a > c) {
                System.out.println("El mayor es: " + a);
            } else {
                System.out.println("El mayor es: " + c);
            }
        } else {
            if (b > c) {
                System.out.println("El mayor es: " + b);
            } else {
                System.out.println("El mayor es: " + c);
            }
        }
    }
    {
        System.out.println("Ingresa tres números:");
        Scanner input = new Scanner(System.in);
        byte a = input.nextByte();
        byte b = input.nextByte();
        byte c = input.nextByte();

        
// && esto es un and por si acaso JAKJAK
        if (a >= b && a >= c) {
            System.out.println("El mayor es: " + a);
        } else if (b >= a && b >= c) {
            System.out.println("El mayor es: " + b);
        } else {
            System.out.println("El mayor es: " + c);
        }
    }
    {
        System.out.println("Ingresa tres números:");
        Scanner input = new Scanner(System.in);
        byte a = input.nextByte();
        byte b = input.nextByte();
        byte c = input.nextByte();

        System.out.println((a >= b && a >= c) ? "El mayor es: " + a : 
                           (b >= a && b >= c ? "El mayor es: " + b : "El mayor es: " + c));
    }
}
