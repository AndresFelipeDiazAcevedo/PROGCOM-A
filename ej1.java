import java.util.*;

class Main {
    public static void main(String[] args) {
  Scanner input = new Scanner(System.in);
    byte numero = input.nextByte();
    
    if(numero >= 0) {
        System.out.println("El numero es positivo");
    }else{
        System.out.println("El numero es negativo");
    }
        }
    // esta es la segunda forma
    {
        Scanner input = new Scanner(System.in);
        byte numero = input.nextByte();
    
        if(numero > 0) {
            System.out.println("El numero es positivo");
        }else if (numero < 0){
            System.out.println("El numero es negativo");
        }else{
            System.out.println("El numero es 0, osea neutro");
        }
        
// esta es la tercera fornma
    {
        System.out.println(numero >= 0 ? "El numero es positivo" : "El numero es negativo");

    }
    
}
