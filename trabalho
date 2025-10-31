# Solicita um número inteiro ao usuário para calcular o fatorial
numero = int(input("digite um número: "))

# Define a função recursiva para calcular o fatorial
def fatorial(numero):
    # CASO BASE: Condição que encerra a recursão.
    # O fatorial de 0 e 1 é, por definição, igual a 1.
    if numero == 0 or numero == 1:
        # Quando a função chega aqui, ela para de chamar a si mesma e retorna 1.
        return 1 
    
    # PASSO RECURSIVO: A função se chama para resolver um subproblema.
    else:
        # Retorna o número atual (n) multiplicado pelo fatorial do número anterior (n-1).
        # Este é o ponto onde a função chama a si mesma, empilhando a operação de multiplicação.
        return numero * fatorial(numero - 1)
    
# Chama a função 'fatorial' com o número fornecido e armazena o resultado.

resultado_fatorial = fatorial(numero)

# Imprime o resultado formatado.
print(f"O fatorial de {numero} é {resultado_fatorial}")

# Exemplo de rastreio (comentado) para n=4:
# 1. fatorial(4) chama 4 * fatorial(3)
# 2. fatorial(3) chama 3 * fatorial(2)
# 3. fatorial(2) chama 2 * fatorial(1)
# 4. fatorial(1) retorna 1 (CASO BASE)
# 5. fatorial(2) resolve: 2 * 1 = 2
# 6. fatorial(3) resolve: 3 * 2 = 6
# 7. fatorial(4) resolve: 4 * 6 = 24 (RESULTADO FINAL)




