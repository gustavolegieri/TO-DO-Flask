from flask import Flask, render_template, request, redirect, send_from_directory
import csv
import os

app = Flask(__name__)

arquivo = "tarefas.csv"
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Carregar tarefas do CSV
def carregar_tarefas():
    tarefas = []
    if not os.path.exists(arquivo):
        with open(arquivo, "w", encoding="utf-8", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Nome", "Grau", "Descrição", "Imagem"])
    try:
        with open(arquivo, "r", encoding="utf-8", newline='') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                tarefas.append(row)
    except Exception as e:
        print(f"Erro ao carregar tarefas: {e}")
    return tarefas

# Salvar tarefas no CSV
def salvar_tarefas(tarefas):
    try:
        with open(arquivo, "w", encoding="utf-8", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Nome", "Grau", "Descrição", "Imagem"])
            writer.writerows(tarefas)
    except Exception as e:
        print(f"Erro ao salvar tarefas: {e}")

# Gerar novo ID
def gerar_id(tarefas):
    if not tarefas:
        return 1
    ids = [int(t[0]) for t in tarefas]
    return max(ids) + 1

# Adicionar tarefa com ID
def adicionar_tarefa(nome, grau, descricao, caminho_imagem):
    tarefas = carregar_tarefas()
    novo_id = gerar_id(tarefas)
    tarefas.append([novo_id, nome, grau, descricao, caminho_imagem])
    salvar_tarefas(tarefas)

@app.route('/tarefas')
def listar_tarefas():
    tarefas = carregar_tarefas()
    return render_template("tarefas.html", tarefas=tarefas)

@app.route('/form_tarefas')
def form_tarefa():
    return render_template("form_tarefas.html")

@app.route('/adicionar_tarefa', methods=['POST'])
def adicionar_tarefa_route():
    nome = request.form['nome']
    grau = request.form['grau']
    descricao = request.form['descricao']
    imagem = request.files['imagem']

    caminho_imagem = ""
    if imagem and imagem.filename != "":
        filename = imagem.filename
        caminho_imagem = os.path.join(UPLOAD_FOLDER, filename)
        imagem.save(caminho_imagem)
        caminho_imagem = f"{UPLOAD_FOLDER}/{filename}"

    adicionar_tarefa(nome, grau, descricao, caminho_imagem)
    return redirect('/tarefas')

@app.route('/editar_tarefa/<int:id>', methods=['GET', 'POST'])
def editar_tarefa(id):
    tarefas = carregar_tarefas()
    for tarefa in tarefas:
        if int(tarefa[0]) == id:  
            if request.method == 'POST':
                tarefa[2] = request.form['grau']
                tarefa[3] = request.form['descricao']
                salvar_tarefas(tarefas)
                return redirect('/tarefas')
            return render_template("editar_tarefa.html", tarefa=tarefa)
    return redirect('/tarefas')

@app.route('/excluir_tarefa/<int:id>', methods=['POST'])
def excluir_tarefa(id):
    tarefas = carregar_tarefas()
    tarefas = [tarefa for tarefa in tarefas if int(tarefa[0]) != id]
    salvar_tarefas(tarefas)
    return redirect('/tarefas')

@app.route('/uploads/<path:filename>')
def uploads(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
