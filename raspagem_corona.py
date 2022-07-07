from selenium import webdriver
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

class RaspagemCorona():

	def __init__(self):

		self.driver = webdriver.Chrome()
		self.driver.get('https://www.worldometers.info/coronavirus/')


	def RasparDados(self, pais, coluna):

		dado = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[{}]/td[{}]'.format(pais,coluna)).text
		
		return dado		

	def ParaDicionario(self, dados_pais, dict_final):

		dict_final[dados_pais[1]] = dict()

		dict_final[dados_pais[1]]['Total de Casos'] = dados_pais[2]
		dict_final[dados_pais[1]]['Novos Casos'] = dados_pais[3]
		dict_final[dados_pais[1]]['Total de Mortes'] = dados_pais[4]
		dict_final[dados_pais[1]]['Novas Mortes'] = dados_pais[5]
		dict_final[dados_pais[1]]['Total de Recuperados'] = dados_pais[6]
		dict_final[dados_pais[1]]['Casos Ativos'] = dados_pais[7]
		dict_final[dados_pais[1]]['Sério ou Crítico'] = dados_pais[8]
		dict_final[dados_pais[1]]['Total de Casos/1M População'] = dados_pais[9]
		dict_final[dados_pais[1]]['Mortes/1M População'] = dados_pais[10]
		dict_final[dados_pais[1]]['Total de Testes'] = dados_pais[11]
		dict_final[dados_pais[1]]['Testes/1M População'] = dados_pais[12]

		return dict_final

	def TratarString(self, dado):

		if ',' in dado:
			dado = dado.replace(',', '')

		if '+' in dado:
			dado = dado.replace('+', '') 

		if dado == '':
			dado = 0

		if dado == 'N/A':
			dado = np.nan
		
		try:
			dado = int(dado)
		except:	
			pass

		return dado

 
class TratamentoGrafico():

	def PlotarBarrasComposto(self, df):
		
		paises = df['Paises']

		fig = go.Figure()

		fig.add_trace(go.Bar(
		    x=paises,
		    y=df['Total de Casos'],
		    name='Total de Casos',
		    marker_color='indianred'
		))
		fig.add_trace(go.Bar(
		    x=paises,
		    y=df['Total de Mortes'],
		    name='Total de Mortes',
		    marker_color='lightsalmon'
		))

		# Here we modify the tickangle of the xaxis, resulting in rotated labels.
		fig.update_layout(barmode='group', 
						  xaxis_tickangle=-45, 
						  title = 'Incidência Mundial do Vírus',
						  font = dict(family="Courier New, monospace",
        							  size=18,
        							  color="#7f7f7f")
						  )
		fig.write_html('barras_corona.html', auto_open=True)

'''
	def PlotarMapa(self, df):

		df_base = px.data.gapminder()

		df_base = df_base.drop_duplicates(subset="country")

		out_df = df_base[['country', 'iso_alpha', 'continent']]

		out_df.at[1596, 'country'] = 'UK'
		out_df.at[1608, 'country'] = 'USA'
		
		df = df[['Paises', 'Total de Casos']]
		
		final_df = out_df.merge(df, left_on = 'country', right_on = 'Paises')
		
		fig = px.scatter_geo(final_df, locations="iso_alpha", color="continent",
		                     hover_name="country", size="Total de Casos",
		                     projection="natural earth")

		fig.update_layout(title = 'Número Total de Casos: COVID-19',
						  font = dict(family="Courier New, monospace",
        							  size=18,
        							  color="#7f7f7f")
						  )


		fig.write_html('mapa_corona.html', auto_open=True)

		'''