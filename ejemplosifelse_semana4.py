from eii_utils import leer_entero, imprimir_titulo_decorado, limpiar_consola

#variables
limpiar_consola()
horas_trabajadas:int=0
tarifa_hora: int=0
salario:int=0

#inputs
horas_trabajadas=leer_entero("digite la cantidad de horas trabajadas: ")
tarifa_hora=leer_entero("digite la tarifa por hora: ")

#process
if horas_trabajadas<=40:
    salario=horas_trabajadas*tarifa_hora
else:
    salario=(((horas_trabajadas-40)*tarifa_hora*1.5)+ 40*tarifa_hora)

#salidas
imprimir_titulo_decorado("SALARIO MENSUAL",20)
print(f"su salario es de {salario} colones en total")