from flask import Flask, render_template_string, request
import json
import socket

app = Flask(__name__)

# Carrega as questões criadas no gerador
def carregar_questoes():
    with open('questoes.json', 'r', encoding='utf-8') as f:
        return json.load(f)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz Offline - Prof. Alison</title>
    <style>
        body { font-family: sans-serif; text-align: center; background: #f0f2f6; }
        .card { background: white; margin: 20px; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        button { background: #4CAF50; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🏆 Arena de Português</h1>
        {% for q in questoes %}
            <div class="card">
                <p><strong>{{ q.pergunta }}</strong></p>
                {% for opt in q.opcoes %}
                    <button onclick="verificar('{{opt}}', '{{q.correta}}')">{{ opt }}</button>
                {% endfor %}
            </div>
        {% endfor %}
    </div>
    <script>
        function verificar(escolha, correta) {
            if(escolha === correta) { alert("✅ Acertou! +10 XP"); }
            else { alert("❌ Errou! Tente a próxima."); }
        }
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    questoes = carregar_questoes()
    return render_template_string(HTML_TEMPLATE, questoes=questoes)

if __name__ == '__main__':
    # Descobre o IP do seu computador na rede Wi-Fi
    hostname = socket.gethostname()
    ip_local = socket.gethostbyname(hostname)
    print(f"\n🚀 SERVIDOR ONLINE SEM INTERNET!")
    print(f"1. Conecte os alunos no seu Wi-Fi.")
    print(f"2. Peça para acessarem: http://{ip_local}:5000\n")
    app.run(host='0.0.0.0', port=5000)