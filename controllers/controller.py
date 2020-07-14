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
        result = self.firebaseService.getData(FirebaseUrls.pathListCategoryNode)

        if not result:
            return {'message': 'Error when getting list of categories'},400 #bad request
                 
        json = self.parseDictToJson(result)
        return {'message' : json},200







    #Faz o parser de um dicionario para json
    def parseDictToJson(self,dictionary):
        json_obj = json.dumps(dictionary)
        return json_obj

        

