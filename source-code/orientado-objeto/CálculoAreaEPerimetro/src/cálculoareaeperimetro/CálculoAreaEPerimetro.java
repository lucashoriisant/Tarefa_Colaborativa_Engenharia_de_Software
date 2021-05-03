package cálculoareaeperimetro;
public class CálculoAreaEPerimetro {
    public static void main(String[] args) {
        Circulo c1 = new Circulo(false, true,4,3.14f);
        
        c1.calcularArea();
        c1.estadoAtual();
       
        Retangulo r1 = new Retangulo(false, true, 5, 2);
        
        r1.calcularArea();
        r1.estadoAtual();   
    }  
}
