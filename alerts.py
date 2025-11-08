# servicios de alertas por umbrales
def generar_alerta(estacion_id, temperatura, humedad):
    if temperatura > 40:
        print(f"[ALERTA ] Estación {estacion_id}: Temperatura crítica ({temperatura}°C)")
    elif humedad < 20:
        print(f"[ALERTA ] Estación {estacion_id}: Humedad muy baja ({humedad}%)")
    elif temperatura < 0:
        print(f"[ALERTA ] Estación {estacion_id}: Temperatura bajo cero ({temperatura}°C)")