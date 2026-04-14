from flask import Flask, render_template_string, redirect, url_for

app = Flask(__name__)

# --- SUA CLASSE ORIGINAL (Ajustada para o ambiente web) ---
class ControleRemoto:
    canal_min, canal_max = 1, 5
    volume_min, volume_max = 1, 5

    def __init__(self):
        self.canal_atual = 1
        self.volume_atual = 2
        self.ligado = False

    def liga_desliga(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            self.canal_atual = self.canal_min if self.canal_atual == self.canal_max else self.canal_atual + 1

    def canal_menos(self):
        if self.ligado:
            self.canal_atual = self.canal_max if self.canal_atual == self.canal_min else self.canal_atual - 1

    def volume_mais(self):
        if self.ligado and self.volume_atual < self.volume_max:
            self.volume_atual += 1

    def volume_menos(self):
        if self.ligado and self.volume_atual > self.volume_min:
            self.volume_atual -= 1

# Instância única para manter o estado da TV enquanto o servidor rodar
tv = ControleRemoto()

# --- INTERFACE VISUAL (Substituindo o Panel do Rich por HTML/CSS) ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Controle Remoto Web</title>
    <style>
        body { background: #1a1a1a; color: white; font-family: sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .tv-frame { background: #333; padding: 20px; border-radius: 20px; border-bottom: 40px solid #222; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        .screen { width: 350px; height: 220px; background: #000; display: flex; flex-direction: column; align-items: center; justify-content: center; border-radius: 10px; border: 4px solid #111; }
        .screen.on { background: radial-gradient(circle, #222 0%, #000 100%); color: #00ffcc; text-shadow: 0 0 8px #00ffcc; }
        .screen.off { color: #400; }
        .vol-bar { display: flex; gap: 3px; margin-top: 10px; }
        .vol-unit { width: 12px; height: 15px; background: #222; border: 1px solid #444; }
        .vol-on { background: #00ffcc; box-shadow: 0 0 5px #00ffcc; }
        .controls { margin-top: 30px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
        button { padding: 15px; border: none; border-radius: 10px; background: #444; color: white; cursor: pointer; font-weight: bold; }
        button:active { background: #666; transform: translateY(2px); }
        .power { background: #b00; grid-column: span 3; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="tv-frame">
        <div class="screen {{ 'on' if tv.ligado else 'off' }}">
            {% if tv.ligado %}
                <h1 style="font-size: 3em; margin: 0;">CH {{ tv.canal_atual }}</h1>
                <div class="vol-bar">
                    {% for i in range(1, 6) %}
                        <div class="vol-unit {{ 'vol-on' if i <= tv.volume_atual else '' }}"></div>
                    {% endfor %}
                </div>
            {% else %}
                <h2>DESLIGADA</h2>
            {% endif %}
        </div>
    </div>

    <div class="controls">
        <a href="/acao/power"><button class="power">LIGAR / DESLIGAR</button></a>
        <a href="/acao/ch_menos"><button>CH -</button></a>
        <div style="text-align:center; padding: 10px">CONTROLE</div>
        <a href="/acao/ch_mais"><button>CH +</button></a>
        <a href="/acao/vol_menos"><button>VOL -</button></a>
        <div></div>
        <a href="/acao/vol_mais"><button>VOL +</button></a>
    </div>
</body>
</html>
"""

# --- ROTAS (Comandos) ---
@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, tv=tv)

@app.route('/acao/<comando>')
def acao(comando):
    if comando == 'power': tv.liga_desliga()
    elif comando == 'ch_mais': tv.canal_mais()
    elif comando == 'ch_menos': tv.canal_menos()
    elif comando == 'vol_mais': tv.volume_mais()
    elif comando == 'vol_menos': tv.volume_menos()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)