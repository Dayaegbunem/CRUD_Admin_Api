import pymongo,io
import urllib.parse

client = pymongo.MongoClient("mongodb+srv://"+urllib.parse.quote_plus('Dayaegbunem')+":"+urllib.parse.quote_plus('zYqp7wmUXx2nBZV0')+"@cluster0.yysevdx.mongodb.net/?retryWrites=true&w=majority")

db = client.storage_application

collection_name = db['items_app']
