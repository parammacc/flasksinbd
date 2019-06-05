from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def holamundo():
    return 'HOLA MUNDO'

MMUsuarios = [
    {
        'id': 1,
        'nombre': 'amparo',
        'edad': '33'
    },
    {
        'id': 2,
        'nombre': 'wanolo',
        'edad': '25'
    },
    {
        'id': 3,
        'nombre': 'pozi',
        'edad': '55'
    },
    
]
'''
getUsuarios()
obtiene los usuarios
devuelve un json con los usuarios
'''
@app.route('/Usuarios/', methods=['GET'])
def getUsuarios():
    return jsonify({'usuarios':MMUsuarios})

'''
addUsuario()
inserta un usuario

'''

@app.route('/Cabeza/', methods=['POST'])
def addUsuario():
    usuario = {
        'id':MMUsuarios[-1]['id'] + 1,
        'nombre':request.json['nombre'],
        'edad':request.json.get('edad','27')
    }
    MMUsuarios.append(usuario)
    return jsonify({'usuario':usuario}), 201

@app.route('/ejemploPUT/<id>', methods=['PUT'])
def actualiza(id):
    
    #MMUsuarios(int(id)).nombre=request.json['nombre']
    #return jsonify({'usuario':MMUsuarios[int(id)]}) 
#    MMUsuarios[id].nombre=request.json['nombre']
    
    num=int(id)
    MMUsuarios[num]=num+1
    MMUsuarios[num]=request.json['nombre']
    MMUsuarios[num]=request.json['edad']
    return jsonify({'usuarios':MMUsuarios})

#    auxUsuario.nombre=request.json['nombre']
#    return jsonify({'usuario':MMUsuarios[int(id)]})
    #auxUsuario = MMUsuarios[int(id)]
    #return jsonify({'usuario':auxUsuario['nombre']}) 
    #return jsonify({'usuario':request.json['nombre']})
    '''
    {
        "usuario": "RICARDO"
    }
    '''

@app.route("/borrar/<id>", methods=['DELETE'])
def eliminar(id):
    id = int(id)
    #MMUsuarios.remove(id)
    del MMUsuarios[id]
    return jsonify({'usuarios':MMUsuarios}) 
    

@app.route("/json", methods=["POST"])
def json_example():

    req = request.get_json()

    print(req)

    return "Thanks!", 200

'''
@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def main():
    return "Done sir!"
'''

@app.route('/obtener/', methods=['GET'])
def mmobtener():
    return "método obtener"

@app.route('/anadir/', methods=['POST'])
def mmanadir():
    return "método añadir"

@app.route('/modificar/', methods=['PUT'])
def mmmodificar():
    return "método modificar"

@app.route('/eliminar/', methods=['DELETE'])
def mmeliminar():
    return "método eliminar"

if __name__ == '__main__':
    app.run(debug=True, port=10000)