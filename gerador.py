import streamlit as st
import json

st.title("🛠️ Criador de Quiz Gamificado")

if 'questoes' not in st.session_state:
    st.session_state.questoes = []

with st.form("nova_pergunta"):
    pergunta = st.text_input("Pergunta:")
    opcoes = st.text_area("Opções (uma por linha):").split('\n')
    correta = st.selectbox("Qual a opção correta?", options=opcoes)
    enviar = st.form_submit_state("Adicionar Pergunta")

    if enviar:
        st.session_state.questoes.append({
            "pergunta": pergunta,
            "opcoes": opcoes,
            "correta": correta
        })
        st.success("Pergunta adicionada!")

if st.button("💾 Salvar Quiz para a Aula"):
    with open('questoes.json', 'w', encoding='utf-8') as f:
        json.dump(st.session_state.questoes, f, ensure_ascii=False)
    st.balloons()
    st.write("Arquivo 'questoes.json' criado com sucesso!")