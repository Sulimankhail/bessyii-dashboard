from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="src/templates")
@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    #return FileResponse("src/templates/index.html")
    countries = ['Afghanistan', 'USA', 'Russia']
    return templates.TemplateResponse("index.html", {"request": request, "countries": countries})