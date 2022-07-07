import pandas as pd
from raspagem_corona import RaspagemCorona, TratamentoDados, TratamentoGrafico

# Para rodar esse arquivo de teste, apenas é necessário executar 
# quando setado o prompt/cmder na pasta com o arquivo o comando 'pytest' 

# Testa os metodos relacionados a opção 'ler_excel' do programa principal

def test_ler_excel():
	# Testa se o método ler excel retorna um dataframe
	tratamento = TratamentoDados()
	df = tratamento.LerExcel()
	assert type(df) == pd.DataFrame

def test_ler_excel_delete():
	# Testa se a coluna 'Unnamed: 0' foi de fato apagada do df
	tratamento = TratamentoDados()
	df = tratamento.LerExcel()
	colunas_nome = list(df.columns)
	print(colunas_nome)
	assert ('Unnamed: 0' not in colunas_nome) == True

def test_porcentagem():
	# Testa se a soma da coluna de porcentagens é igual a 100
	tratamento = TratamentoDados()
	df = tratamento.LerExcel()
	df = tratamento.GerarPorcentagem(df, 'Total de Casos')
	soma = df['porcentagem_' + 'Total de Casos'].sum()
	# Comparação de float feita com o módulo da subtração
	assert abs(soma-float(100)) <= 0.001 
 