from math import pi
def volumen(r1:float, r2:float, h:float, pi:float ) -> float :
    volumenEsfera = (4/3 * pi * r1**3)
    volumenCono = (1/3 * pi * r2**2 * h)
    volumenTotal = volumenEsfera + volumenCono 
    return volumenTotal

def area(r1:float, r2:float, h:float, pi:float ) -> float :
    areaEsfera = (4 * pi * r1**2 )
    generatriz = (h**2 + r2**2)**0.5
    areaCono = (pi * generatriz * r2) + (pi * r2**2)
    areaTotal = areaEsfera + areaCono
    return areaTotal


if __name__ == "__main__": 
    
    r1 = float(input("Ingrese el radio de la esfera: "))
    r2 = float(input("Ingrese el radio de la base del cono: "))
    h = float(input("Ingrese la altura del cono: "))

    volumenFigura = volumen(r1, r2, h, pi)
    areaFigura = area(r1, r2, h, pi)

    print("El area superficial de la figura es de ", areaFigura, "cm²")
    print("El volumen total de la figura es de ", volumenFigura, "cm³")
