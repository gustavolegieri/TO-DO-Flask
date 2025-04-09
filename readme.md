# Projeto de Gerenciamento de Tarefas com Flask

Este é um sistema web simples para gerenciamento de tarefas, feito com Python e Flask. O projeto possui duas versões:

- Versão que usa um arquivo CSV para armazenar os dados
- Versão que usa um banco de dados MySQL.

## Funcionalidades

- Listar tarefas
- Adicionar nova tarefa com imagem
- Editar grau e descrição da tarefa
- Excluir tarefa
- Fazer upload de imagem para cada tarefa

## Como executar

### 1. Clone o projeto

```bash

git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto

```

---

## Versão com CSV

### Executar

```bash

python app_csv.py

```

### Estrutura esperada

```

- app_csv.py
- tarefas.csv (será criado automaticamente)
- uploads/ (pasta onde ficam as imagens)
- templates/
    - tarefas.html
    - form_tarefas.html
    - editar_tarefa.html

```

---

## Versão com MySQL

### Pré-requisitos

- MySQL Server instalado e rodando
- Banco de dados e tabela criados com o seguinte comando:

```sql

CREATE DATABASE tarefas;
USE tarefas;

CREATE TABLE tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    grau VARCHAR(255),
    descricao TEXT,
    imagem VARCHAR(255)
);

```

### Instalar dependências

```bash

pip install flask mysql-connector-python

```

### Configurar conexão com banco

Edite a função get_db_connection() no arquivo app_mysql.py com os seus dados:

```python

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="tarefas"
    )

```

### Executar

```bash

python app_mysql.py

```

---

## Uploads

As imagens enviadas são salvas na pasta uploads. Ela é criada automaticamente se não existir.

---

## Templates HTML

Os arquivos HTML devem estar na pasta templates:

- tarefas.html: exibe a lista de tarefas
- form_tarefas.html: formulário para adicionar tarefa
- editar_tarefa.html: formulário para editar tarefa