from flask import Flask, render_template, request, redirect, url_for, flash
from dao.MarcasDao import MarcasDao 

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/inicio')
def inicio():
    return"hola mundo desde el backend"

@app.route('/contacto')
def contacto():
    return"<h3>Introduciendo HTML desde el servidor</h3>"

@app.route('/contacto2')
def contacto2():
    return render_template('contacto.html')

@app.route('/marcas-index')
def marcas_index():
    # Creacion de la instalacion de marcadao 
    marcasDao = MarcasDao()
    lista_marcas = marcasDao.getMarcas()
    return render_template('marcas-index.html', lista_marcas=lista_marcas)

@app.route('/marcas')
def marcas():
    return render_template('marcas.html')

@app.route('/guardar-marca', methods=['POST'])
def guardarMarcas():
    marcas = request.form.get('txtDescripcion').strip()
    if marcas == None or len(marcas) < 1:
        # mostrar un mensaje al usuario
        flash('Debe escribir algo en la descripcion', 'warning')

        # redireccionar a la vista 
        return redirect(url_for('marcas'))

    marcasdao = MarcasDao()
    marcasdao.guardarMarcas(marcas.upper())

    # mostrar un mensaje al usuario
    flash('Guardado exitoso', 'success')

    # redireccionar a la vista ciudades
    return redirect(url_for('marcas_index'))

@app.route('/marcas-editar/<id>')
def marcasEditar(id):
    marcasdao = MarcasDao()
    return render_template('marcas-editar.html', marca=marcasdao.getMarcasById(id))

@app.route('/actualizar-marcas', methods=['POST'])
def actualizarMarcas():
    id = request.form.get('txtIdMarcas')
    descripcion = request.form.get('txtDescripcion').strip()

    if descripcion == None or len(descripcion) == 0:
     flash('No debe estar vacia la descripcion')
     return redirect(url_for('marcasEditar', id=id))

    # actualizar
    marcasdao = MarcasDao()
    marcasdao.updateMarca(id, descripcion.upper())
    return redirect(url_for('marcas_index'))

@app.route('/guardar-mascota', methods=['POST'])
def guardarMascota():
    print(request.form)
    nombreMascota = request.form.get('txtNombreMascota')
    return f"Ya llego tu mascota <strong>{nombreMascota}</strong> al servidor"


@app.route('/marcas-eliminar/<id>')
def marcasEliminar(id):
    marcasdao = MarcasDao()
    marcasdao.deleteMarca(id)
    return redirect(url_for('marcas_index'))

#se pregunta por el proceso principal
if __name__=='__main__':
    app.run(debug=True)