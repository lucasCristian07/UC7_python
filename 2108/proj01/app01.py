from flask import Flask, render_template, request

class app01():
    def __init__(self):
        self.app = Flask(__name__)
        self.defineRotas()

    def defineRotas(self):
        @self.app.route('/')
        def rotainicial():
            return 'rota que começa nesse krai'
        
        @self.app.route('/index')
        def rotaindex():
            return render_template('/index.html')
        
        @self.app.route('/exe1')
        def exe1():
            return render_template('/exe1.html')

        # @self.app.route('/exe1_submit', methods=['POST'])
        # def exe1():
        #     if request.method == 'POST':
        #         nota = request.form.get('nota')
        #         if nota and nota.isdigit() and 0 <= int(nota) <= 10:
        #             return 'Finalmente um valor válido!!'
        #         else:
        #             return render_template('exe1.html', mensagem='Valor inválido. Por favor, informe uma nota entre 0 e 10.')
        #     return render_template('exe1.html')
                     # ⬆️ARRUMAR O CODIGO!!!!
            # exe2
        @self.app.route('/exe2')            
        def exe2():
            return render_template('/exe2.html')
        
        @self.app.route('/exe2', methods=['POST'])
        def exe02():
            if request.method == 'POST':
                nome = request.form.get('nome')
                senha = request.form.get('senha')
                if nome == 'lukinhas do grau 244' and senha == '123':
                    return f'Olá, {nome}, seja bem vindo!'
                else:
                    return render_template('exe2.html', mensagem='Usuário ou senha inválida')
            return render_template('exe2.html')
        
            # DESAFIO3
        @self.app.route('/exe3')
        def exe3():
            return render_template('/exe3.html')
        
        @self.app.route('/exe3' , methods=['POST'])
        def desafio03():
            if request.method == 'POST':
                num1 = int(request.form.get('num1'))
                num2 = int(request.form.get('num2'))
                if num1 < num2:
                    intervalo = list(range(num1 + 1, num2))
                    return render_template('exe3.html', intervalo=intervalo)
                else:
                    return render_template('exe3.html', mensagem='O primeiro número deve ser menor que o segundo')
            return render_template('exe3.html')
        
        #DESAFIO4
        @self.app.route('/exe4')
        def desafio04():
            return render_template('/exe4.html')

        @self.app.route('/exe4', methods=['POST'])
        def desafio04_post():
            if request.method == 'POST':
                num1 = int(request.form.get('num1'))
                num2 = int(request.form.get('num2'))
                if num1 <= num2:
                    soma = sum(range(num1, num2 + 1))
                    return render_template('exe4.html', soma=soma, num1=num1, num2=num2)
                else:
                    return render_template('exe4.html', mensagem='O primeiro número deve ser menor ou igual ao segundo')
            return render_template('exe4.html')    
        
        #desafio5
        @self.app.route('/exe5')
        def desafio05():
            return render_template('/exe5.html')

        @self.app.route('/exe5', methods=['POST'])
        def desafio05_post():
            if request.method == 'POST':
                num = int(request.form.get('num'))
                if 1 <= num <= 10:
                    tabuada = [f'{num} X {i} = {num * i}' for i in range(1, 11)]
                    return render_template('exe5.html', tabuada=tabuada, num=num)
                else:
                    return render_template('exe5.html', mensagem='O número deve estar entre 1 e 10')
            return render_template('exe5.html')        



        # DESAFIO6
        @self.app.route('/exe6')
        def desafio06():
            return render_template('/exe6.html')

        @self.app.route('/exe6', methods=['POST'])
        def desafio06_post():
            if request.method == 'POST':
                num1 = int(request.form.get('num1'))
                num2 = int(request.form.get('num2'))
                num3 = int(request.form.get('num3'))
                num4 = int(request.form.get('num4'))
                num5 = int(request.form.get('num5'))
                num6 = int(request.form.get('num6'))
                numeros = [num1, num2, num3, num4, num5, num6]
                soma_negativos = sum([num for num in numeros if num < 0])
                multiplicacao_positivos = 1
                for num in numeros:
                    if num > 0:
                        multiplicacao_positivos *= num
                quantidade_zeros = sum([1 for num in numeros if num == 0])
                return render_template('exe6.html', soma_negativos=soma_negativos, multiplicacao_positivos=multiplicacao_positivos, quantidade_zeros=quantidade_zeros)
            return render_template('exe6.html')       


            #DESAFIO7
        @self.app.route('/exe7')
        def desafio07():
            return render_template('/exe7.html')

        @self.app.route('/exe7', methods=['POST'])
        def desafio07_post():
            if request.method == 'POST':
                frase = request.form.get('frase')
                palavras = frase.split()
                quantidade_palavras = len(palavras)
                return render_template('exe7.html', quantidade_palavras=quantidade_palavras)
            return render_template('exe7.html')

