# declarar variables
monto: float = 0
impuesto: float = 0
total: float = 0

monto = float (input("Digite el monto del producto"))

impuesto = monto * 0.13
total= monto + impuesto

print("Monto: ", monto)
print("IVA: ", impuesto)