import pymongo
import os


class MongodbClient:
    client = None

    def __init__(self, database_name=os.environ["DATABASE_NAME"]) -> None:
        if MongodbClient.client is None:
            MongodbClient.client = pymongo.MongoClient(
                f"mongodb+srv://{os.environ['ATLAS_CLUSTER_USERNAME']}:{os.environ['ATLAS_CLUSTER_PASSWORD']}@cluster0.vmj90.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
            )
        self.client = MongodbClient.client
        self.database = self.client[database_name]
        self.database_name = database_name
