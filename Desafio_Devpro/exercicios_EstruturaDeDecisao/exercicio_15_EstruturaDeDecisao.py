"""
15 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem
ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
    
"""

while True:
    
    try:
                
        lado_a = float(input('Entre com o valor para o primeiro lado do triângulo: '))
        lado_b = float(input('Entre com o valor para o segundo lado do triângulo: '))
        lado_c = float(input('Entre com o valor para o terceiro lado do triângulo: '))
        
        if lado_a + lado_b < lado_c or lado_a > lado_b + lado_c or lado_a + lado_c < lado_b: 
            triangulo = 'Não é um triângulo'
        else:
            if lado_a == lado_b == lado_c:
                triangulo = 'Triângulo Equilátero'
            elif lado_a == lado_b or lado_b == lado_c or lado_c == lado_a:
                triangulo = 'Triângulo Isósceles'
            else:
                triangulo = 'Triângulo Escaleno'
        
        print(f'{triangulo}')
        break
    
    except ValueError:
        print('Entrada inválida')    
    

    