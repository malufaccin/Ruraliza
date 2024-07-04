<<<<<<< HEAD:ProjetoBase/routes/produtor_routes.py
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates

router = APIRouter()
templates = obter_jinja_templates("templates/main")


@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})

@router.get("/configuracoes", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/configuracoes.html", {"request": request})

@router.get("/entrar", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/entrar.html", {"request": request})

@router.get("/login", response_class=HTMLResponse)
async def get_root(request: Request):
=======
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates

router = APIRouter()
templates = obter_jinja_templates("templates/main")


@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})

@router.get("/configuracoes", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/configuracoes.html", {"request": request})

@router.get("/entrar", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/entrar.html", {"request": request})

@router.get("/login", response_class=HTMLResponse)
async def get_root(request: Request):
>>>>>>> 4a8cacf03fdccd70c499bad177231ea460c9f5db:routes/produtor_routes.py
    return templates.TemplateResponse("pages/login.html", {"request": request})