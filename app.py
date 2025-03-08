from flask import Flask, request, jsonify #classe do flask usada para criar a aplicação
from models.task import Task

app = Flask(__name__) 

#CRUD
#CRUD = Create, Read, Update and Delete.
#Tabela: tarefa.

tasks = []
task_id_control = 1

#Create
@app.route("/tasks", methods=['POST']) #methos define o método HTTP
def create_task():
    global task_id_control #define o valor da variável dentro da função.
    data = request.get_json() #o request vem do Flask. o get_json recupera os dados inseridos pelo cliente. o data vira um dicionário com esses métodos
    print(data)
    new_task = Task(id= task_id_control, title=data["title"], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso."}) #jsonify vem do flask que transforma o conteúdo de um dicionário em json ou xml. as normas da API REST exigem que retorne json/xml

#Read
@app.route("/tasks", methods=['GET'])
def get_tasks():
    task_list = [] #não é possível utilizar a variável "task = []" do início do código por que ela está armazenando objetos da classe Task

    for task in tasks:
        task_list.append(task.to_dict()) #o to_dict retorna a task que está na lista como está no formato da classe Task.

    #forma alternativa: task_list = [task.to_dict() for task in tasks]

    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)

@app.route("/tasks/<int:id>", methods=["GET"]) #parâmetro: id do tipo inteiro. permite receber uma variável do usuário.
def get_task(id):
    task = None
    for t in tasks: #"t" é cada atividade dentro da lista tasks
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"message": "Não foi possível encontrar a atividade."}), 404 #404 significa não encontrado.

#Update
@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
        
    print(task)

    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso."})

#Delete
@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break #quebra o loop para não percorrer todas as verificações.

    if not task: #se não encontrar nenhuma task
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
        
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso."})

if __name__ == "__main__":
    app.run(debug=True)   