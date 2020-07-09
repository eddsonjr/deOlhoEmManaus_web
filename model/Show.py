''' 
    Classe de model para Show

    Edson Jr
    Jul 2020
'''


class Show:

    def __init__(self,id,imgUrl,hasDate,endDate,showHouse,showHouseKey,category,subCategory,startDate):
        self.id = id
        self.imgUrl = imgUrl
        self.hasDate = hasDate
        self.endDate = endDate
        self.showHouse = showHouse
        self.showHouseKey = showHouseKey
        self.category = category
        self.subCategory = subCategory
        self.startDate = startDate