from flask import Flask, render_template, request

class app01():
    def __init__(self):
        self.app = Flask(__name__)
        self.defineRotas()

    def defineRotas(self):
        @self.app.route('/')
        def rotainicial():
            return '/rota que começa nesse krai'
        
        @self.app.route('/index')
        def index():
            return render_template('/index.html')
        
        # desafio 1
        @self.app.route('/desafio1')
        def desafio1():
            return render_template('desafio1.html')
        
        @self.app.route('/desafio1_submit', methods=['POST'])
        def desafio1_submit():
            n1 = int(request.form.get('numero1'))
            n2 = int(request.form.get('numero2'))
            maior = max(n1, n2)
            return f'O maior número é: {maior}'
        
        # desafio 2
        @self.app.route('/desafio2')
        def desafio2():
            return render_template('desafio2.html')

        @self.app.route('/desafio2_submit', methods=['POST'])
        def desafio02():
            if request.method == 'POST':
                valor = float(request.form['valor'])
                if valor > 0:
                    resultado = 'O valor é positivo!'
                elif valor < 0:
                    resultado = 'O valor é negativo!'
                else:
                    resultado = 'O valor é zero!'
                return render_template('desafio2.html', resultado=resultado)
            return render_template('desafio2.html')
        
        #desafio3
        # @self.app.route('/desafio3')
        # def desafio03():
        #     return render_template('desafio3.html')
        
        # @self.app.route('/desafio3_submit', methods=['POST'])
        # def desafio03():
        #     if request.method == 'POST':
        #         letra = request.form['letra'].upper()
        #         if letra == 'F':
        #             resultado = 'Feminino'
        #         elif letra == 'M':
        #             resultado = 'Masculino'
        #         else:
        #             resultado = 'Outro'
        #         return render_template('desafio3.html', resultado=resultado)
        #     return render_template('desafio3.html')

            # ⬆️ARRUMAR O CODIGO!!!!

        # desafio4
        @self.app.route('/desafio4')
        def desafio4():
            return render_template('desafio4.html')
        
        @self.app.route('/desafio4_submit', methods=['POST'])
        def desafio04():
            if request.method == 'POST':
                letra = request.form['letra'].lower()
                vogais = 'aeiou'
                if letra in vogais:
                    resultado = 'Vogal'
                elif letra.isalpha():
                    resultado = 'Consoante'
                else:
                    resultado = 'Não é uma letra'
                return render_template('desafio4.html', resultado=resultado)
            return render_template('desafio4.html')  

        # desafio5
        @self.app.route('/desafio5')
        def desafio():
            return render_template('desafio5.html')
        
        @self.app.route('/desafio5', methods=['POST'])
        def desafio05():
            if request.method == 'POST':
                nota1 = float(request.form['nota1'])
                nota2 = float(request.form['nota2'])
                media = (nota1 + nota2) / 2
                if media == 10:
                    resultado = 'Aprovado com Distinção'
                elif media >= 7:
                    resultado = 'Aprovado'
                elif media >= 4:
                    resultado = 'Recuperação'
                else:
                    resultado = 'Reprovado'
                return render_template('desafio5.html', resultado=resultado)
            return render_template('desafio5.html')
        
        # @self.app.route('/desafio6')
        # def desafio06():
        #     return render_template('desafio6.html')

        # @self.app.route('/desafio6', methods=['POST'])
        # def desafio06():
        #     if request.method == 'POST':
        #         num1 = float(request.form['num1'])
        #         num2 = float(request.form['num2'])
        #         num3 = float(request.form['num3'])
        #         maior = max(num1, num2, num3)
        #         return render_template('desafio6.html', resultado=f'O maior número é {maior}')
        #     return render_template('desafio6.html')

                # ⬆️ARRUMAR O CODIGO!!!!

# DESAFIO7
        @self.app.route('/desafio7')
        def desafio07():
            return render_template('/desafio7.html')

        @self.app.route('/desafio7', methods=['POST'])
        def desafio07_post():
            if request.method == 'POST':
                num1 = int(request.form.get('num1'))
                num2 = int(request.form.get('num2'))
                num3 = int(request.form.get('num3'))
                num4 = int(request.form.get('num4'))
                numeros = [num1, num2, num3, num4]
                maior = max(numeros)
                menor = min(numeros)
                return render_template('desafio7.html', maior=maior, menor=menor)
            return render_template('desafio7.html')            

