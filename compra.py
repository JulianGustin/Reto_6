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