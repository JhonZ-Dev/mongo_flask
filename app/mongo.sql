test> use tienda
switched to db tienda
tienda> db.createCollection("productos")
{ ok: 1 }
tienda> db.productos.insertOne({nombre:"Coca Cola", precio:0.50, descripcion:"CocaCola"})
{
  acknowledged: true,
  insertedId: ObjectId('66739638ca7f7279fb9f990a')
}
tienda> db.producto.find()

tienda> db.productos.find()
[
  {
    _id: ObjectId('66739638ca7f7279fb9f990a'),
    nombre: 'Coca Cola',
    precio: 0.5,
    descripcion: 'CocaCola'
  }
]