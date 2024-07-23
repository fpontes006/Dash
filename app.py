import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1-Importando os Dados
data = pd.read_csv('data/Pedidos.csv')
df = pd.DataFrame(data)
# print(df)

def main():
    st.title("DashBoard de Vendas :shopping_trolley:")
    
    aba1,aba2,aba3 = st.tabs(['DataSet','Receita','Vendedores'])
    with aba1:
        display_dataframe(df)
    with aba2:
        pass
    with aba3:
        pass
    
    
    
def display_dataframe(data):
    st.header("Visualização do Dataframe")
    st.sidebar.header("Filtros")
    selectd_region = st.sidebar.multiselect("Selecione as regioes",data['Regiao'].unique(),data['Regiao'].unique())
    filtered_data = data[data['Regiao'].isin(selectd_region)]
    st.write(filtered_data)

if __name__ == "__main__":
    main()