public class Casa {
    protected String color;
    protected int numero_habitaciones;
    protected int numero_plantas;
    protected boolean tiene_jardin;
    protected boolean tiene_terraza;

    public Casa(String color, int numero_habitaciones, int numero_plantas, boolean tiene_jardin, boolean tiene_terraza) {
        this.color = color;
        this.numero_habitaciones = numero_habitaciones;
        this.numero_plantas = numero_plantas;
        this.tiene_jardin = tiene_jardin;
        this.tiene_terraza = tiene_terraza;
    }

    public String descripcion() {
        String descripcion = "La casa es de color " + this.color +
                ", tiene " + this.numero_habitaciones + " habitaciones y " + this.numero_plantas + " plantas.";
        if (this.tiene_jardin) {
            descripcion += " Tiene un jardín amplio y bien cuidado.";
        }
        if (this.tiene_terraza) {
            descripcion += " También cuenta con una terraza perfecta para descansar.";
        }
        return descripcion;
    }

    public void pintar(String nuevoColor) {
        this.color = nuevoColor;
        System.out.println("La casa ahora está pintada de " + this.color + ".");
    }
}


