from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    """
    displays the stock screener dashboard / homepage
    """
    return templates.TemplateResponse("home.html", {
        "request": request,
        "somevar": 2
    })

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    result = {"item_id": item_id, "q": q}
    print(type(result))
    return result

@app.post("/stock")
def create_stock():
    """
    created a stock and stores it in the database
    """
    return {
        "code": "success",
        "message": "stock created"
    }