'''
    Este arquivo contem a classe de controler, 
    responsavel por fazer a interacao entre a camada
    de view (no caso a camada que vai receber as requisicoes)
    com as camadas de model e service


    Edson Jr
    Jul 2020
'''
from services.firebaseServices.firebaseService import FirebaseService
from services.firebaseServices.firebaseUrls import FirebaseUrls
import json



class Controller:

    firebaseService = FirebaseService()
    __TAG = '[Controller]: '

    def retrieveAllCategoriesFromDB(self):
        result = self.firebaseService.getData(FirebaseUrls.pathListCategoryNode.value)

        if not result:
            return {'message': 'Error when getting list of categories'},400 #bad request
                 
        return {'message' : result},200




    def saveData(self,jsonRequest):
        dictionary = self.parseDictToJson(jsonRequest)
        print(dictionary)
        





    

    #Recebe como parametro um json e retorna um dicionario
    def parserJsonToDict(self,jsonRequest):
	    json_to_string = json.dumps(jsonRequest)
	    json_dict = json.loads(json_to_string)
	    return json_dict




    #Faz o parser de um dicionario para json
    def parseDictToJson(self,dictionary):
        json_obj = json.dumps(dictionary)
        return json_obj

        

