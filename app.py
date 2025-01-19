from flask import Flask, render_template, url_for
import pandas as pd
import random
from collections import deque


# Configuração do Flask
app = Flask(__name__)

# Criar banco de dados básico com times e suas estrelas
data = [

#la liga
    {"team": "Real Madrid", "country": "Spain", "overall": 86, "image": "imagens/real-madrid.png"},
    {"team": "Barcelona", "country": "Spain", "overall": 83, "image": "imagens/barcelona.png"},
    {"team": "Atletico Madrid", "country": "Spain", "overall": 82, "image": "imagens/atletico-de-madrid.png"},
    {"team": "Athletic Club Bilbao", "country": "Spain", "overall": 80, "image": "imagens/athletic-club-bilbao.png"},
    {"team": "Girona FC", "country": "Spain", "overall": 79, "image": "imagens/girona.png"},

#premier league
    {"team": "Newcastle", "country": "England", "overall": 80, "image": "imagens/newcastle.png"},
    {"team": "Tottenham", "country": "England", "overall": 81, "image": "imagens/tottenham.png"},
    {"team": "Arsenal", "country": "England", "overall": 84, "image": "imagens/arsenal.png"},
    {"team": "West Ham", "country": "England", "overall": 79, "image": "imagens/west-ham.png"},
    {"team": "Manchester United", "country": "England", "overall": 80, "image": "imagens/manchester-united.png"},
    {"team": "Chelsea", "country": "England", "overall": 81, "image": "imagens/chelsea.png"},
    {"team": "Manchester City", "country": "England", "overall": 85, "image": "imagens/manchester-city.png"},
    {"team": "Liverpool", "country": "England", "overall": 84, "image": "imagens/liverpool.png"},
    {"team": "Aston Villa", "country": "England", "overall": 80, "image": "imagens/aston-villa.png"},

#seria a italia
    {"team": "Atalanta", "country": "Italy", "overall": 79, "image": "imagens/atalanta.png"},
    {"team": "Lazio", "country": "Italy", "overall": 79, "image": "imagens/lazio.png"},
    {"team": "Napoli", "country": "Italy", "overall": 79, "image": "imagens/napoli.png"},
    {"team": "Milano (AC Milan)", "country": "Italy", "overall": 81, "image": "imagens/milano.png"},
    {"team": "Juventus", "country": "Italy", "overall": 80, "image": "imagens/juventus.png"},
    {"team": "Roma", "country": "Italy", "overall": 80, "image": "imagens/roma.png"},
    {"team": "Lombardia FC (Inter)", "country": "Italy", "overall": 83, "image": "imagens/inter.png"},

#bundesliga
    {"team": "FC Bayern München", "country": "Germany", "overall": 84, "image": "imagens/fc-bayern mnchen.png"},
    {"team": "Bayer 04 Leverkusen", "country": "Germany", "overall": 83, "image": "imagens/leverkusen.png"},
    {"team": "Borussia Dortmund", "country": "Germany", "overall": 83, "image": "imagens/borussia-dortmund.png"},
    {"team": "RB Leipzig", "country": "Germany", "overall": 83, "image": "imagens/rb-leipzig.png"},
    

#outros
    {"team": "Galatasaray SK", "country": "Turkey", "overall": 83, "image": "imagens/galatasaray.png"},
    {"team": "Fenerbahçe SK", "country": "Turkey", "overall": 83, "image": "imagens/fenerbahce.png"},
    {"team": "Paris Saint-Germain", "country": "France", "overall": 82, "image": "imagens/psg.png"},

#seleções
    {"team": "França", "country": " ", "overall": 85, "image": "imagens/franca.png"},
    {"team": "Inglaterra", "country": " ", "overall": 84, "image": "imagens/inglaterra.png"},
    {"team": "Alemanha", "country": " ", "overall": 84, "image": "imagens/alemanha.png"},
    {"team": "Portugal", "country": " ", "overall": 84, "image": "imagens/portugal.png"},
    {"team": "Espanha", "country": " ", "overall": 84, "image": "imagens/espanha.png"},
    {"team": "Netherlands", "country": " ", "overall": 83, "image": "imagens/netherlands.png"},
    {"team": "Argentina", "country": " ", "overall": 83, "image": "imagens/argentina.png"},


    {"team": "Itália", "country": "", "overall": 82, "image": "imagens/italia.png"}

]

# Converter para DataFrame para facilitar a manipulação
df = pd.DataFrame(data)

# Histórico de partidas recentes
recent_matches = deque(maxlen=5)  # Armazena até 5 partidas recentes

# Rota principal
def generate_match():
    filtered_teams = df[df['overall'] >= 79]  # Filtrar times com overall >= 79
    while True:
        match = filtered_teams.sample(n=2)  # Selecionar 2 times aleatórios
        team1, team2 = match.iloc[0], match.iloc[1]
        match_tuple = frozenset([team1['team'], team2['team']])  # Representação única para o par de times

        # Verificar diferença máxima de overall e se a partida já ocorreu recentemente
        if abs(team1['overall'] - team2['overall']) <= 3 and match_tuple not in recent_matches:
            recent_matches.append(match_tuple)  # Adicionar ao histórico de partidas recentes
            break
    return team1.to_dict(), team2.to_dict()

@app.route('/')
def index():
    team1, team2 = generate_match()
    return render_template('index.html', team1=team1, team2=team2)

if __name__ == "__main__":
    app.run(debug=True)
