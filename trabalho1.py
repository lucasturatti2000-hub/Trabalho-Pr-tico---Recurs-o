def busca_binaria(lista, valor, inicio, fim):
    #CASO BASE DE FALHA: A sub-lista está vazia
    if inicio > fim:
        return -1  
    
    # Calcula o índice do meio
    meio = (inicio + fim) // 2
    
    # CASO BASE DE SUCESSO: O valor foi encontrado
    if lista[meio] == valor:
        return meio  
    
    # PASSO RECURSIVO (Busca na sub-lista esquerda)
    # Se o valor for menor, ajusta o 'fim' para (meio - 1)
    elif valor < lista[meio]:
        return busca_binaria(lista, valor, inicio, meio - 1) 
        
    # PASSO RECURSIVO (Busca na sub-lista direita)
    # Se o valor for maior, ajusta o 'inicio' para (meio + 1)
    else:
        return busca_binaria(lista, valor, meio + 1, fim) 

# Lista de números ordenada (Requisito essencial para Busca Binária)
nums = [2, 4, 6, 8, 10, 12, 14]
valor_procurado = 10
inicio_lista = 0
fim_lista = len(nums) - 1

# Chamada da função
indice_encontrado = busca_binaria(nums, valor_procurado, inicio_lista, fim_lista)

# Imprimindo o resultado
print(f"Lista: {nums}")
print(f"Valor buscado: {valor_procurado}")
print(f"Resultado da busca binária: {indice_encontrado}")

# Teste para um valor que não está na lista (Ex: 5)
valor_nao_encontrado = 5
indice_falha = busca_binaria(nums, valor_nao_encontrado, inicio_lista, fim_lista)
print(f"Valor buscado: {valor_nao_encontrado}")
print(f"Resultado da busca binária: {indice_falha}") # Saída: -1