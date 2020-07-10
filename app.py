from services.firebaseServices.firebaseService import FirebaseService
from services.firebaseServices.firebaseUrls import FirebaseUrls




#pegando os dados do firebase
firebaseDAO = FirebaseService()
data = firebaseDAO.getData(FirebaseUrls.pathListShows.value)
print(str(data))


data = {
    'testing' : 'testing the update function',
    'watch' : 'firebase rulez'
}


#firebaseDAO.saveData(pathListShows,data,'testChildKey2')

#path = pathListShows + '/-MBl90nVBxYz4UWS9Hoz11111'
#result = firebaseDAO.getData()
#print(result)
