import subprocess
from github import Github
import os

# Instalar o PyGitHub automaticamente, se não estiver instalado
try:
    import github
except ImportError:
    subprocess.check_call(["pip", "install", "PyGithub"])

# Configurações
GITHUB_TOKEN = "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"  # Substitua pelo token gerado
REPO_NAME = "dz09pl/Upload"  # Nome do repositório no formato 'usuario/nome-repositorio'

# Entrada do usuário para o caminho do arquivo
FILE_PATH = input("Digite o caminho completo do arquivo que deseja enviar: ").strip()

# Verificar se o caminho do arquivo existe
if not os.path.isfile(FILE_PATH):
    print(f"Erro: O arquivo '{FILE_PATH}' não foi encontrado.")
    exit()

# Definir o caminho no repositório como o nome do arquivo (diretório raiz do repositório)
TARGET_PATH = os.path.basename(FILE_PATH)

# Autenticar no GitHub
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

# Ler o conteúdo do arquivo local
with open(FILE_PATH, "rb") as file:
    content = file.read()

# Subir o arquivo no repositório
try:
    repo.create_file(
        path=TARGET_PATH,  # Caminho no repositório
        message=f"Adicionando o arquivo {TARGET_PATH}",  # Mensagem do commit
        content=content.decode("utf-8")  # Conteúdo do arquivo
    )
    print(f"Arquivo '{FILE_PATH}' enviado com sucesso para o repositório!")
except Exception as e:
    print(f"Erro ao enviar o arquivo: {e}")
  
