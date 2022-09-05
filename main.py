from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)


@app.route("/concentracion", methods=["POST"])
def concentracion():
  caudal = request.json['caudal']
  tiempoBacheo = request.json['tiempoBacheo']
  volumenBiocida = request.json['volumenBiocida']

  nuevoCaudal = caudal/24
  print(nuevoCaudal)
  caudalBacheo = nuevoCaudal * tiempoBacheo
  print(caudalBacheo)
  nuevoVolumenBiocida = volumenBiocida / 42
  print(nuevoVolumenBiocida)
  caudalTotal = caudalBacheo + nuevoVolumenBiocida
  print(caudalTotal)
  concentracionBiocida = 1000000 * 0.9143 / caudalTotal
  print(concentracionBiocida)

  response = jsonify(resultado=concentracionBiocida)
  response.headers.add("Access-Control-Allow-Origin", "*")
  return response

@app.route('/public/<path>')
def send_report(path):
    return send_from_directory('public', path)