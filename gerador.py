import streamlit as st
import json

st.set_page_config(page_title="Gerador de Quiz - Prof. Alison", page_icon="📝")

st.title("🛠️ Criador de Quiz Gamificado")
st.markdown("Use este formulário para criar as perguntas da sua aula.")

if 'questoes' not in st.session_state:
    st.session_state.questoes = []

# Formulário para adicionar perguntas
with st.form("nova_pergunta"):
    pergunta = st.text_input("Digite a Pergunta:")
    opcoes_texto = st.text_area("Digite as Opções (uma por linha):")
    
    # Processa as opções para não dar erro se estiver vazio
    opcoes = opcoes_texto.split('\n') if opcoes_texto else [""]
    
    correta = st.selectbox("Qual é a opção correta?", options=opcoes)
    
    # AQUI ESTAVA O ERRO: Corrigido para st.form_submit_button
    enviar = st.form_submit_button("Adicionar Pergunta à Lista")

    if enviar:
        if pergunta and opcoes_texto:
            st.session_state.questoes.append({
                "pergunta": pergunta,
                "opcoes": [opt.strip() for opt in opcoes if opt.strip()],
                "correta": correta.strip()
            })
            st.success("✅ Pergunta adicionada com sucesso!")
        else:
            st.warning("⚠️ Por favor, preencha a pergunta e as opções.")

# Exibe as perguntas já adicionadas
if st.session_state.questoes:
    st.subheader("📋 Perguntas no seu Quiz:")
    for i, q in enumerate(st.session_state.questoes):
        st.write(f"{i+1}. {q['pergunta']} (Correta: {q['correta']})")

    # Botão para salvar o arquivo final
    if st.button("💾 Finalizar e Baixar Quiz para a Aula"):
        dados_json = json.dumps(st.session_state.questoes, indent=4, ensure_ascii=False)
        st.download_button(
            label="Clique aqui para baixar o arquivo do Quiz",
            data=dados_json,
            file_name="questoes.json",
            mime="application/json"
        )
        st.balloons()
