class Producto:
    def __init__(self, db):
        self.collection = db['productos']

    def agregar_producto(self, producto):
        return self.collection.insert_one(producto)

    def obtener_productos(self):
        return list(self.collection.find({}))

    def obtener_producto_por_id(self, producto_id):
        return self.collection.find_one({'_id': producto_id})

    def actualizar_producto(self, producto_id, datos_actualizados):
        return self.collection.update_one({'_id': producto_id}, {'$set': datos_actualizados})

    def eliminar_producto(self, producto_id):
        return self.collection.delete_one({'_id': producto_id})
