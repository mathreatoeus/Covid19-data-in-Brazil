import pandas as pd
import plotly.express as px
import streamlit as st

# Acessando o dataset e renomeando as colunas

data_frame = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

data_frame = data_frame.rename(columns={
    'newDeaths': 'Novos Óbitos',
    'newCases': 'Novos Casos',
    'deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes',
    'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes',
    'recovered': 'Recuperados',
    'deaths_by_totalCases': 'Mortes por casos totais',
    'vaccinated_third': 'Vacinados (terceira dose)'
})

# Selecao do estado

estados = list(data_frame['state'].unique())

selecao_estado = st.sidebar.selectbox(
    'Selecione o estado',
    estados
)

# Selecao da coluna

colunas = ('Novos Óbitos', 
    'Novos Casos', 
    'Óbitos por 100 mil habitantes', 
    'Casos por 100 mil habitantes', 
    'Recuperados', 
    'Mortes por casos totais',
    'Vacinados (terceira dose)')

selecao_coluna = st.sidebar.selectbox(
    'Selecione a informação',
    colunas
)

 # Plotagem dos dados 

data_frame = data_frame[data_frame['state'] == selecao_estado]

grafico_info_geral = px.line(data_frame, x='date', y=selecao_coluna, title=selecao_coluna + ' - ' + selecao_estado)
grafico_info_geral.update_layout(xaxis_title = 'Data', yaxis_title = selecao_coluna.upper(), title={'x': 0.5})

grafico_efetividade_vacinas = px.line(data_frame, x='date', y='Novos Óbitos', title='Efetividade das vacinas' + ' - ' + selecao_estado)
grafico_efetividade_vacinas.add_scatter(x=data_frame['date'], y=data_frame['Vacinados (terceira dose)'])
grafico_efetividade_vacinas.update_layout(xaxis_title='Data', yaxis_title='Efetividade das vacinas', title={'x': 0.5})

st.title('Covid 19 - Casos e Óbitos - Brasil')
st.write('Selecione o estado e a informação que deseja acessar. O gráfico será gerado automaticamente.')
st.caption('Os dados foram obtidos em: https://github.com/wcota/covid19br')

st.plotly_chart(grafico_info_geral, use_container_width=True)
st.plotly_chart(grafico_efetividade_vacinas, use_container_width=True)
