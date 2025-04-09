from flask import Flask, render_template, request, redirect
import mysql.connector
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="gustavo",  
        password="45878329", 
        database="tarefas"
    )


def carregar_tarefas():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, grau, descricao, imagem FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    return tarefas


def adicionar_tarefa(nome, grau, descricao, imagem):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tarefas (nome, grau, descricao, imagem) VALUES (%s, %s, %s, %s)",
        (nome, grau, descricao, imagem)
    )
    conn.commit()
    conn.close()


def editar_tarefa(id, grau, descricao):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tarefas SET grau = %s, descricao = %s WHERE id = %s",
        (grau, descricao, id)
    )
    conn.commit()
    conn.close()


def excluir_tarefa(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = %s", (id,))
    conn.commit()
    conn.close()


@app.route('/tarefas')
def listar_tarefas():
    tarefas = carregar_tarefas()
    return render_template("tarefas.html", tarefas=tarefas)


@app.route('/adicionar_tarefa', methods=['POST'])
def adicionar_tarefa_route():
    nome = request.form['nome']
    grau = request.form['grau']
    descricao = request.form['descricao']
    imagem = request.files['imagem']

    
    caminho_imagem = ""
    if imagem:
        filename = imagem.filename
        caminho_imagem = os.path.join(UPLOAD_FOLDER, filename)
        with open(caminho_imagem, "wb") as f:
            f.write(imagem.read())
        caminho_imagem = f"uploads/{filename}"

    adicionar_tarefa(nome, grau, descricao, caminho_imagem)
    return redirect('/tarefas')


@app.route('/editar_tarefa/<int:id>', methods=['POST'])
def editar_tarefa_route(id):
    grau = request.form['grau']
    descricao = request.form['descricao']
    editar_tarefa(id, grau, descricao)
    return redirect('/tarefas')


@app.route('/excluir_tarefa/<int:id>', methods=['POST'])
def excluir_tarefa_route(id):
    excluir_tarefa(id)
    return redirect('/tarefas')

@app.route('/form_tarefas')
def form_tarefa():
    return render_template("form_tarefas.html")

if __name__ == "__main__":
    app.run(debug=True)