from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/entregador")
templates = obter_jinja_templates("templates")

@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/index_entregador.html", {"request": request})

@router.get("/visualizar_entrega", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/visualizar_entrega.html", {"request": request})

@router.get("/pagina_entregas", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/pagina_entregas.html", {"request": request})

@router.get("/meus_dados", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/meus_dados.html", {"request": request})

@router.get("/finalizar_entrega", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/finalizar_entrega.html", {"request": request})

@router.get("/enderecos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/enderecos.html", {"request": request})

@router.get("/adicionar_endereco", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("/main/pages/adicionar_endereco.html", {"request": request})

@router.get("/contatos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/contatos.html", {"request": request})

@router.get("/feedback", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/feedback.html", {"request": request})

@router.get("/lista_mensagens", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/lista_mensagens.html", {"request": request})

@router.get("/perfil_entregador", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/perfil_entregador.html", {"request": request})

