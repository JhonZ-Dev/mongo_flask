from flask import jsonify, request
from bson.objectid import ObjectId
from app.models.producto import Producto

def agregar_producto(db):
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

        producto_model = Producto(db)
        producto_model.agregar_producto(producto)
        return jsonify({'mensaje': 'Producto agregado correctamente'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def obtener_productos(db):
    try:
        producto_model = Producto(db)
        productos = producto_model.obtener_productos()
        return jsonify(productos), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def obtener_producto_por_id(db, producto_id):
    try:
        producto_model = Producto(db)
        producto = producto_model.obtener_producto_por_id(ObjectId(producto_id))
        if producto:
            return jsonify(producto), 200
        else:
            return jsonify({'error': 'Producto no encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def actualizar_producto(db, producto_id):
    try:
        data = request.get_json()
        producto_model = Producto(db)
        resultado = producto_model.actualizar_producto(ObjectId(producto_id), data)

        if resultado.matched_count == 0:
            return jsonify({'error': 'Producto no encontrado'}), 404

        return jsonify({'mensaje': 'Producto actualizado correctamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def eliminar_producto(db, producto_id):
    try:
        producto_model = Producto(db)
        resultado = producto_model.eliminar_producto(ObjectId(producto_id))

        if resultado.deleted_count == 0:
            return jsonify({'error': 'Producto no encontrado'}), 404

        return jsonify({'mensaje': 'Producto eliminado correctamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
