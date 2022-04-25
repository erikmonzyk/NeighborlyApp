import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://cosmosdbforfunctionapp:mfXB7AYSLHMtKLbFKT0sYWB6TqGTmZxM10hawNez6UtSYmmP0F4WxzP4iaj5uWYK6POW6km48KAoqmfTvQywYA==@cosmosdbforfunctionapp.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@cosmosdbforfunctionapp@"
        client = pymongo.MongoClient(url)
        database = client['AdvertsPosts']
        collection = database['Posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)