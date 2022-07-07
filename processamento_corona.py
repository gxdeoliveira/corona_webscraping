from raspagem_corona import RaspagemCorona, TratamentoDados, TratamentoGrafico

if __name__ == '__main__':

	paises_out = [5, 6, 18]
	n_primeiro = 4 
	n_ultimo_pais = 34
	# Escolher opcao para 'raspar' ou 'ler_excel'
	opcao = 'ler_excel'

	# Raspador
	if opcao == 'raspar':

		raspador = RaspagemCorona()
		dict_final = dict()

		for pais in range(n_primeiro, n_ultimo_pais): 
			
			dados_pais = list()

			if pais not in paises_out:
				for coluna in range(1,15):
					dado = raspador.RasparDados(pais, coluna)
					dado = raspador.TratarString(dado)
					dados_pais.append(dado)
				dict_final = raspador.ParaDicionario(dados_pais, dict_final)
			else:
				pass
	
		tratamento = TratamentoDados()
		df = tratamento.ParaDataFrame(dict_final)
		df = tratamento.TratarDataFrame(df)
		tratamento.ParaExcel(df)
		print('DataFrame raspado')
		print(df)

	# Ler excel
	elif opcao == 'ler_excel':

		tratamento = TratamentoDados()
		df = tratamento.LerExcel()
		print('DataFrame do Excel')
		print(df)

	tratamento_grafico = TratamentoGrafico()
	#tratamento_grafico.PlotarBarrasComposto(df)

	tratamento_grafico.PlotarMapa(df)

print('Função main executada!')