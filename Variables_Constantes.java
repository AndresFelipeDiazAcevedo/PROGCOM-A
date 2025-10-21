package clase;

public class Variables_Constantes {

	public static void main(String[] args) {
		// Tipo de datos primitivo
		// Enteros - int
		int edad= 17;
		System.out.println("Mi edad es: "+edad);
		//Decimales
		double estatura=1.73;
		System.out.println("Mi estatura es: "+estatura+" metros");
		//System.out.println(edad);
		
		//alfanumerico
		String nombre="Andres";
		System.out.println(nombre.getClass().getSimpleName());
		//char - un solo caracter
		char a='s';
		
		
		//Booleano
		boolean verdad=true;
		
		var flor="Holitas";
		System.out.println(flor);
		
		final String mail="adiaz277@unab.edu.co";
		System.out.println(mail);
		//mail="andresda.diaz10@gmail.com";
		//System.out.println(mail);

	}

}