# DESAFIO8
        @self.app.route('/desafio8')
        def desafio08():
            return render_template('/desafio8.html')

        @self.app.route('/desafio8', methods=['POST'])
        def desafio08_post():
            if request.method == 'POST':
                nome1 = request.form.get('nome1')
                preco1 = float(request.form.get('preco1'))
                nome2 = request.form.get('nome2')
                preco2 = float(request.form.get('preco2'))
                nome3 = request.form.get('nome3')
                preco3 = float(request.form.get('preco3'))
                produtos = [(nome1, preco1), (nome2, preco2), (nome3, preco3)]
                mais_barato = min(produtos, key=lambda x: x[1])
                return render_template('desafio8.html', mais_barato=mais_barato[0])
            return render_template('desafio8.html')



# DESAFIO9
        @self.app.route('/desafio9')
        def desafio09():
            return render_template('/edesafio.html')

        @self.app.route('/desafio9', methods=['POST'])
        def desafio09_post():
            if request.method == 'POST':
                num1 = int(request.form.get('num1'))
                num2 = int(request.form.get('num2'))
                num3 = int(request.form.get('num3'))
                numeros = [num1, num2, num3]
                numeros.sort(reverse=True)
                return render_template('desafio9.html', numeros=numeros)
            return render_template('desafio9.html') 
        


# DESAFIO10
        @self.app.route('/desafio10')
        def desafio10():
            return render_template('/desafio10.html')

        @self.app.route('/desafio10', methods=['POST'])
        def desafio10_post():
            if request.method == 'POST':
                num1 = int(request.form.get('num1'))
                num2 = int(request.form.get('num2'))
                num3 = int(request.form.get('num3'))
                numeros = [num1, num2, num3]
                numeros.sort()
                return render_template('desafio10.html', numeros=numeros)
            return render_template('desafio10.html')    

# DESAFIO11
        # @self.app.route('/desafio11')
        # def desafio11():
        #     return render_template('/desafio11.html')

        # @self.app.route('desafio11', methods=['POST'])
        # def desafio11_post():
        #     if request.method == 'POST':
        #         turno = request.form.get('turno').upper()
        #         if turno == 'M':
        #             return render_template('desafio11.html', mensagem='Bom Dia!')
        #         elif turno == 'V':
        #             return render_template('desafio11.html', mensagem='Boa Tarde!')
        #         elif turno == 'N':
        #             return render_template('desafio11.html', mensagem='Boa Noite!')
        #         else:
        #             return render_template('desafio11.html', mensagem='Valor Inválido!')
        #     return render_template('desafio11.html')   



# DESAFIO12
        @self.app.route('/desafio12')
        def desafio12():
            return render_template('/desafio12.html')

        @self.app.route('/desafio12', methods=['POST'])
        def desafio12_post():
            if request.method == 'POST':
                lado1 = int(request.form.get('lado1'))
                lado2 = int(request.form.get('lado2'))
                lado3 = int(request.form.get('lado3'))
                if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
                    if lado1 == lado2 == lado3:
                        return render_template('desafio12.html', mensagem='Triângulo Equilátero!')
                    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                        return render_template('desafio12.html', mensagem='Triângulo Isósceles!')
                    else:
                        return render_template('desafio12.html', mensagem='Triângulo Escaleno!')
                else:
                    return render_template('desafio12.html', mensagem='Não é um triângulo!')
            return render_template('desafio12.html')
        

# DESAFIO13
        @self.app.route('/desafio13')
        def desafio13():
            return render_template('/desafio13.html')

        @self.app.route('/desafio13', methods=['POST'])
        def desafio13_post():
            if request.method == 'POST':
                nome = request.form.get('nome')
                salario_atual = float(request.form.get('salario_atual'))
                if salario_atual <= 280:
                    percentual_aumento = 20
                elif salario_atual <= 700:
                    percentual_aumento = 15
                elif salario_atual <= 1500:
                    percentual_aumento = 10
                else:
                    percentual_aumento = 5
                valor_aumento = (salario_atual / 100) * percentual_aumento
                novo_salario = salario_atual + valor_aumento
                return render_template('desafio13.html', nome=nome, salario_atual=salario_atual, percentual_aumento=percentual_aumento, valor_aumento=valor_aumento, novo_salario=novo_salario)
            return render_template('desafio13.html')        
        
if __name__ == '__main__':    
    MeuApp = app01()
    MeuApp.app.run(debug=True)