from fastapi import FastAPI, HTTPException

app = FastAPI()

items = dict()


@app.get("/")
def read_root():
    return items


@app.get("/items/{key}")
def read_item(key):
    if key in items.keys():
        return items[key]
    else:
        raise HTTPException(status_code=404, detail=f"Item with key {key} not found")


@app.post("/items/{key}")
def create_item(key, value):
    if key not in items.keys():
        items[key] = value
    else:
        raise HTTPException(status_code=409, detail=f"Item with key {key} already exists")


@app.patch("/items/{key}")
def update_item(key, value):
    if key in items.keys():
        items[key] = value
    else:
        raise HTTPException(status_code=404, detail=f"Item with key {key} not found")


@app.delete("/items/{key}")
def delete_item(key):
    items.pop(key, None)
