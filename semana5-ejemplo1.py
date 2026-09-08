from eii_utils import limpiar_consola, leer_entero, leer_booleano, leer_flotante


salario_bruto: float=0
salario_neto: float= 0
sem:float=0
ivm:float=0
bp:float=0
hijos: int=0
esta_casado: bool=True
impuestos:float=0

limpiar_consola()
salario_bruto= leer_flotante("Digite su salario")
esta_casado= leer_booleano("Esta casado")
hijos=leer_entero("Cantidad de hijos")

if salario_bruto <=918000:
    impuestos=0
elif salario_bruto<=1347000:
    impuestos= (salario_bruto - 918000)*0.1
elif salario_bruto<=  2364000:
    impuestos=42900 + 354450+ (salario_bruto-2364000)*0.2
else:
    impuestos= 42900+354450+472600+(salario_bruto-4727000)*0.25


salario_neto= salario_bruto- impuestos
bp= salario_bruto*0.01
sem=salario_bruto*0.055
ivm= salario_bruto*0.433