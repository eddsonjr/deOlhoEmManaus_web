'''
    Esta arquivo contem classes responsaveis por realizar
    operacoes com o banco de dados do firebase


    Edson Jr
    Jul 2020

'''
import pyrebase
from firebase import firebase
from firebaseUrls import pathBase,pathListCategoryNode,pathListShowHouseNode,pathListShows


class FirebaseService:

    __TAG = '[FirebaseService]: '
    firebase = firebase.FirebaseApplication(pathBase,None)

    def getData(self,urlNode):
        data = None

        print(self.__TAG + 'Getting data from ' + urlNode + '\n\n')
        
        try:
            data = firebase.get(urlNode,'')
        except Exception:
            print(self.__TAG + 'Error: cannot get data')
        finally:
            return data
        
        






    def saveData(self):
        pass




    def deleteData(self):
        pass



    def updateData(self):
        pass








