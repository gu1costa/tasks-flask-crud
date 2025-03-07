from flask import Flask   #classe do flask usada para criar a aplicação

#__name__ = "__main__"  quando executado de forma manual.
app = Flask(__name__) 

#rota com os clientes, permitindo receber informações e devolve-las para quem está socilitando
@app.route("/")  #método route. parâmetro endpoint. "/" representa a rota inicial/local.
def hello_world():    #o que va ser executado ao acessar a rota.
    return "Hello world!"

@app.route("/about")
def about():
    return "Página sobre."

if __name__ == "__main__":
    app.run(debug=True)   #método run com a propriedade debug como parâmetro. o debug ajuda  a  viualizar informações sobre o que está acontecendo no servidor web. recomendado apenas para desenvolvimento local.

#rotas são a ponte de acesso com outros programas ou usuários que estão acessando determinada informação.

#registro de requisição: ip / dia e horário / protocolo (get/http) / código da requisição.