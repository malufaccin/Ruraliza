from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Usuario:
    id: Optional[str] = None
    nome: Optional[str] = None
    data_nascimento: Optional[str] = None
    cpf: Optional[int] = None
    telefone: Optional[str] = None
    email: Optional[str] = None
    senha: Optional[str] = None
    perfil: Optional[int] = None
    cpr: Optional[int] = None
    endereco: Optional[str] = None
    cnpj: Optional[int] = None
    tipo_veiculo: Optional[str] = None
    cor: Optional[str] = None
    placa: Optional[str] = None
    cnh: Optional[int] = None
    token: Optional[str] = None
