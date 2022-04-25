import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://cosmosdbforfunctionapp:mfXB7AYSLHMtKLbFKT0sYWB6TqGTmZxM10hawNez6UtSYmmP0F4WxzP4iaj5uWYK6POW6km48KAoqmfTvQywYA==@cosmosdbforfunctionapp.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@cosmosdbforfunctionapp@"
            client = pymongo.MongoClient(url)
            database = client['AdvertsPosts']
            collection = database['Advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
