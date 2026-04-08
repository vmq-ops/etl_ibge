import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def load(documentos):
    uri = os.getenv("MONGODB_URI")

    client     = MongoClient(uri)
    db         = client["ibge_db"]
    collection = db["taxa_desocupacao"]

    inseridos  = 0
    ignorados  = 0

    for doc in documentos:
        existe = collection.find_one({
            "categoria": doc["categoria"],
            "periodo":   doc["periodo"]
        })

        if not existe:
            collection.insert_one(doc)
            inseridos += 1
        else:
            ignorados += 1

    print(f"[LOAD] {inseridos} inseridos | {ignorados} já existiam.")
    client.close()