from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/administrador")
templates = obter_jinja_templates("templates")

@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/index_adm.html", {"request": request})

@router.get("/exclusao", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/exc_not.html", {"request": request})

@router.get("/meus_dados", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/meus_dados.html", {"request": request})

@router.get("/cadastrar_categorias", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/cadastrar_categorias.html", {"request": request})

@router.get("/gerenciar_anuncios", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/gerenciar_anuncios.html", {"request": request})

@router.get("/gerenciar_contas", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/gerenciar_contas.html", {"request": request})

@router.get("/gerenciar_categorias", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/gerenciar_categorias.html", {"request": request})

@router.get("/editar_conta", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/editar_conta.html", {"request": request})

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

@router.get("/perfil_administrador", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/perfil_administrador.html", {"request": request})
