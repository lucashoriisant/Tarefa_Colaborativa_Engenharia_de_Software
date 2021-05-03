package cálculoareaeperimetro;
import java.lang.Math;
public class Circulo {
    private boolean statusPerimetro;
    private boolean statusArea;
    private float perimetro;
    private float area;
    private float pi;
    private float raio;
    
  
    public void estadoAtual(){
        System.out.println("Raio : " + this.getRaio());
        System.out.println("Pi: " + this.getPi());
        System.out.println("Circunferência do círculo: "+ this.getPerimetro());
        System.out.println("Área do círculo: " + this.getArea());
    }
    
    public Circulo(boolean statusPerimetro, boolean statusArea, float raio, float pi) {
        this.statusPerimetro = statusPerimetro;
        this.statusArea = statusArea;
        this.raio = raio;
        this.pi = pi;
    }
    
    public float getPerimetro() {
        return perimetro;
    }

    public void setPerimetro(float perimetro) {
        this.perimetro = perimetro;
    }

    public float getRaio() {
        return raio;
    }

    public void setRaio(float raio) {
        this.raio = raio;
    }
    
    public boolean getstatusPerimetro() {
        return statusPerimetro;
    }

    public void setPerimetro(boolean statusPerimetro) {
        this.perimetro = perimetro;
    }
    
    public boolean getStatusArea() {
        return statusArea;
    }

    public void setStatusArea(boolean statusArea) {
        this.statusArea = statusArea;
    }

    public float getArea() {
        return area;
    }

    public void setArea(float area) {
        this.area = area;
    }

    public float getPi() {
        return pi;
    }

    public void setPi(float pi) {
        this.pi = pi;
    }
    
    
    public void calcularPerimetro(){
        this.setPerimetro(this.getRaio()* 2 * getPi());
    }
    
    public float circunferencia(){
        if (this.getstatusPerimetro() == true){
            
        }
        return 0;
    }  
    public void calcularArea(){
        this.setArea(getRaio() * getRaio() * getPi());
    }
    
    public void area(){
        if (this.getStatusArea() == true){
            
        }
    }
}
