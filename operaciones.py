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


    
