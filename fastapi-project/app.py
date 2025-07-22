from fastapi import FastAPI, Query
import json

def load_data():
    with open("patients.json", "r") as f:
        data=json.load(f)
    return data


app = FastAPI() #to run the server

#@app.route("/", methods=["GET"])
#uvicorn app:app --reload (to run)
#name=request.args.get("name") --normally 

@app.get("/")
def hello():
    return {"message": "Hello from App"}

@app.get("/about")
def about(name: str = Query("Stranger", description = "You need to give a description")): #(...) shows necessary
    message = f'This app is build in colab with {name}'
    return message

@app.get("/view")
def view():
    return load_data()
