# Reto 6 

## Lista de contenidos 
1. [Figura de esfera y cono](#figura-1)
2. [Figura de rectángulo y circulos](#figura-2)
3. [Carne de aves](#carne)
4. [Compras de mamá](#compras)
5. [Prestamo](#prestamo)
6. [Covid en NuncaLandia](#covid)
7. [Operaciones con 5 números](#operaciones)
8. [Funciones para operaciones](#funciones)
9. [Consulta sobre pip](#que-es-pip)
10. [Modulos populares pip](#modulos)

***
## Figura 1 
![imagen](https://camo.githubusercontent.com/100b4565370665cb6dc8eeb57a662a10739043ee88c469412805f701539f370b/68747470733a2f2f692e706f7374696d672e63632f465276436d7078782f696d6167652e706e67)

```python
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
```
***
## Figura 2
![figura2](https://camo.githubusercontent.com/1a56c739fc45f64bd5f731f69f70c88c2bdd59840ffe6ad12c41082d76393952/68747470733a2f2f692e706f7374696d672e63632f3174344d727a734c2f696d6167652e706e67)
```python
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
```
***
## Carne
```python
def peso_aves(n:float, m:float, k:float ) -> float: 
    pesoN = n*6
    pesoM = m*7 
    pesoK = k*1
    pesoTotal = pesoN + pesoM + pesoK 
    return pesoTotal 

if __name__ == "__main__":
    n = float(input("Ingrese el número de gallinas: "))
    m = float(input("Ingrese el número de gallos: "))
    k = float(input("Ingrese el número de pollitos: "))

    cantidadCarne = peso_aves(n,m,k)
    print("La cantidad de carne en kilos es:", cantidadCarne)

```
***
## Compras 
```python
def precio_compra(p:float, m:float, h:float ) -> float: 
    precioP = p*300
    precioM = m*3300 
    precioH = h*350
    precioTotal = precioP + precioM + precioH
    return precioTotal 

if __name__ == "__main__": 
    p = float(input("Ingrese el numero de panes a comprar: "))
    m = float(input("Ingrese el numero de bolsas de leche a comprar: "))
    h = float(input("Ingrese el numero de huevos a comprar: "))
    B = float(input("Ingrese cuánta plata le da su mamá: "))

    precio = precio_compra(p,m,h)

    resultado = B - precio
    if resultado < 0:
        print("Quedó debiendo ", (resultado*-1), "pesos")
    elif resultado > 0:
        print("Le sobraron ", resultado, "pesos")
    else:
        print("Issss, exactico.")
```
***
## Prestamo
```python
def valor_prestamo(C:float, i:float, n:float) ->float: 
    valor = C * (1 + i)**n
    return valor

if __name__ == "__main__":
    
    C = float(input("Ingrese el monto del prestamo: "))
    i = float(input("Ingrese la tasa de interes anual (decimal) "))
    n = int(input("Ingrese el numero de meses: "))

    valor_final = valor_prestamo(C,i,n)

    print("El valor de su prestamo después de ", n, "meses será de ", valor_final)
```
***
## Covid
```python
def contagios_totales(D: float, C: float) -> float: 
    total_contagios = C * (2 ** D)
    return total_contagios

if __name__ == "__main__":
    C = float(input("Ingrese el numero actual de contagiados en NuncaLandia: "))
    D = float(input("Ingrese el numero de días a partir de hoy: "))

    contagiados_total = contagios_totales(D, C)
    print("Despues de", D, "dias, el número total de contagiados en NuncaLandia sera:", contagiados_total)
```
***
## Operaciones
```python
import funciones

if __name__ == "__main__": 
    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))
    n3 = float(input("Ingrese el tercer número: "))
    n4 = float(input("Ingrese el cuarto número: "))
    n5 = float(input("Ingrese el quinto número: "))
    print("Sus números son: ",n1,n2,n3,n4,n5)

    n1, n2, n3, n4, n5 = funciones.ordernar(n1,n2,n3,n4,n5)

    promedioNumeros = funciones.promedio(n1,n2,n3,n4,n5)
    
    medianaNumeros = funciones.mediana(n1,n2,n3,n4,n5)

    promedioMultiNumeros = funciones.promedio_multiplicativo(n1,n2,n3,n4,n5)

    ascendenteNumeros = funciones.ascendente(n1,n2,n3,n4,n5)

    descendenteNumeros = funciones.descendente(n1,n2,n3,n4,n5)

    potenciaNumeros = funciones.potencia(n1,n2,n3,n4,n5)

    raizNumeros = funciones.raiz(n1,n2,n3,n4,n5) 

    print("El promedio de los números es: ", promedioNumeros)
    print("La mediana de los números es: ", medianaNumeros)
    print("El promedio multiplicativo de los números es: ", promedioMultiNumeros)
    print("El orden ascendente de los números es: ", ascendenteNumeros)
    print("El orden descendente de los números es: ", descendenteNumeros)
    print("La potencia del mayor elevado al menor es ", potenciaNumeros)
    print("La raiz cubica del menor es ", raizNumeros)


```
***
## Funciones
```python
def ordernar(n1:float, n2:float, n3:float, n4:float, n5:float) ->float:
    if n1 > n2:
        n1, n2 = n2, n1
    if n1 > n3:
        n1, n3 = n3, n1
    if n1 > n4:
        n1, n4 = n4, n1
    if n1 > n5:
        n1, n5 = n5, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n2 > n4:
        n2, n4 = n4, n2
    if n2 > n5:
        n2, n5 = n5, n2
    if n3 > n4:
        n3, n4 = n4, n3
    if n3 > n5:
        n3, n5 = n5, n3
    if n4 > n5:
        n4, n5 = n5, n4
    
    return n1, n2, n3, n4, n5

def promedio(n1:float, n2:float, n3:float, n4:float, n5:float) ->float:
    promedio = (n1+n2+n3+n4+n5)/5
    return promedio

def mediana(n1:float, n2:float, n3:float, n4:float, n5:float) ->float:
    mediana = n3
    return mediana 

def promedio_multiplicativo(n1:float, n2:float, n3:float, n4:float, n5:float) ->float:
    multi : float = n1*n2*n3*n4*n5
    promedioMulti = multi**(1/5)
    return promedioMulti

def ascendente(n1:float, n2:float, n3:float, n4:float, n5:float) ->float:
    ascendente = n1,n2,n3,n4,n5
    return ascendente

def descendente(n1:float, n2:float, n3:float, n4:float, n5:float) ->float:
    descendente = n5,n4,n3,n2,n1
    return descendente

def potencia(n1:float, n2:float, n3:float, n4:float, n5:float) ->float:
    mayor : float = n5
    menor : float = n1 
    potencia = mayor**menor
    return potencia

def raiz(n1:float, n2:float, n3:float, n4:float, n5:float) ->float:
    raiz = n1**(1/3)
    return raiz
```
***

## Que es pip

Pip es una herramienta fundamental para manejar paquetes de software en Python. Se emplea para instalar y gestionar una variedad de módulos que pueden ser incorporados en tus programas. Estos módulos ofrecen una amplia gama de funcionalidades, como cálculos matemáticos, acceso a bases de datos, análisis de datos, etc. 

***
## Modulos

Primero que todo, para instalar modulos pip, debes abrir la terminal o simbolo del sistema de tu computador e ingresar el comando "pip install" seguido del módulo que desees instalar.  
Ej: numpy: pip install numpy
Ahora, este es un listado de modulos populares de pip
1. numpy
2. pandas
3. matplotlib
4. scikit-learn
5. keras
6. tensorflow
7. beautifulsoup4
8. flask
9. django
10. pygame
