'''
    Arquivo de inicio da API para o aplicativo 'DeOlhoEmManaus'

    Edson Jr
    Jul 2020

'''
from flask import Flask,jsonify, request
from controllers.controller import Controller

# Mark: Configuracoes do flask
app = Flask(__name__)


#Mark: Rotas

@app.route('/categories/getAll',methods=['GET'])
def getAllCategories():
    controller = Controller()
    result = controller.retrieveAllCategoriesFromDB()
    return result


@app.route('/categories/<nodeUrlID>',methods=['POST','PUT','DELETE'])
def categories(nodeUrlID):
    nodeUrlID = nodeUrlID
    return {'message: ' : str(nodeUrlID)}















#Mark: main
if __name__ == '__main__':
    app.run(debug=True)