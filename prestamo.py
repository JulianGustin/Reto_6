def valor_prestamo(C:float, i:float, n:float) ->float: 
    valor = C * (1 + i)**n
    return valor

if __name__ == "__main__":
    
    C = float(input("Ingrese el monto del prestamo: "))
    i = float(input("Ingrese la tasa de interes anual (decimal) "))
    n = int(input("Ingrese el numero de meses: "))

    valor_final = valor_prestamo(C,i,n)

    print("El valor de su prestamo después de ", n, "meses será de ", valor_final)