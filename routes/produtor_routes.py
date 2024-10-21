from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/produtor")

templates = obter_jinja_templates("templates")

@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/index_produtor.html", {"request": request})

@router.get("/adicionar_produto", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/adicionar_produto.html", {"request": request})

@router.get("/lista_pedidos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/lista_pedidos.html", {"request": request})

@router.get("/lista_produtos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/lista_produtos.html", {"request": request})

@router.get("/lista_mensagens", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/lista_mensagens.html", {"request": request})

@router.get("/montar_box", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/montar_box.html", {"request": request})

@router.get("/perfil", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/produtor.html", {"request": request})

@router.get("/perfis_seguindo", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/perfis_seguindo.html", {"request": request})

@router.get("/pedidos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/pedidos.html", {"request": request})