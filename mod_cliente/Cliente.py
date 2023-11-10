from pydantic import BaseModel

class Cliente(BaseModel):
    id_cliente: int = None
    nome: str
    cpf: str
    telefone: str = None
    senha: str = None
    compra_fiado: int = None
    dia_fiado: int = None