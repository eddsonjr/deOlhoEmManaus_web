'''
    Este arqui contem as urls de acesso aos nodes do banco de dados

    Edson Jr
    Jul 2020
'''
from enum import Enum
class FirebaseUrls(Enum):

    #path db base
    pathBase = 'https://deolhoemmanaustests.firebaseio.com/'
    
    #path para lista de shows
    pathListShows = '/show/'

    #path para a lista de casas de show
    pathListShowHouseNode = '/showHouse'

    #path para a lista de categorias
    pathListCategoryNode = '/category/-LrarCqAGUtS3LqUFg1S/listCategory'


    