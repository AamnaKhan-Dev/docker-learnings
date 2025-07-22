from fastapi import FastAPI, Query, Path, HTTPException
from fastapi.responses import FileResponse
import json

def load_data():
    with open("patients.json","r") as f:
        data=json.load(f)
    return data

app = FastAPI()

@app.get("/")
def hello():
    return {"msg": "World"}

@app.get("/view")
def view():
    return FileResponse('flower.jpg')

@app.get('/about')
def about(name: str = Query(...), description = "Give your name in url like this ?name=Your name"):
    msg=f'Hey {name} 👋, This app is work in progress 🛠.. Go Away!!'
    return msg

@app.get('/record')
def patients():
    return load_data()


@app.get("/record/{id}")
def view_specific(id: str = Path(description='')):
    data = load_data()
    return data[id]

@app.get("/sort")
def sort(param: str = Query(..., description='Parameter to sort by'),
          type: str = Query("desc", description='Sort type (asc or desc)')):
    
    data = load_data()
    reverse = True if type == 'desc' else False
    checks = ['height', 'weight', 'age', 'bmi']
    
    if param in checks:
        sort_data = sorted(data.items(), key = lambda X: int(X[1].get(param)), reverse=reverse) #.items and .values
        
        
    else:
        raise HTTPException(status_code=404, detail='This parameter doesn\'t exist')
        
        
    return sort_data
    
