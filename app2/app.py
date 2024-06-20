from flask import Flask, request, jsonify
from pymongo import MongoClient, errors

app = Flask(__name__)

# Configuración de la conexión a MongoDB
try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['tienda']
    productos_collection = db['productos']
    print("Conexión a la base de datos MongoDB exitosa")
except errors.ConnectionError as e:
    print(f"Error al conectar a MongoDB: {e}")

@app.route('/productos', methods=['POST'])
def agregar_producto():
    try:
        data = request.get_json()
        nombre = data.get('nombre')
        precio = data.get('precio')
        descripcion = data.get('descripcion')

        if not nombre or not precio:
            return jsonify({'error': 'Nombre y precio son campos obligatorios'}), 400

        producto = {
            'nombre': nombre,
            'precio': precio,
            'descripcion': descripcion
        }

        productos_collection.insert_one(producto)
        return jsonify({'mensaje': 'Producto agregado correctamente'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
