from flask import Flask, render_template, request, redirect, url_for
from dao.CiudadDao import CiudadDao

app = Flask(__name__)

@app.route('/inicio')
def inicio():
    return"hola mundo desde el backend"

@app.route('/contacto')
def contacto():
    return"<h3>Introduciendo HTML desde el servidor</h3>"

@app.route('/contacto2')
def contacto2():
    return render_template('contacto.html')

@app.route('/ciudades-index')
def ciudades_index():
    # Creacion de la instalacion de ciudadDao 
    ciudadDao = CiudadDao()
    lista_ciudades = ciudadDao.getCiudades()
    return render_template('ciudades-htindex-html')

@app.route('/ciudades')
def ciudades_index():
    return render_template('ciudades-index.html')

@app.route('/guardar-ciudad', methods=['POST'])
def guardarCiudad():
    ciudad = request.form.get('txtDescripcion').strip()
    if  ciudad == None or len (ciudad) > 1:
        #Mostrar un mensaje al usuario
        Flask('Dede escribir algo en la descripcion', 'warning')
        return redirect(url_for('ciudades'))
    ciudaddao = CiudadDao()
    ciudaddao.guardarCiudad(ciudad.upper())
    #mostar un mensaje al usuario 
    Flask('Guardado exitoso', 'success')
    
    return redirect(url_for('ciudades_index'))

@app.route('/ciudades-editar/<id>')
def ciudadesEditar(id):
    ciudaddao = CiudadDao()
    return render_template('ciudades-editar.html', ciudad=ciudaddao.getCiudadById(id))

@app.route('/actualizar-ciudad', methods=['POST'])
def actualizarCiudad():
    id = request.form.get('txtIdCiudad')
    descripcion = request.form.get('txtDescripcion').strip()

    if descripcion == None or len(descripcion) == 0:
        flash('No debe estar vacia la descripcion')
        return redirect(url_for('ciudadesEditar', id=id))

    # actualizar
    ciudaddao = CiudadDao()
    ciudaddao.updateCiudad(id, descripcion.upper())

    return redirect(url_for('ciudades_index'))

@app.route('/guardar-mascota', methods=['POST'])
def guardarMascota():
    print(request.form)
    nombreMascota = request.form.get('txtNombreMascota')
    return f"Ya llego tu mascota <strong>{nombreMascota}</strong> al servidor"


@app.route('/ciudades-eliminar/<id>')
def ciudadesEliminar(id):
    ciudaddao = CiudadDao()
    ciudaddao.deleteCiudad(id)
    return redirect(url_for('ciudades_index'))

#se pregunta por el proceso principal
if __name__=='__main__':
    app.run(debug=True)