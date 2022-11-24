from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/my-first-api")
def hello(name: str):
  return {'Hello ' + name + '!'}


if __name__ == '__main__':
  resp = requests.get('http://127.0.0.1:8000/my-first-api?name=Ander.')
