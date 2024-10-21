from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/entregador")
templates = obter_jinja_templates("templates")

@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/index_entregador.html", {"request": request})

@router.get("/finalizar_entrega", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/finalizar_entrega.html", {"request": request})

@router.get("/lista_mensagens", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/lista_mensagens.html", {"request": request})

@router.get("/montar_box", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/montar_box.html", {"request": request})

@router.get("/pagina_entregas", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/pagina_entregas.html", {"request": request})

@router.get("/perfil_entregador", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/perfil_entregador.html", {"request": request})

@router.get("/perfis_seguindo", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/perfis_seguindo.html", {"request": request})

@router.get("/pedidos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/pedidos.html", {"request": request})

@router.get("/visualizar_entrega", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/visualizar_entrega.html", {"request": request})