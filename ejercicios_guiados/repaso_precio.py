precio=float(input("introduce el precio del producto: "))
preciodesc=precio-precio*10/100
precioiva=preciodesc+preciodesc*21/100

print("precio con descuento son", preciodesc, "euros")
print("precio con IVA son", precioiva, "euros")

preciototal=precio*(1-10/100)*(1+21/100)
print("nuevo resultado", preciototal)
#print(f"el produto con precio {precio} tiene un descuento {preciodesc} y un total de {precioiva}")

print(round(preciototal,2))
print(f"precio total es {preciototal:.2f}")