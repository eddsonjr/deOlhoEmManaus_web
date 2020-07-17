'''
    Arquivo de inicio da API para o aplicativo 'DeOlhoEmManaus'

    Edson Jr
    Jul 2020


    Pesquisas:
        https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask

'''
from flask import Flask,jsonify, request
from controllers.controller import Controller

# Mark: Configuracoes do flask
app = Flask(__name__)


#Mark: Rotas

@app.route('/categories/getAll',methods=['GET'])
def getAllCategories():
    controller = Controller()
    result = controller.retrieveAllCategories()
    return result





@app.route('/categories/<childID>',methods=['POST','PUT','DELETE'])
def categories(childID):

    controller = Controller()
    content = request.json #recebe um json do contexto
    result = None

    if request.method == 'POST':
        result = controller.saveCategory(content,childID)

    
    elif request.method == 'DELETE':
        result = controller.deleteCategory(childID)




   
    return result















#Mark: main
if __name__ == '__main__':
    app.run(debug=True)