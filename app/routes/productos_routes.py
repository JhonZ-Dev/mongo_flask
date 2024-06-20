from flask import Blueprint, current_app
from app.controller.productos_controller import (
    agregar_producto, obtener_productos, obtener_producto_por_id, actualizar_producto, eliminar_producto
)

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/', methods=['POST'])
def agregar_producto_route():
    return agregar_producto(current_app.db)

@productos_bp.route('/', methods=['GET'])
def obtener_productos_route():
    return obtener_productos(current_app.db)

@productos_bp.route('/<producto_id>', methods=['GET'])
def obtener_producto_por_id_route(producto_id):
    return obtener_producto_por_id(current_app.db, producto_id)

@productos_bp.route('/<producto_id>', methods=['PUT'])
def actualizar_producto_route(producto_id):
    return actualizar_producto(current_app.db, producto_id)

@productos_bp.route('/<producto_id>', methods=['DELETE'])
def eliminar_producto_route(producto_id):
    return eliminar_producto(current_app.db, producto_id)
