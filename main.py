from fabrica_fila import FabricaFila

teste_fabrica = FabricaFila.pega_fila('normal')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(8))
# print(fila_teste.estatisticas('21/03/2024', 341, 'detail'))
