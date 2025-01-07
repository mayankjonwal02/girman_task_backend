import pymongo
from girman_app.serializer import UserDataSerializer
from bson import ObjectId 
def get_connection():
    connectionstring = "mongodb+srv://jonwal:jonwal@girmancluster.fju12.mongodb.net/?retryWrites=true&w=majority&appName=GirmanCluster"

    try:
        connection = pymongo.MongoClient(connectionstring)
        return connection
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s" % e)
        return None
    
def get_all_data():
    connection = get_connection()
    collection = connection["girman"]["userdata"]
    data = collection.find()
    data = list(data)
    for i in range(len(data)):
        data[i]['_id'] = str(data[i]['_id'])  
    return data



def insert_data(data):
    connection = get_connection()
    if connection:
        collection = connection["girman"]["userdata"]
        try:
            result = collection.insert_one(data)  
            data["_id"] = str(result.inserted_id)  
            return data  
        except Exception as e:
            print(f"Error inserting data: {e}")
            return None
    else:
        return None
