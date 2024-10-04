SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data_nascimento TEXT NOT NULL,
        cpf INT NOT NULL UNIQUE,
        telefone TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        perfil INT NOT NULL,
        cpr INT,
        endereco TEXT,
        cnpj INT,
        tipo_veiculo TEXT,
        cor TEXT,
        placa TEXT,
        cnh TEXT,        
        token TEXT)
"""

SQL_INSERIR_CLIENTE = """
    INSERT INTO usuario(nome, data_nascimento, cpf, telefone, email, senha)
    VALUES (?, ?, ?, ?, ?, ?)
"""

SQL_INSERIR_PRODUTOR = """
    INSERT INTO usuario(nome, data_nascimento, cpf, telefone, email, senha, perfil, cpr, endereco, cnpj)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

SQL_INSERIR_ENTREGADOR  = """
    INSERT INTO usuario(nome, data_nascimento, cpf, telefone, email, senha, tipo_veiculo, cor, placa, cnh)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

SQL_ALTERAR = """
    UPDATE usuario
    SET nome=?, email=?
    WHERE id=?
"""

SQL_ALTERAR_TOKEN = """
    UPDATE usuario
    SET token=?
    WHERE id=?
"""

SQL_EXCLUIR = """
    DELETE FROM usuario    
    WHERE id=?
"""

SQL_OBTER_POR_ID = """
    SELECT id, nome, email, token
    FROM usuario
    WHERE id=?
"""

SQL_OBTER_POR_EMAIL = """
    SELECT id, nome, email, token
    FROM usuario
    WHERE id=?
"""

SQL_OBTER_POR_TOKEN = """
    SELECT id, nome, email, token
    FROM usuario
    WHERE token=?
"""

SQL_OBTER_QUANTIDADE = """
    SELECT COUNT(*)
    FROM usuario
"""

SQL_EMAIL_EXISTE = """
    SELECT COUNT(*)
    FROM usuario
    WHERE email=?
"""
