import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://cosmosdbforfunctionapp:mfXB7AYSLHMtKLbFKT0sYWB6TqGTmZxM10hawNez6UtSYmmP0F4WxzP4iaj5uWYK6POW6km48KAoqmfTvQywYA==@cosmosdbforfunctionapp.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@cosmosdbforfunctionapp@"  
            client = pymongo.MongoClient(url)
            database = client['AdvertsPosts']
            collection = database['Advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )