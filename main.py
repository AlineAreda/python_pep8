from fabrica_fila import FabricaFila
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada


teste_fabrica = FabricaFila.pega_fila('prioritaria')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(8))
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.chama_cliente(11))
print(teste_fabrica.estatistica(EstatisticaResumida('06/04/2024', 500)))
