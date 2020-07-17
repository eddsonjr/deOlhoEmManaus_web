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

    #Pega todas as categorias do banco de dados 
    def getAllCategories(self):
        result = self.firebaseService.getData(FirebaseUrls.pathListCategoryNode.value)

        if not result:
            return {'message': 'Error when getting list of categories'},400 #bad request
                 
        return {'message' : result},200




    #salva uma categoria especifica no banco de dados
    def postCategory(self,jsonRequest,child):
        categoryName = jsonRequest['categoryName']
        result = self.firebaseService.saveData(FirebaseUrls.pathListCategoryNode.value,categoryName,child)

        if not result:
            return {'message': 'Error when getting list of categories'},400 #bad request
        
        return {'message': 'category ' + str(categoryName) + ' added succefully'},200
        
    



    #remove uma categoria do banco de dados
    def deleteCategory(self,child):
        result = self.firebaseService.deleteData(FirebaseUrls.pathListCategoryNode.value + str(child))

        if not result:
            return {'message': 'Error when getting list of categories'},400 #bad request
        

        return {'message' : 'Category ' + child + ' deleted'}



        






