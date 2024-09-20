from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/cliente")
templates = obter_jinja_templates("templates")

@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/index_usuario.html", {"request": request})

@router.get("/rastreio_enviado", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/rastreio_enviado.html", {"request": request})

@router.get("/rastreio", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/rastreio.html", {"request": request})

@router.get("/pedidos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/pedidos.html", {"request": request})

@router.get("/montar_box", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/montar_box.html", {"request": request})

@router.get("/meus_dados", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/meus_dados.html", {"request": request})

@router.get("/cesta", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/cesta.html", {"request": request})

@router.get("/enderecos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/enderecos.html", {"request": request})

@router.get("/adicionar_endereco", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("/main/pages/adicionar_endereco.html", {"request": request})

@router.get("/avaliar", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/avaliar.html", {"request": request})

@router.get("/avaliar_2", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/avaliar_2.html", {"request": request})

@router.get("/contatos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/contatos.html", {"request": request})

@router.get("/cupons", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/cupons.html", {"request": request})

@router.get("/fazer_pedido", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/fazer_pedido.html", {"request": request})

@router.get("/feedback", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/feedback.html", {"request": request})

@router.get("/lista_mensagens", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/lista_mensagens.html", {"request": request})

@router.get("/perfis_seguindo", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/perfis_seguindo.html", {"request": request})

