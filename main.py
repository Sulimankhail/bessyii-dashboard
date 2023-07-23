from fastapi import FastAPI
from pymongo import MongoClient
from src.controller import index_controller
import uvicorn
from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles



app = FastAPI()
app.mount("/templates", StaticFiles(directory="src/templates"), name="static")


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient("mongodb://localhost:27017/")
    app.database = app.mongodb_client["bessyii"]


@app.on_event("shutdown")
def shutdown_db_client():
    pass

app.include_router(index_controller.router, tags=["index"], prefix="")


@app.get("/healthcheck/")
def healthcheck():
    return 'Health - OK'




router = APIRouter()

#templates = Jinja2Templates(directory="src/templates")


#@app.get("/", response_class=HTMLResponse)
#async def index(request: Request):
 #   countries = ['Afghanistan', 'USA', 'Russia']

  #  return templates.TemplateResponse("index.html", {"request": request, "countries": countries})
   # return FileResponse("src/templates/index.html")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
