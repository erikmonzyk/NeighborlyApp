import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://cosmosdbforfunctionapp:mfXB7AYSLHMtKLbFKT0sYWB6TqGTmZxM10hawNez6UtSYmmP0F4WxzP4iaj5uWYK6POW6km48KAoqmfTvQywYA==@cosmosdbforfunctionapp.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@cosmosdbforfunctionapp@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['AdvertsPosts']
        collection = database['Advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

