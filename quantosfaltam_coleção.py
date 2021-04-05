x = []
y = []
alpha = 0
b=int(input('diga o tamanho da coleção: '))

while alpha != 'S':
    alpha = input('digite o novo valor ou pare apertando S: ')
    if alpha != 'S':
        alpha = int(alpha)
        if alpha <= b:
            x.append(alpha)
            print('Atualmente o tamanho da array é: ', len(x), 'e ela totalmente é: ', x)
        else:
            print('insira um valor menor ou igual a', b, '!')

x.sort()
print('a lista completa é:\n')
print(x)

for j in range (b):
    y.append(int(j+1))


for element in x:
    if element in y:
        y.remove(element)

print('\nOs números faltantes são:\n')
print(y)