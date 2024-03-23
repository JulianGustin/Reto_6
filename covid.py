def contagios_totales(D: float, C: float) -> float: 
    total_contagios = C * (2 ** D)
    return total_contagios

if __name__ == "__main__":
    C = float(input("Ingrese el numero actual de contagiados en NuncaLandia: "))
    D = float(input("Ingrese el numero de días a partir de hoy: "))

    contagiados_total = contagios_totales(D, C)
    print("Despues de", D, "dias, el número total de contagiados en NuncaLandia sera:", contagiados_total)
