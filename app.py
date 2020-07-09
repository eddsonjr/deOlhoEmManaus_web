from services.firebaseServices.firebaseService import FirebaseService
from services.firebaseServices.firebaseUrls import pathListCategoryNode,pathListCategoryNode,pathListShowHouseNode,pathListShows




#pegando os dados do firebase
firebaseDAO = FirebaseService()
data = firebaseDAO.getData(pathListCategoryNode)
print(str(data))


data = {
    '27' : 'pablo_viadao'
}

#tentando criar uma nova categoria
commit = firebaseDAO.saveData(pathListCategoryNode,data)
print(str(data))