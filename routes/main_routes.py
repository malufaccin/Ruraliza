from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates

router = APIRouter()
templates = obter_jinja_templates("templates")


@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/index.html", {"request": request})

@router.get("/configuracoes", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/configuracoes.html", {"request": request})

@router.get("/entrar", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/entrar.html", {"request": request})

@router.get("/login", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/login.html", {"request": request})

@router.get("/categoria_frutas", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/categoria_frutas.html", {"request": request})

@router.get("/categoria_vegetais", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/categoria_vegetais.html", {"request": request})

@router.get("/categoria_temperos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/categoria_temperos.html", {"request": request})

@router.get("/categoria_graos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/categoria_graos.html", {"request": request})

@router.get("/categoria_compotas", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/categoria_compotas.html", {"request": request})

@router.get("/categoria_producoes_rurais", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/categoria_producoes_rurais.html", {"request": request})

@router.get("/assinar", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/assinar.html", {"request": request})

@router.get("/bemvindo", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/bemvindo.html", {"request": request})

@router.get("/criar_conta_cliente1", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/criar_conta_cliente1.html", {"request": request})

@router.get("/criar_conta_cliente2", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/criar_conta_cliente2.html", {"request": request})

@router.get("/criar_conta_entregador1", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/criar_conta_entregador1.html", {"request": request})

@router.get("/criar_conta_entregador2", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/criar_conta_entregador2.html", {"request": request})

@router.get("/criar_conta_entregador3", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/criar_conta_entregador3.html", {"request": request})

@router.get("/criar_conta_produtor1", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/criar_conta_produtor1.html", {"request": request})

@router.get("/criar_conta_produtor2", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/criar_conta_produtor2.html", {"request": request})

@router.get("/criar_conta_produtor3", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/criar_conta_produtor3.html", {"request": request})

@router.get("/mudar_conta", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/mudar_conta.html", {"request": request})

@router.get("/perfil_produtor", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/perfil_produtor.html", {"request": request})

@router.get("/perfil_usuario", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/perfil_usuario.html", {"request": request})

@router.get("/pesquisa", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/pesquisa.html", {"request": request})

@router.get("/produto", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/produto.html", {"request": request})

@router.get("/selecionar_tipo_perfil", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/selecionar_tipo_perfil.html", {"request": request})

@router.get("/sobrenos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/sobrenos.html", {"request": request})

@router.get("/termos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/termos.html", {"request": request})
