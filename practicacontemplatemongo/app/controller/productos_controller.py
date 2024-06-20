from flask import jsonify, request, render_template, redirect, url_for
from bson.objectid import ObjectId
from app.models.producto import Producto

def agregar_producto(db):
    if request.method == 'POST':
        try:
            data = request.form
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
            return redirect(url_for('productos.obtener_productos_route'))

        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return render_template('productos/agregar_producto.html')

def obtener_productos(db):
    try:
        producto_model = Producto(db)
        productos = producto_model.obtener_productos()
        return render_template('productos/lista_productos.html', productos=productos)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def obtener_producto_por_id(db, producto_id):
    try:
        producto_model = Producto(db)
        producto = producto_model.obtener_producto_por_id(ObjectId(producto_id))
        if producto:
            return render_template('productos/detalle_producto.html', producto=producto)
        else:
            return jsonify({'error': 'Producto no encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def actualizar_producto(db, producto_id):
    if request.method == 'POST':
        try:
            data = request.form
            producto_model = Producto(db)
            resultado = producto_model.actualizar_producto(ObjectId(producto_id), data)

            if resultado.matched_count == 0:
                return jsonify({'error': 'Producto no encontrado'}), 404

            return redirect(url_for('productos.obtener_producto_por_id_route', producto_id=producto_id))

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    producto_model = Producto(db)
    producto = producto_model.obtener_producto_por_id(ObjectId(producto_id))
    return render_template('productos/editar_producto.html', producto=producto)

def eliminar_producto(db, producto_id):
    try:
        producto_model = Producto(db)
        resultado = producto_model.eliminar_producto(ObjectId(producto_id))

        if resultado.deleted_count == 0:
            return jsonify({'error': 'Producto no encontrado'}), 404

        return redirect(url_for('productos.obtener_productos_route'))

    except Exception as e:
        return jsonify({'error': str(e)}), 500
