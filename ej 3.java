import java.util.*;

class Main {
    public static void main(String[] args) {
        System.out.println("Ingresa a:");
        Scanner input = new Scanner(System.in);
        byte a = input.nextByte();
        System.out.println("Ingresa b:");
        byte b = input.nextByte();
        if (a>b){
            System.out.println("a es mayor que b");
        }else{
            System.out.println("b es mayor que a");
        }
    }
    {
        System.out.println("Ingresa a:");
        Scanner input = new Scanner(System.in);
        byte a = input.nextByte();
        System.out.println("Ingresa b:");
        byte b = input.nextByte();
        if (a>b){
            System.out.println("a es mayor que b");
        }else if (b>a) {
            System.out.println("b es mayor que a");
        }else {
            System.out.println("los numeros son iguales");
        }
    }
    {
        System.out.println("Ingresa a:");
        Scanner input = new Scanner(System.in);
        byte a = input.nextByte();
        System.out.println("Ingresa b:");
        byte b = input.nextByte();
        System.out.println(a>b ? "a es mayor que b" : "b es mayor que a");
    }
}