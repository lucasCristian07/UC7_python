from flask import Flask, render_template, request

class proj01:
    def __init__(self):
        self.app = Flask(__name__)

        #rota inicial
        @self.app.route('/')
        def index02():
            return render_template('index02.html')
        #------------------
        # @self.app.route('/exe01')
        # def exe01():
        #     return "inicio do exercicio 01"
        # @self.app.route('/exe02')
        # def exe02():
        #     return "agora eu entendi!!!"
        #rota que recebe dados do front-end index.html
        @self.app.route('/acao', methods=['POST'])
        def acao():
            numero1 = request.form.get('number1')
            numero2 = request.form.get('number2')

            soma = int(numero1) + int(numero2)
            return f"a soma é: {soma}"
            
        
if __name__ == '__main__':
    MeuApp = proj01()
    MeuApp.app.run(debug=True)