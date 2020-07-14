'''
    Este arquivo contem uma classe de resources 
    referentes as categorias. 

    Edson Jr
    jul 2020
'''
from flask_restful import Resource, Api, reqparse
from .firebaseServices.firebaseService import FirebaseService


class CategoriesService(Resource):

    firebaseDB = FirebaseService()


    def get(self,nodeUlrID):
        pass 


    
    def post(self,nodeUlrID):
        pass



    def put(self,nodeUlrID):
        pass




    def delete(self,nodeUlrID):
        pass
