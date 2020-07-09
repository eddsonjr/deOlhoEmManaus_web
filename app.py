from services.firebaseServices.firebaseService import FirebaseService
from services.firebaseServices.firebaseUrls import pathListCategoryNode,pathListCategoryNode,pathListShowHouseNode,pathListShows




#pegando os dados do firebase
firebaseDAO = FirebaseService()
data = firebaseDAO.getData(pathListCategoryNode)
print(str(data))


data = {
    'child' : 'show CHield'
}


#tentando criar uma nova categoria
#commit = firebaseDAO.saveData(pathListShows,data)
#print(str(commit))


firebaseDAO.saveChild(data,'/show/-MBl90nVBxYz4UWS9Hoz')

