from fastapi import FastAPI

app = FastAPI()

items = [
    {"id":1, "name":"MACK LAFOND","profil":"Développeur"},
    {"id":2, "name":"Maxina","profil":"Développeur Fullstack"}
]

@app.get("/health")
def health_check():
    return {"status":"ok"}

@app.get("/items")
def get_items():
    return items

@app.get("/item/{item_id}")
def get_item(item_id:int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item no found"}

@app.post("/items")
def create_item(item:dict):
    items.append(item)
    return item