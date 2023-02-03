# BIBLIOTECAS USADAS

import streamlit as st
from PIL import Image

im = Image.open("imagens/olx_scrapy.png")
st.set_page_config(page_title="OLX Scrapy | Grande Florianópolis", page_icon=im, layout="wide")

st.markdown(""" <style>
        footer {visibility: hidden;}
        </style> """, unsafe_allow_html=True)


from plots.plots_olx import *
from layout.layout_olx import *

path = 'data/olx22.csv'
df1 = get_data(path)

df = tratamento_dados(df1)

im1 = Image.open("imagens/olx.png")
im2 = Image.open("imagens/scrapy.png")

col1, col2, col3, col4, col5 = st.columns([100, 150, 1000, 150, 100])
with col1:
    st.text("")
with col2:
    st.image(im1)
with col3:
    st.markdown("<h1 style='font-size:300%; text-align: center; color: #6709CB; padding: 0px 0px;'" +
                ">OLX Scrapy</h1>",
                unsafe_allow_html=True)
    st.markdown("<h2 style='font-size:180%; text-align: center; color: #6709CB; padding: 0px 0px;'" +
                ">Anúncios de Venda de Imóveis da Grande Florianópolis</h2>",
                unsafe_allow_html=True)
    st.markdown("<h3 style='font-size:130%; text-align: center; color: #6709CB; padding: 0px 0px;'" +
                ">Atualização: 24/01/2023</h3>",
                unsafe_allow_html=True)

with col4:
    st.image(im2)
with col5:
    st.text("")
st.markdown('---')



with st.expander("⚙️ Configurar Dados"):

    valor_max = (df['VALOR [R$]'].max())
    valor_min = (df['VALOR [R$]'].min())
    #slider1, slider2 = st.slider('Filtre o Valor do Imóvel:', valor_min, valor_max, [valor_min, valor_max], 100)
    #mask_valor = (df['VALOR [R$]'] >= slider1) & (df['VALOR [R$]'] <= slider2)

    area_max = (df['AREA [M2]'].max())
    area_min = (df['AREA [M2]'].min())
    #slider1, slider2 = st.slider('Filtre a Area do Imóvel:', area_min, area_max, [area_min, area_max], 10)
    #mask_area = (df['AREA [M2]'] >= slider1) & (df['AREA [M2]'] <= slider2)

    categoria = df['CATEGORIA'].unique().tolist()
    selected_categoria = st.multiselect("Filtre por Categoria de Imóvel:",
                                   options=categoria, default=categoria)

    quartos = df['QUARTOS'].unique().tolist()
    selected_quartos = st.multiselect("Filtre a Quantidade de Quartos:",
                                     options=quartos, default=quartos)
    banheiros = df['BANHEIROS'].unique().tolist()
    selected_banheiros = st.multiselect("Filtre a Quantidade de Banheiros:",
                                      options=banheiros, default=banheiros)
    vagas = df['VAGAS GARAGEM'].unique().tolist()
    selected_vagas = st.multiselect("Filtre a Quantidade de Vagas de Garagem:",
                                      options=vagas, default=vagas)


df = df[df['CATEGORIA'].isin(selected_categoria)]
df = df[df['QUARTOS'].isin(selected_quartos)]
df = df[df['BANHEIROS'].isin(selected_banheiros)]
df = df[df['VAGAS GARAGEM'].isin(selected_vagas)]
#df = df.loc[mask_valor]
#df = df.loc[mask_area]

st.markdown("<h3 style='font-size:200%; text-align: center; color: #6709CB; padding: 0px 0px;'" +
            ">Base de Dados Completa</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='font-size:120%; text-align: center; color: #6709CB; padding: 0px 0px;'" +
            ">Número de linhas: "+str(df.shape[0])+"</h4>", unsafe_allow_html=True)
st.text("")

selected_rows = agg_tabela(df, use_checkbox=True)
st.markdown('---')


tab1, tab2, tab3, tab4 = st.tabs([ "📊 DASHBOARD", "🌎 MAPAS", "‍🔬 LABORATÓRIO", "🔎 DADOS"])

with tab1:
    dashboard(df)
with tab2:
    st.text("mapas")
with tab3:
    olxlab(df, selected_rows)
with tab4:
    relatorio(df)





st.text("")
st.text("")
st.text("")

rodape()