total_clientes = int(input("¿Cuántos clientes hubo hoy?: "))

for i in range(total_clientes):
    compra = float(input("\nTotal de la compra: "))
    color = input("Color de la bolita (roja, amarilla, blanca): ")

    if color == "roja":
        descuento = compra * 0.40
    elif color == "amarilla":
        descuento = compra * 0.25
    else:
        descuento = 0

    total_pagar = compra - descuento

    print("Descuento:", descuento)
    print("Total a pagar:", total_pagar)