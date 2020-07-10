from services.firebaseServices.firebaseService import FirebaseService
from services.firebaseServices.firebaseUrls import pathListCategoryNode,pathListCategoryNode,pathListShowHouseNode,pathListShows




#pegando os dados do firebase
firebaseDAO = FirebaseService()
data = firebaseDAO.getData(pathListShows)
print(str(data))


data = {
    'child' : 'show CHield'
}

