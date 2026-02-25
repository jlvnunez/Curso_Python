import streamlit as st

# Configuração da página (Título na aba do navegador)
st.set_page_config(page_title="Brasileirão 2026", page_icon="⚽")

# Dados
times = ('Palmeiras', 'Sao Paulo', 'Fluminense', 'Bahia', 'Corinthians',
         'Athletico-PR', 'Bragantino', 'Chapecoense', 'Mirassol', 'Coritiba',
         'Flamengo', 'Botafogo', 'Gremio', 'Vitoria', 'Atletico MG',
         'Remo', 'Vasco', 'Santos', 'Internacional', 'Cruzeiro')

# Título Principal na Página
st.title("🏆 Tabela do Brasileirão 2026")

# Criando abas para organizar a visualização
tab1, tab2, tab3 = st.tabs(["Tabela Completa", "Análises", "Busca"])

with tab1:
    st.header("Classificação")
    for i, t in enumerate(times):
        pos = i + 1
        if pos <= 6:
            st.success(f"**{pos}º {t}** (Libertadores)")
        elif pos >= 17:
            st.error(f"**{pos}º {t}** (Zona de Rebaixamento)")
        else:
            st.write(f"**{pos}º** {t}")

with tab2:
    st.header("Resumo")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Top 5")
        st.write(list(times[:5]))
    with col2:
        st.subheader("Z4")
        st.write(list(times[-4:]))
    
    st.subheader("Ordem Alfabética")
    st.info(", ".join(sorted(times)))

with tab3:
    st.header("Localizar Time")
    escolha = st.selectbox("Selecione um time para ver a posição:", times)
    pos_busca = times.index(escolha) + 1
    st.metric(label=f"Posição do {escolha}", value=f"{pos_busca}º Lugar")