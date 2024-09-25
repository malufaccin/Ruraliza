from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/produtor")

templates = obter_jinja_templates("templates")

@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/index_produtor.html", {"request": request})

@router.get("/meus_dados", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/meus_dados.html", {"request": request})

@router.get("/vendedor", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/vendedor.html", {"request": request})

@router.get("/lista_pedidos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/lista_pedidos.html", {"request": request})

@router.get("/lista_produtos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/lista_produtos.html", {"request": request})

@router.get("/adicionar_produto", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/adicionar_produto.html", {"request": request})

@router.get("/enderecos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/enderecos.html", {"request": request})

@router.get("/adicionar_endereco", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("/main/pages/adicionar_endereco.html", {"request": request})

@router.get("/feedback", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/feedback.html", {"request": request})

@router.get("/lista_mensagens", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/lista_mensagens.html", {"request": request})

@router.get("/mudar_conta", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/mudar_conta.html", {"request": request})