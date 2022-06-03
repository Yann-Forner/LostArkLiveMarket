import requests
def getByCat(reg,cat,subCat="None"):
    url = 'https://www.lostarkmarket.online/api/export-market-live/'+reg+"?category="+cat
    if subCat != "None":
        url += "&subcategory="+subCat
    return requests.get(url).json()

def getById(reg,id):
    url = 'https://www.lostarkmarket.online/api/export-market-live/'+reg+"?items="+id
    return requests.get(url).json()

def getMarketHistoryById(reg,id):
    url = "https://www.lostarkmarket.online/api/export-item-history/"+reg+"/"+id+"?format=json"
    return requests.get(url).json()