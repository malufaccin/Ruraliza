<<<<<<< HEAD:ProjetoBase/routes/cliente_routes.py
=======
<<<<<<<< HEAD:ProjetoBase/routes/main_routes.py
>>>>>>> 4a8cacf03fdccd70c499bad177231ea460c9f5db:routes/cliente_routes.py
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates

router = APIRouter()
<<<<<<< HEAD:ProjetoBase/routes/cliente_routes.py
templates = obter_jinja_templates("templates/cliente")
=======
templates = obter_jinja_templates("templates/main")
>>>>>>> 4a8cacf03fdccd70c499bad177231ea460c9f5db:routes/cliente_routes.py


@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})

<<<<<<< HEAD:ProjetoBase/routes/cliente_routes.py
=======
@router.get("/configuracoes", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/configuracoes.html", {"request": request})

@router.get("/entrar", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/entrar.html", {"request": request})

@router.get("/login", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/login.html", {"request": request})
========
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates

router = APIRouter()
templates = obter_jinja_templates("templates/cliente")


@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})

>>>>>>>> 4a8cacf03fdccd70c499bad177231ea460c9f5db:routes/cliente_routes.py
>>>>>>> 4a8cacf03fdccd70c499bad177231ea460c9f5db:routes/cliente_routes.py
