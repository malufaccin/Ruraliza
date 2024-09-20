import dotenv
from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from repositories.usuario_repo import UsuarioRepo
from routes.main_routes import router as main_router
from routes.administrador_routes import router as administrador_router
from routes.cliente_routes import router as cliente_router
from routes.produtor_routes import router as produtor_router
from routes.entregador_routes import router as entregador_router
from util.exceptions import configurar_excecoes
from util.auth import checar_autenticacao, checar_autorizacao

UsuarioRepo.criar_tabela()
dotenv.load_dotenv()
app = FastAPI(dependencies=[Depends(checar_autorizacao)])
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
app.middleware("http")(checar_autenticacao)
configurar_excecoes(app)
app.include_router(main_router)
app.include_router(administrador_router)
app.include_router(cliente_router)
app.include_router(produtor_router)
app.include_router(entregador_router)