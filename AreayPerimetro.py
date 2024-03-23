from math import pi

def area (r:float, a:float, b:float, pi:float) ->float: 
    areaRectangulo = (b * a)
    areaCirculos = (pi * r**2)*2
    areaTotal = (areaRectangulo + areaCirculos)
    return areaTotal

def perimetro (r:float, a:float, b:float, pi:float) ->float: 
    perimetroRectangulo = (b*2)+(a*2)
    perimetroCirculo = (2*pi*r)
    perimetroTotal = perimetroRectangulo + perimetroCirculo
    return perimetroTotal 

if __name__ == "__main__": 
    r = (float(input("Ingrese el radio de los circulos: ")))
    b = (float(input("Ingrese un lado del rectangulo: ")))
    a = (float(input("Ingrese el otro lado del rectangulo: ")))
    areaFigura = area(r,a,b,pi)
    perimetroFigura = perimetro(r,a,b,pi)

    print("El area de la figura es de ", areaFigura, "cm²")
    print("El perimetro de la figura es de ", perimetroFigura, "cm")