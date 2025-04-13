from app.database import inserir_comando, buscar_comandos

def lembrar_comando(comando):
    inserir_comando(comando)

def listar_comandos():
    return buscar_comandos()
