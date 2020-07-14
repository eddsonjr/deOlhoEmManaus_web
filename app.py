'''
    Arquivo de inicio da API para o aplicativo 'DeOlhoEmManaus'

    Edson Jr
    Jul 2020

'''
from flask import Flask,jsonify, request

# Mark: Configuracoes do flask
app = Flask(__name__)


#Mark: Rotas

@app.route('/categories/getAll',methods=['GET'])
def getAllCategories():
    print('Gettin all categories')












#Mark: main
if __name__ == '__main__':
    app.run(debug=True)