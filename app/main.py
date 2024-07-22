from typing import Union

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")

# steps
# 1. save all dependencies in requirements.txt file.
# 2. create docker file in root directory of project.
# 3. Create an image using docker build -t fastapi . command.
