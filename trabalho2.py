def hanoi(n, origem, destino, auxiliar):


    # CASO BASE: O menor sub-problema (n=1)
    # Se há apenas um disco, basta movê-lo diretamente da Origem para o Destino.
    if n == 1:
        # A recursão para aqui e imprime o movimento final.
        print(f"Mover disco 1 de {origem} para {destino}") 
        return
    
    # PASSO RECURSIVO 1: Mover N-1 discos (Origem -> Auxiliar)
    # O problema se reduz: movemos N-1 discos para o pino auxiliar, 
    # usando o destino final como pino temporário.
    hanoi(n - 1, origem, auxiliar, destino)
    
    # MOVIMENTO DO DISCO MAIOR
    # Movemos o disco N (o maior) da Origem para o Destino.
    # Isso só é possível porque os N-1 discos menores estão fora do caminho (no auxiliar).
    print(f"Mover disco {n} de {origem} para {destino}")
    
    # PASSO RECURSIVO 2: Mover N-1 discos (Auxiliar -> Destino)
    # O problema se reduz novamente: movemos os N-1 discos do auxiliar para o destino,
    # usando a origem original como pino temporário.
    hanoi(n - 1, auxiliar, destino, origem)

n_discos = 3
print(f" Solução para {n_discos} discos ")
hanoi(n_discos, 'A', 'C', 'B')

# Saída esperada: 7 movimentos
# Mover disco 1 de A para C
# Mover disco 2 de A para B
# Mover disco 1 de C para B
# Mover disco 3 de A para C
# Mover disco 1 de B para A
# Mover disco 2 de B para C
# Mover disco 1 de A para C