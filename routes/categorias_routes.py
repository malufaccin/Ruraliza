from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates

router = APIRouter()
templates = obter_jinja_templates("templates/main")


@router.get("/frutas", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/categoria_frutas.html", {"request": request})

@router.get("/vegetais", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/categoria_vegetais.html", {"request": request})

@router.get("/temperos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/categoria_temperos.html", {"request": request})

@router.get("/compotas", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/categoria_compotas.html", {"request": request})

@router.get("/laticineos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/categoria_laticineos.html", {"request": request})