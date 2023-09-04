"""
lista comprehension - Compreensão de lista
Otimização - melhorar performa-se e não ocupar tanta memoria
"""
l1 = [1, 2, 3, 4, 5, 6, 7]
ex1 = [variavel for variavel in l1]  # Iteragindo na lista(l1), formando outra lista(ex1)
print(ex1)

ex2 = [v * 2 for v in l1]  # Iteragindo na lista, multiplicando os elementos, add em outra lista(ex2)
print(ex2)

ex3 = [(v, v2) for v in l1 for v2 in range(3)]  # Fazendo uma coordenada!
print(ex3)

l2 = ['Everton', 'Anna', 'Maria']
ex4 = [v.upper().replace('A', '@') for v in l2]  # Trocando os 'A' por '@'
print(ex4)

tupla = (('chave', 'valor'), ('chave2', 'valor2'))
ex5 = [(y, x) for x, y in tupla]  # Invertendo valores
ex5 = dict(ex5)
print(ex5)

l3 = list(range(100))
ex6 = [v for v in l3 if v % 2 == 0]  # Multiplos de 2
print(ex6)
ex6 = [v for v in l3 if v % 2 == 0 if v % 5 == 0]  # Multiplos de 2 e 5
print(ex6)

ex7 = [v if v % 3 == 0 and v % 7 == 0 else 0 for v in l3]  # ultilizando else
print(ex7)
