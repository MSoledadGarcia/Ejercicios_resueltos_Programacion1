# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca

#Ejercicio 1.11

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
pago_extra = 1000
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108


while saldo > 0:
    mes = mes +1
    if pago_extra_mes_comienzo >= mes and mes <= pago_extra_mes_fin:
        a_pagar = pago_mensual + pago_extra
    else:
        a_pagar = pago_mensual
    if saldo * (1+tasa/12) < a_pagar:
        a_pagar = saldo * (1+tasa/12)
    saldo = saldo * (1+tasa/12) - a_pagar
    total_pagado = total_pagado + a_pagar
    print(mes, round(total_pagado,2), round(saldo,2))
    
print('Total pagado', round(total_pagado, 2))
print("Meses requeridos", mes)