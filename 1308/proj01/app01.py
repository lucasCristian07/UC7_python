from flask import Flask, render_template, request

class app01():
    def __init__(self):
        self.app = Flask(__name__)
        self.defineRotas()
    
    def defineRotas(self):
        @self.app.route('/')
        def rotainicial():
            return 'esta é a rota inicial'
    
        @self.app.route('/exe01')
        def rotaexe01():
            return render_template('index.html')
        
        @self.app.route('/form01')
        def rotaform01():
            return render_template('form01.html')
        
        @self.app.route('/form01_submit', methods=['POST'])
        def rotadorm01_submit():
            nome = request.form.get('nome')
            return f'Ola {nome}'
        
        @self.app.route('/proj03')
        def proj03():
            return render_template('proj03.html')
        
        @self.app.route('/rotaCalc_submit', methods=['POST'])
        def rotaCalc__submit():
            n1 = request.form.get('n1')
            n2 = request.form.get('n2')
            n1 = n1.replace(',', '.')
            n2 = n2.replace(',', '.')
            soma = float(n1) + float(n2)
            soma = f'{soma:.2f}'
            soma = soma.replace(".", ",")
            return f'O resultado da soma é {soma}'

if __name__ == '__main__':
    MeuApp = app01()
    MeuApp.app.run(debug=True)