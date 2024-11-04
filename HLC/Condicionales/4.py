 #4. Algoritmo que solicita el dato Ingresos y el dato Gastos y dice si ha habido beneficio o pérdida.
# ---------------------------------------------------------------------------------------------------
ingresos = float(input("Introduce los ingresos: "))
gastos = float(input("Introduce los gastos: "))
if ingresos > gastos:
    print("Ha habido beneficio.")  # Beneficio si los ingresos superan a los gastos
elif ingresos < gastos:
    print("Ha habido pérdida.")  # Pérdida si los gastos superan a los ingresos
else:
    print("No ha habido ni beneficio ni pérdida, el resultado es neutro.")  # Caso neutro