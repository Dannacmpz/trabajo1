from eii_utils import leer_booleano, leer_entero, limpiar_consola

#leccion 03 ejercicio 1.7
# declaracion de variables
ingresos:int=0
deudas:int=0
historial_limpio:bool=True
resultado:bool=True
#inputs
limpiar_consola()
ingresos = leer_entero('Digite los ingresos: ')
deudas = leer_entero('Digite las deudas: ')
historial_limpio = leer_booleano('Tiene el historial limpio')
#process
resultado = ingresos >= 600000 and deudas < 200000 and historial_limpio
#output
print(resultado)



#leccion03 ejercicio 2.1
from eii_utils import limpiar_consola, leer_booleano, leer_entero, leer_flotante

nota:float=0
ingresos:int=0
zona_riesgo:bool=True
resultado:bool=True

limpiar_consola()
nota = leer_flotante("Digite su nota: ")
ingresos = leer_entero("Digite los ingresos familiares: ")
zona_riesgo = leer_booleano("Usted vive en zona de riesgo: ")

resultado = nota >= 90 and (ingresos < 400000 or zona_riesgo)

print(resultado)


#leccion04 nivel 2 ejericio 1.4

from eii_utils import leer_booleano, limpiar_consola
# variables
costo:int =  400000
extra_ram:bool = True
extra_ssd:bool = True
extra_garantia:bool = True

#inputs
limpiar_consola()
extra_ram = leer_booleano("Desea RAM adicional")
extra_ssd = leer_booleano("Desea un SSD adicional")
extra_garantia = leer_booleano("Desea garantia adicional")

#process
if extra_ram:
    costo = costo + 35000

if extra_ssd:
    costo = costo + 45000

if extra_garantia:
    costo = costo + 25000

print(f"El costo final es {costo} colones")