package cálculoareaeperimetro;
public class Retangulo {    
    
    private boolean statusPerimetro;
    private boolean statusArea;
    private float base;
    private float altura;
    private float perimetro;
    private float area;

    public void estadoAtual(){
        System.out.println("Base : " + this.getBase());
        System.out.println("Altura: " + this.getAltura());
        System.out.println("Perímetro do retângulo: "+ this.getPerimetro());
        System.out.println("Área do retângulo: " + this.getArea());
    }
    
    public Retangulo(boolean statusPerimetro, boolean statusArea, float base, float altura) {
        this.statusPerimetro = statusPerimetro;
        this.statusArea = statusArea;
        this.base = base;
        this.altura = altura;
    }

    public float getPerimetro() {
        return perimetro;
    }

    public void setPerimetro(float perimetro) {
        this.perimetro = perimetro;
    }

    public float getArea() {
        return area;
    }

    public void setArea(float area) {
        this.area = area;
    }
    

    public boolean getStatusPerimetro() {
        return statusPerimetro;
    }

    public void setStatusPerimetro(boolean statusPerimetro) {
        this.statusPerimetro = statusPerimetro;
    }

    public boolean getStatusArea() {
        return statusArea;
    }

    public void setStatusArea(boolean statusArea) {
        this.statusArea = statusArea;
    }

    public float getBase() {
        return base;
    }

    public void setBase(float base) {
        this.base = base;
    }

    public float getAltura() {
        return altura;
    }

    public void setAltura(float altura) {
        this.altura = altura;
    }
    
    public float perimetro(){
      if (this.getStatusPerimetro() == true) {
          
      } 
       return 0;
    }
    
    public void calcularPerimetro(){
        this.setPerimetro((this.getAltura()* 2) +  getBase() * 2);   
    }
    
    public float area(){
        if (this.getStatusArea() == true){
            
        }
        return 0;
    }
    
    public void calcularArea(){
        this.setArea(this.getAltura() * getBase());
    }
}

