import pytest
import requests

#CRUD
BASE_URL = "http://127.0.0.1:5000"
tasks = []

#Create
def test_create_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa."
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)   #o método post vem da biblioteca requests.
    assert response.status_code == 200 #para "quebrar" o teste.
    response_json = response.json() #corpo do retorno.
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json["id"])

#Read
def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks") #não precisa definir json por conta que não a estrutura não tem nenhum corpo
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

#validando tarefa específica
def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200 #o teste só será bem sucedido se...
        response_json = response.json() #recupera o corpo da resposta.
        assert task_id == response_json["id"] #o id da task tem que ser igual ao id do corpo da resposta.

#Update
def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "completed": True,
            "description": "Nova descrição",
            "title": "Título atualizado."
        }

        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)  #enviando requisição
        response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        #nova requisição a tarefa específica
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200 
        response_json = response.json()
        assert response_json["title"] == payload["title"]
        assert response_json["description"] == payload["description"]
        assert response_json["completed"] == payload["completed"]

 #Delete
def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        response.status_code == 200

        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404