from dataclasses import dataclass
from typing import Optional


@dataclass
class Usuario:
    id: Optional[str] = None
    nome: Optional[str] = None
    email: Optional[str] = None
    cpf: Optional[int] = None
    data_nascimento: Optional[int] = None
    senha: Optional[str] = None
    cpr: Optional[int] = None
    endereco: Optional[str] = None
    numero: Optional[int] = None
    cnpj: Optional[int] = None
    tipo_veiculo: Optional[str] = None
    cor: Optional[str] = None
    placa: Optional[str] = None
    cnh: Optional[int] = None
    perfil: Optional[int] = None
    token: Optional[str] = None
