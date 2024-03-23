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
