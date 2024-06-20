from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Configuración de la base de datos MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/tienda"
mongo = PyMongo(app)

# Ruta principal - Leer y mostrar los datos
@app.route('/')
def index():
    productos = mongo.db.productos.find()
    return render_template('index.html', productos=productos)

# Ruta para agregar un nuevo producto
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        precio = float(request.form.get('precio'))
        descripcion = request.form.get('descripcion')
        mongo.db.productos.insert_one({'nombre': nombre, 'precio': precio, 'descripcion': descripcion})
        return redirect(url_for('index'))
    return render_template('add.html')

# Ruta para editar un producto existente
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    producto = mongo.db.productos.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        precio = float(request.form.get('precio'))
        descripcion = request.form.get('descripcion')
        mongo.db.productos.update_one({'_id': ObjectId(id)}, {'$set': {'nombre': nombre, 'precio': precio, 'descripcion': descripcion}})
        return redirect(url_for('index'))
    return render_template('edit.html', producto=producto)

# Ruta para eliminar un producto
@app.route('/delete/<id>')
def delete(id):
    mongo.db.productos.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
