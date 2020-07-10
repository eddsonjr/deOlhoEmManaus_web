'''
    Esta arquivo contem classes responsaveis por realizar
    operacoes com o banco de dados do firebase


    Edson Jr
    Jul 2020

'''
import pyrebase
from firebase import Firebase
from  .firebaseUrls import pathBase,pathListCategoryNode,pathListShowHouseNode,pathListShows
from  .firebaseConf import firebaseConf

class FirebaseService:

    __TAG = '[FirebaseService]: '
    firebaseObj = Firebase(firebaseConf)
    db = firebaseObj.database()


    def getData(self,urlNode):
        print(self.__TAG + "Getting data from node: " + urlNode)
       
        all_data = None
        valueArray = []

        try:
            all_data = self.db.child(urlNode).get()
            for data in all_data.each():
                valueArray.append({data.key():data.val()})
        except:
            print(self.__TAG + 'Error when getting firebase data')
        finally:
            return valueArray



        
                
        
    def saveData(self,urlNode,data):
       pass




    def deleteData(self):
        pass



    def updateData(self):
        pass








