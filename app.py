import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



st.set_page_config(page_title="Dashboard - Student Dataset", page_icon=":books:")


#st.sidebar.title("Configurações ")

st.title("Análise de Dados do Dataset de Refeições ")

#private_gsheets_url = "https://docs.google.com/spreadsheets/d/12345/edit?usp=sharing"
gsheets_url = 'https://docs.google.com/spreadsheets/d/1Xr6uPNAlT4n9FDuR91JyY2QwFGLGmMICPE5WqjW-s1k/export?format=csv&gid=1378939680' 
dados = pd.read_csv(gsheets_url)

st.dataframe(dados)

# Plot do gráfico
plt.figure(figsize=(10, 6))
sns.countplot(x='Refeicao', data=dados)
plt.xlabel('Tipo de Refeicao')
plt.ylabel('Contagem')
plt.title('Distribuição dos Tipos de Refeicao')

st.pyplot()
