from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

from fastapi.middleware.cors import CORSMiddleware

from services.preguntas import router as preguntas_router

from database.db import Base, engine


app = FastAPI(
    title="Consultio agente IA",
    description= "Empezando proyecto de API",
    version="1.0.0"

)

app.add_middleware(
    CORSMiddleware
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


app.include_router(preguntas_router)

Base.metadata.create_all(bind=engine)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
)
