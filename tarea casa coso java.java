public class Casa {
    private String colorParedDelantera;
    private String colorParedTrasera;
    private String colorParedesLaterales;
    private int numero_habitaciones;
    private int numero_plantas;
    private boolean tiene_jardin;
    private boolean tiene_terraza;

    public Casa(int numero_habitaciones, int numero_plantas, boolean tiene_terraza) {
        this.colorParedDelantera = "blanca con puntos azules";
        this.colorParedTrasera = "verde";
        this.colorParedesLaterales = "blancas con rayas azules";
        this.numero_habitaciones = numero_habitaciones;
        this.numero_plantas = numero_plantas;
        this.tiene_jardin = false; // No tiene jardín
        this.tiene_terraza = tiene_terraza;
    }

    public String descripcion() {
        String descripcion = "La casa tiene " + this.numero_habitaciones + " habitaciones y " + this.numero_plantas + " plantas.\n";
        descripcion += "La pared delantera es " + this.colorParedDelantera + ", la pared trasera es de color " + this.colorParedTrasera +
                " y las paredes laterales son " + this.colorParedesLaterales + ".\n";
        
        if (!this.tiene_jardin) {
            descripcion += "No tiene jardín.\n";
        }
        if (this.tiene_terraza) {
            descripcion += "Cuenta con una terraza perfecta para descansar.";
        }
        return descripcion;
    }

    public void pintarParedDelantera(String nuevoColor) {
        this.colorParedDelantera = nuevoColor;
        System.out.println("La pared delantera ahora es " + this.colorParedDelantera + ".");
    }

    public void pintarParedTrasera(String nuevoColor) {
        this.colorParedTrasera = nuevoColor;
        System.out.println("La pared trasera ahora es " + this.colorParedTrasera + ".");
    }

    public void pintarParedesLaterales(String nuevoColor) {
        this.colorParedesLaterales = nuevoColor;
        System.out.println("Las paredes laterales ahora son " + this.colorParedesLaterales + ".");
    }
}
