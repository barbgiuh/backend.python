from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/data', methods=['POST'])
def create_data():
    data = request.get_json()
    # lógica para inserir dados no banco de dados
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)
