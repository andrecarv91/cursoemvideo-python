expr = str(input('Digite a expressão: '))
pilha = []
for char in expr:
    if char == '(':
        pilha.append('(')
    elif char == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
print('Expressão válida!') if len(pilha) == 0 else print('Expressão inválida!')
