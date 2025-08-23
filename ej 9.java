import java.util.*;

class Main {
    public static void main(String[] args) {
            Scanner input = new Scanner(System.in);
            System.out.print("Ingresa un número: ");
            int num = input.nextInt();

            if (num % 3 == 0 && num % 5 == 0) {
                System.out.println("FizzBuzz");
            } else {
                if (num % 3 == 0) {
                    System.out.println("Fizz");
                } else {
                    if (num % 5 == 0) {
                        System.out.println("Buzz");
                    } else {
                        System.out.println("No es divisible entre 3 ni 5");
                    }
                }
            }
        }
        {
            Scanner input = new Scanner(System.in);
            System.out.print("Ingresa un número: ");
            int num = input.nextInt();

            if (num % 3 == 0 && num % 5 == 0) {
                System.out.println("FizzBuzz");
            } else if (num % 3 == 0) {
                System.out.println("Fizz");
            } else if (num % 5 == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println("No es divisible entre 3 ni 5");
            }
        }

        {
            Scanner input = new Scanner(System.in);
            System.out.print("Ingresa un número: ");
            int num = input.nextInt();

            System.out.println((num % 3 == 0 && num % 5 == 0) ? "FizzBuzz" :(num % 3 == 0) ? "Fizz" :(num % 5 == 0) ? "Buzz" :"No es divisible entre 3 ni 5");
        }
    }
}
