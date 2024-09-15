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

@router.get("/cesta", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/cesta.html", {"request": request})

@router.get("/adicionar_endereco", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("/main/pages/adicionar_endereco.html", {"request": request})

@router.get("/adicionar_produto", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/adicionar_produto.html", {"request": request})

@router.get("/assinar", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/assinar.html", {"request": request})

@router.get("/avaliar", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/avaliar.html", {"request": request})

@router.get("/avaliar_2", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/avaliar_2.html", {"request": request})

@router.get("/bemvindo", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/bemvindo.html", {"request": request})

@router.get("/cadastrar_categorias", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/cadastrar_categorias.html", {"request": request})

@router.get("/categoria_frutas", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/categoria_frutas.html", {"request": request})

@router.get("/categoria_vegetais", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/categoria_vegetais.html", {"request": request})

@router.get("/categoria_temperos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/categoria_temperos.html", {"request": request})

@router.get("/contatos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/contatos.html", {"request": request})

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

@router.get("/cupons", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/cupons.html", {"request": request})

@router.get("/editar_conta", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/editar_conta.html", {"request": request})

@router.get("/enderecos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/enderecos.html", {"request": request})

@router.get("/fazer_pedido", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/fazer_pedido.html", {"request": request})

@router.get("/feedback", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/feedback.html", {"request": request})

@router.get("/finalizar_entrega", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/finalizar_entrega.html", {"request": request})

@router.get("/gerenciar_anuncios", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/gerenciar_anuncios.html", {"request": request})

@router.get("/gerenciar_contas", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/gerenciar_contas.html", {"request": request})

@router.get("/gerenciar_categorias", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/gerenciar_categorias.html", {"request": request})

@router.get("/meus_dados", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/meus_dados.html", {"request": request})

@router.get("/lista_mensagens", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/lista_mensagens.html", {"request": request})

@router.get("/lista_pedidos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/lista_pedidos.html", {"request": request})

@router.get("/lista_produtos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/lista_produtos.html", {"request": request})

@router.get("/montar_box", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/montar_box.html", {"request": request})

@router.get("/mudar_conta", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/mudar_conta.html", {"request": request})

@router.get("/pagina_entregas", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/pagina_entregas.html", {"request": request})

@router.get("/pedidos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/pedidos.html", {"request": request})

@router.get("/perfil_administrador", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/perfil_administrador.html", {"request": request})

@router.get("/perfil_entregador", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/perfil_entregador.html", {"request": request})

@router.get("/perfil_produtor", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/perfil_produtor.html", {"request": request})

@router.get("/perfil_usuario", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/perfil_usuario.html", {"request": request})

@router.get("/perfis_seguindo", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/perfis_seguindo.html", {"request": request})

@router.get("/pesquisa", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/pesquisa.html", {"request": request})

@router.get("/produto", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/produto.html", {"request": request})

@router.get("/rastreio_enviado", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/rastreio_enviado.html", {"request": request})

@router.get("/rastreio", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/rastreio.html", {"request": request})

@router.get("/selecionar_tipo_perfil", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/selecionar_tipo_perfil.html", {"request": request})

@router.get("/sobrenos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/sobrenos.html", {"request": request})

@router.get("/termos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/termos.html", {"request": request})

@router.get("/vendedor", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/vendedor.html", {"request": request})

@router.get("/visualizar_entrega", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/visualizar_entrega.html", {"request": request})
