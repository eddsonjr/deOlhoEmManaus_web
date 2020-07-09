'''
    Esta arquivo contem classes responsaveis por realizar
    operacoes com o banco de dados do firebase


    Edson Jr
    Jul 2020

'''
import pyrebase
from firebase import firebase
from  .firebaseUrls import pathBase,pathListCategoryNode,pathListShowHouseNode,pathListShows

class FirebaseService:

    __TAG = '[FirebaseService]: '
    firebase = firebase.FirebaseApplication(pathBase,None)


    def getData(self,urlNode):
        data = None

        print(self.__TAG + 'Getting data from ' + urlNode + '\n\n')
        
        try:
            data = self.firebase.get(urlNode,'')
        except:
            print(self.__TAG + 'Error: cannot get data')
        finally:
            return data
        
        


    def saveData(self,urlNode,data):
        print(self.__TAG + "Saving data " + str(data) + " to " + urlNode)
        commit = None

        try:
            commit = firebase.post(urlNode,data)
        except:
            print(self.__TAG + 'Error: Cannot save data into firebase')
        finally:
            return commit
        




    def deleteData(self):
        pass



    def updateData(self):
        pass








