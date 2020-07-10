'''
    Esta arquivo contem classes responsaveis por realizar
    operacoes com o banco de dados do firebase


    Edson Jr
    Jul 2020


    Documentacao:
        https://pypi.org/project/firebase/

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
        except Exception as e:
            print(self.__TAG + 'Error when getting firebase data')
            print(self.__TAG + str(e))
        finally:
            return valueArray


        

    def saveData(self,urlNode,data,childKey = None):
        print(self.__TAG + 'Saving data into ' + urlNode)

        success = False

        try:
            if childKey:
                self.db.child(urlNode).child(childKey).set(data)
                success = True
            else:
                self.db.child(urlNode).push(data)
                success = True
        except Exception as e:
            print(self.__TAG + 'Error when saving data into firebase')
            print(self.__TAG + str(e))
        finally:
            return success


    



    def deleteData(self,urlNode):
        print(self.__TAG + "Removing data from " + urlNode)

        success = False

        try:
            self.db.child(urlNode).remove()
            success = True
        except Exception as e:
            print(self.__TAG + "Error when deleting data from firebase")
            print(self.__TAG + str(e))
        finally:
            return success

        



    def updateData(self,urlNode,data):
        print(self.__TAG + "Updating data into " + urlNode) 

        success = False

        try:
            self.db.child(urlNode).update(data)
            success = True
            '''
                Atencao: se o usuario informar um caminho que nao
                existe no banco de dados, a lib cria um contendo
                esse caminho nao existente e salva os dados ao inves
                de atualizar
 
            '''
        except Exception as e:
            print(self.__TAG + "Error when update data")
            print(self.__TAG + str(e))
        finally:
            return success

