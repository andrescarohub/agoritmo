def solicitar_datos():
    """Solicita los datos necesarios para calcular el valor a pagar."""
    mes = input("Ingresa el mes de consumo: ")
    valor_kw = float(input("Ingresa el valor del kW: "))
    total_kw_consumido = float(input("Ingresa el total de kW consumidos en el mes: "))
    estrato = int(input("Ingresa el estrato (1-6): "))
    
    return mes, valor_kw, total_kw_consumido, estrato

def calcular_total_a_pagar(valor_kw, total_kw_consumido, estrato):
    """Calcula el total a pagar por el consumo de energía eléctrica."""
    total_sin_descuento = valor_kw * total_kw_consumido

    if estrato == 1:
        total_final = total_sin_descuento * 0.8  # 20% descuento
    elif estrato == 2:
        total_final = total_sin_descuento * 0.9  # 10% descuento
