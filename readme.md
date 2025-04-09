Projeto de Gerenciamento de Tarefas com Flask
Sistema web simples para gerenciamento de tarefas, utilizando Python e Flask. O projeto possui duas versões:

Versão com armazenamento em arquivo CSV

Versão com banco de dados MySQL

Funcionalidades
Listar tarefas

Adicionar nova tarefa com imagem

Editar grau e descrição da tarefa

Excluir tarefa

Upload de imagem para cada tarefa

Endpoints da Aplicação
Método	Rota	Descrição
GET	/tarefas	Exibe a lista de tarefas
GET	/form_tarefas	Formulário para adicionar uma nova tarefa
POST	/adicionar_tarefa	Adiciona uma nova tarefa
GET	/editar_tarefa/<id ou nome>	Formulário para editar tarefa (GET)
POST	/editar_tarefa/<id ou nome>	Salva as alterações de uma tarefa
POST	/excluir_tarefa/<id ou nome>	Exclui a tarefa indicada
GET	/uploads/<path:filename>	Retorna uma imagem da pasta de uploads
Observação:

Na versão com CSV, os parâmetros de edição e exclusão são baseados no campo nome.

Na versão com MySQL, os parâmetros são baseados no campo id (inteiro e único).

Como executar
1. Clone o projeto
bash
Copiar
Editar
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto
Versão com CSV
Executar
bash
Copiar
Editar
python app_csv.py
Estrutura esperada
diff
Copiar
Editar
- app_csv.py
- tarefas.csv
- uploads/
- templates/
    - tarefas.html
    - form_tarefas.html
    - editar_tarefa.html
Versão com MySQL
Requisitos
MySQL Server

Tabela:

sql
Copiar
Editar
CREATE DATABASE tarefas;
USE tarefas;

CREATE TABLE tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    grau VARCHAR(255),
    descricao TEXT,
    imagem VARCHAR(255)
);
Instalar dependências
bash
Copiar
Editar
pip install flask mysql-connector-python
Configurar conexão
No app_mysql.py, edite:

python
Copiar
Editar
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="tarefas"
    )
Executar
bash
Copiar
Editar
python app_mysql.py
Uploads
A pasta uploads/ armazena as imagens associadas às tarefas. Ela é criada automaticamente se não existir.

Templates HTML
Arquivos HTML utilizados:

tarefas.html

form_tarefas.html

editar_tarefa.html

#   T O - D O - F l a s k  
 