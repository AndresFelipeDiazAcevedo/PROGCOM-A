import java.util.*;

class Main {
    public static void main(String[] args) {
        System.out.println("Ingresa la edad del usuario:");
        Scanner input = new Scanner(System.in);
        byte edad = input.nextByte();
        if(edad >= 18) {
            System.out.println("Es mayor de edad");
        }else{
            System.out.println("Es menor de edad");
        }
    }
        
        {
        System.out.println("Ingresa la edad del usuario:");
        Scanner input = new Scanner(System.in);
        byte edad = input.nextByte();
        if(edad >= 21) {
            System.out.println("Es mayor de edad en todos los paises del mundo");
        } else if (edad >= 18){
            System.out.println("Es mayor de edad en colombia");
        }else{
            System.out.println("Es menor de edad");
        }
        }
    {
        System.out.println("Ingresa la edad del usuario:");
        Scanner input = new Scanner(System.in);
        byte edad = input.nextByte();
        System.out.println(edad >= 18 ? "Es mayor de edad" : "Es menor de edad.");
    }
    }

      
            
