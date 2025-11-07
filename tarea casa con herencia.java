public class Floristeria extends Casa {
    private String paredDelantera;
    private String paredTrasera;
    private String paredesLaterales;

    public Floristeria(int numero_habitaciones, int numero_plantas, boolean tiene_terraza) {
        super("varios colores", numero_habitaciones, numero_plantas, false, tiene_terraza);
        this.paredDelantera = "blanca con puntos azules";
        this.paredTrasera = "verde";
        this.paredesLaterales = "blancas con rayas azules";
    }

    public String descripcion() {
        String descripcion = "Esta floristería tiene " + this.numero_habitaciones + " habitaciones y " +
                this.numero_plantas + " plantas.\n";
        descripcion += "La pared delantera es " + this.paredDelantera +
                ", la pared trasera es de color " + this.paredTrasera +
                " y las paredes laterales son " + this.paredesLaterales + ".\n";
        descripcion += "No tiene jardín, pero está decorada con flores naturales.";
        if (this.tiene_terraza) {
            descripcion += " Y cuenta con una terraza ideal para las plantas.";
        }
        return descripcion;
    }
}
