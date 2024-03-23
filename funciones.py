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