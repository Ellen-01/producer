from flask import Flask, jsonify, request
from alerts import verificar_alerta
import psycopg2
import os

app = Flask(__name__)

# Configuración de conexión a la base de datos
DB_HOST = os.getenv("DATABASE_HOST", "postgres")  # Cambiado a localhost
DB_PORT = int(os.getenv("DATABASE_PORT", 5432))
DB_USER = os.getenv("DATABASE_USER", "postgres")   # Usuario por defecto de PostgreSQL
DB_PASSWORD = os.getenv("DATABASE_PASSWORD", "1234")
DB_NAME = os.getenv("DATABASE_NAME", "weather_db")

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "API funcionando correctamente"})

@app.route('/logs', methods=['GET'])
def get_logs():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            dbname=DB_NAME
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 10;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/alerta', methods=['POST'])
def alerta():
    data = request.get_json()
    estacion_id = data.get('estacion_id', 0)  
    temperatura = data.get('temperatura')
    humedad = data.get('humedad')

    verificar_alerta(estacion_id, temperatura, humedad)  
    return jsonify({"mensaje": "Alerta generada correctamente"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