#DESAFIO8
        @self.app.route('/exe8')
        def desafio08():
            return render_template('/exe8.html')

        @self.app.route('/exe8', methods=['POST'])
        def desafio08_post():
            if request.method == 'POST':
                num1 = int(request.form.get('num1'))
                num2 = int(request.form.get('num2'))
                num3 = int(request.form.get('num3'))
                num4 = int(request.form.get('num4'))
                num5 = int(request.form.get('num5'))
                num6 = int(request.form.get('num6'))
                num7 = int(request.form.get('num7'))
                num8 = int(request.form.get('num8'))
                numeros = [num1, num2, num3, num4, num5, num6, num7, num8]

                quantidade_pares = sum([1 for num in numeros if num % 2 == 0])
                soma_impares = sum([num for num in numeros if num % 2 != 0])

                def eh_primo(n):
                    if n <= 1:
                        return False
                    for i in range(2, int(n ** 0.5) + 1):
                        if n % i == 0:
                            return False
                    return True

                numeros_primos = [num for num in numeros if eh_primo(num)]
                multiplicacao_primos = 1
                for num in numeros_primos:
                    multiplicacao_primos *= num

                return render_template('exe8.html', quantidade_pares=quantidade_pares, soma_impares=soma_impares, multiplicacao_primos=multiplicacao_primos)
            return render_template('exe8.html')
       

        #DESAFIO9
        @self.app.route('/exe9')
        def desafio09():
            return render_template('/exe9.html')

        @self.app.route('/exe9', methods=['POST'])
        def desafio09_post():
            if request.method == 'POST':
                frase = request.form.get('frase')
                vogais = 'aeiouAEIOU'
                quantidade_vogais = sum([1 for char in frase if char in vogais])
                return render_template('exe9.html', quantidade_vogais=quantidade_vogais)
            return render_template('exe9.html')           

        #DESAFIO10  
        @self.app.route('/exe10')
        def desafio10():
            return render_template('/exe10.html')

        @self.app.route('/exe10', methods=['POST'])
        def desafio10_post():
            if request.method == 'POST':
                numeros = request.form.get('numeros')
                numeros = list(map(int, numeros.split(',')))
                menor_valor = min(numeros)
                maior_valor = max(numeros)
                soma_valores = sum(numeros)
                return render_template('exe10.html', menor_valor=menor_valor, maior_valor=maior_valor, soma_valores=soma_valores)
            return render_template('exe10.html')         


        #DESAFIO11
        @self.app.route('/exe11')
        def desafio11():
            return render_template('/exe11.html')

        @self.app.route('/exe11', methods=['POST'])
        def desafio11_post():
            if request.method == 'POST':
                num = int(request.form.get('num'))
                if num <= 1:
                    return render_template('exe11.html', mensagem='O número deve ser maior que 1')
                elif num == 2:
                    return render_template('exe11.html', mensagem='O número é primo')
                else:
                    for i in range(2, int(num ** 0.5) + 1):
                        if num % i == 0:
                            return render_template('exe11.html', mensagem='O número não é primo')
                    return render_template('exe11.html', mensagem='O número é primo')
            return render_template('exe11.html')        
        

        #DESAFIO12
        @self.app.route('/exe12')
        def desafio12():
            return render_template('/exe12.html')

        @self.app.route('/exe12', methods=['POST'])
        def desafio12_post():
            if request.method == 'POST':
                num = int(request.form.get('num'))
                if num <= 1:
                    return render_template('exe12.html', mensagem='O número deve ser maior que 1')
                divisores = [i for i in range(1, num + 1) if num % i == 0]
                return render_template('exe12.html', num=num, divisores=divisores)
            return render_template('exe12.html')     



        #DESAFIO13
        @self.app.route('/exe13')
        def desafio13():
            return render_template('/exe13.html')

        @self.app.route('/exe13', methods=['POST'])
        def desafio13_post():
            if request.method == 'POST':
                num = int(request.form.get('num'))
                if num <= 10:
                    return render_template('exe13.html', mensagem='O número deve ser maior que 10')
                primos = []
                for i in range(10, num + 1):
                    if i > 1:
                        for j in range(2, int(i ** 0.5) + 1):
                            if i % j == 0:
                                break
                        else:
                            primos.append(i)
                return render_template('exe13.html', num=num, primos=primos)
            return render_template('exe13.html')           



        # desafio14
        @self.app.route('/exe14')
        def desafio14():
            return render_template('/exe14.html')

        @self.app.route('/exe14', methods=['POST'])
        def desafio14_post():
            if request.method == 'POST':
                num = int(request.form.get('num'))
                inicial = int(request.form.get('inicial'))
                final = int(request.form.get('final'))
                if inicial > final:
                    return render_template('exe14.html', mensagem='O valor inicial deve ser menor ou igual ao valor final')
                tabuada = [f'{num} X {i} = {num * i}' for i in range(inicial, final + 1)]
                return render_template('exe14.html', num=num, inicial=inicial, final=final, tabuada=tabuada)
            return render_template('exe14.html')
                
if __name__ == '__main__':
    MeuApp = app01()
    MeuApp.app.run(debug=True)