from fila_prioritaria import FilaPrioritaria
from fila_normal import FilaNormal

fila_teste = FilaPrioritaria()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
print(fila_teste.chama_cliente(5))
print(fila_teste.chama_cliente(8))
print(fila_teste.estatisticas('21/03/2024', 341, 'detail'))
