
from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse

from models.usuario_model import Usuario
from repositories.usuario_repo import UsuarioRepo
from util.auth import NOME_COOKIE_AUTH, criar_token, obter_hash_senha 
from util.templates import obter_jinja_templates

router = APIRouter()
templates = obter_jinja_templates("templates")


@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    usuario = request.state.usuario if hasattr(request.state, "usuario") else None
    if not usuario or not usuario.email:
        return templates.TemplateResponse("main/pages/index.html", {"request": request})


@router.post("/post_entrar")
async def post_entrar(
    email: str = Form(...), 
    senha: str = Form(...)):
    usuario = UsuarioRepo.checar_credenciais(email, senha)
    if usuario is None:
        response = RedirectResponse("/login", status_code=status.HTTP_303_SEE_OTHER)
        return response
    token = criar_token(usuario[0], usuario[1], usuario[2])
    nome_perfil = None
    match (usuario[2]):
        case 1: nome_perfil = "produtor"
        case 2: nome_perfil = "cliente"
        case 3: nome_perfil = "entregador"
        case 4: nome_perfil = "administrador"
        case _: nome_perfil = ""    
    response = RedirectResponse(f"/{nome_perfil}", status_code=status.HTTP_303_SEE_OTHER)    
    response.set_cookie(
        key=NOME_COOKIE_AUTH,
        value=token,
        max_age=3600*24*365*10,
        httponly=True,
        samesite="lax"
    )
    return response


@router.post("/post_cadastrar_cliente")
async def post_cadastrar_cliente(
    nome: str = Form(...),
    data_nascimento: str = Form(...),
    cpf: str = Form(...),
    telefone: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    confsenha: str = Form(...)):
    if senha != confsenha:
        return RedirectResponse("/cadastro", status_code=status.HTTP_303_SEE_OTHER)
    senha_hash = obter_hash_senha(senha)
    usuario = Usuario(
        nome=nome,
        data_nascimento=data_nascimento,
        cpf=cpf,
        telefone=telefone,
        email=email,
        senha=senha_hash,
        perfil = 2)
    UsuarioRepo.inserir_cliente(usuario)
    response = RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)
    return response
    
@router.post("/post_cadastrar_produtor")
async def post_cadastrar_produtor(
    nome: str = Form(...),
    data_nascimento: str = Form(...),
    cpf: str = Form(...),
    telefone: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    confsenha: str = Form(...),
    cpr: int = Form(...),
    endereco: str = Form(...),
    cnpj: int = Form(...)):
    if senha != confsenha:
        return RedirectResponse("/cadastro", status_code=status.HTTP_303_SEE_OTHER)
    senha_hash = obter_hash_senha(senha)
    usuario = Usuario(
        nome=nome,
        data_nascimento=data_nascimento,
        cpf=cpf,
        telefone=telefone,
        email=email,
        senha=senha_hash,
        perfil = 1,
        cpr=cpr,
        endereco=endereco,
        cnpj=cnpj)
    UsuarioRepo.inserir_produtor(usuario)
    response = RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)
    return response

@router.post("/post_cadastrar_entregador")
async def post_cadastrar_entregador(
    nome: str = Form(...),
    data_nascimento: str = Form(...),
    cpf: str = Form(...),
    telefone: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    confsenha: str = Form(...),
    tipo_veiculo: str = Form(...),
    cor: str = Form(...),
    placa: str = Form(...),
    cnh: str = Form(...),):
    if senha != confsenha:
        return RedirectResponse("/cadastro", status_code=status.HTTP_303_SEE_OTHER)
    senha_hash = obter_hash_senha(senha)
    usuario = Usuario(
        nome=nome,
        data_nascimento=data_nascimento,
        cpf=cpf,
        telefone=telefone,
        email=email,
        senha=senha_hash,
        perfil = 3,
        tipo_veiculo=tipo_veiculo,
        cor=cor,
        placa=placa,
        cnh=cnh)
    UsuarioRepo.inserir_entregador(usuario)
    response = RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)
    return response

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

@router.get("/contatos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/contatos.html", {"request": request})

@router.get("/meus_dados", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/meus_dados.html", {"request": request})

@router.get("/enderecos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/enderecos.html", {"request": request})

@router.get("/adicionar_endereco", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("/main/pages/adicionar_endereco.html", {"request": request})

@router.get("/feedback", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/feedback.html", {"request": request})

@router.get("/mudar_conta", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/mudar_conta.html", {"request": request})

@router.get("/lista_mensagens", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/lista_mensagens.html", {"request": request})

@router.get("/cesta", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/cesta.html", {"request": request})