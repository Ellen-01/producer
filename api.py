from flask import Flask, jsonify, request
import sqlite3

app = Flask(_name_)

# Ruta para obtener todos los datos meteorológicos
@app.route('/datos', methods=['GET'])
def obtener_datos():
    conexion = sqlite3.connect('datos_meteorologicos.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM mediciones")
    datos = cursor.fetchall()
    conexion.close()

    resultado = []
    for fila in datos:
        resultado.append({
            "id": fila[0],
            "temperatura": fila[1],
            "humedad": fila[2],
            "presion": fila[3],
            "fecha": fila[4]
        })
    return jsonify(resultado)

# Ruta para filtrar por temperatura mínima
@app.route('/datos/temperatura', methods=['GET'])
def filtrar_por_temperatura():
    min_temp = float(request.args.get('min', 0))
    conexion = sqlite3.connect('datos_meteorologicos.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM mediciones WHERE temperatura >= ?", (min_temp,))
    datos = cursor.fetchall()
    conexion.close()

    resultado = []
    for fila in datos:
        resultado.append({
            "id": fila[0],
            "temperatura": fila[1],
            "humedad": fila[2],
            "presion": fila[3],
            "fecha": fila[4]
        })
    return jsonify(resultado)

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)