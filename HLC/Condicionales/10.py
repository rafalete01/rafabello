# 10. Algoritmo que pide una nota numérica, se asegura que está entre 0 y 10 y muestra la calificación que le corresponde.
# -----------------------------------------------------------------------------------------------------------------------
nota = float(input("Introduce una nota entre 0 y 10: "))
if nota < 0 or nota > 10:
    print("La nota no es válida. Debe estar entre 0 y 10.")  # Validación de rango de la nota
else:
    # Determina la calificación según la nota numérica
    if nota < 5:
        calificacion = "IN"  # Insuficiente
    elif nota < 6:
        calificacion = "SF"  # Suficiente
    elif nota < 7:
        calificacion = "BI"  # Bien
    elif nota < 9:
        calificacion = "NT"  # Notable
    else:
        calificacion = "SB"  # Sobresaliente
    print(f"La calificación es: {calificacion}")