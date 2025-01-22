from flask import Flask, render_template, url_for
import pandas as pd
import random
from collections import deque

app = Flask(__name__)

data = [

#la liga
    {"team": "Real Madrid", "country": "Espanha - La Liga",             "Overall": 86, "Ataque": 88, "Meio-campo": 85, "Defesa": 84, "image": "imagens/real-madrid.png"},
    {"team": "Barcelona", "country": "Espanha - La Liga",               "Overall": 83, "Ataque": 81, "Meio-campo": 81, "Defesa": 82, "image": "imagens/barcelona.png"},
    {"team": "Atletico Madrid", "country": "Espanha - La Liga",         "Overall": 82, "Ataque": 84, "Meio-campo": 81, "Defesa": 81, "image": "imagens/atletico-de-madrid.png"},
    {"team": "Athletic Club Bilbao", "country": "Espanha - La Liga",    "Overall": 80, "Ataque": 79, "Meio-campo": 80, "Defesa": 79, "image": "imagens/athletic-club-bilbao.png"},
#    {"team": "Girona FC", "country": "Espanha - La Liga",               "Overall": 79, "Ataque": 75, "Meio-campo": 79, "Defesa": 79, "image": "imagens/girona.png"},

#premier league
    {"team": "Newcastle", "country": "Inglaterra - Premier League",         "Overall": 80, "Ataque": 81, "Meio-campo": 82, "Defesa": 79, "image": "imagens/newcastle.png"},
    {"team": "Tottenham", "country": "Inglaterra - Premier League",         "Overall": 81, "Ataque": 82, "Meio-campo": 80, "Defesa": 78, "image": "imagens/tottenham.png"},
    {"team": "Arsenal", "country": "Inglaterra - Premier League",           "Overall": 84, "Ataque": 84, "Meio-campo": 85, "Defesa": 82, "image": "imagens/arsenal.png"},
#    {"team": "West Ham", "country": "Inglaterra - Premier League",          "Overall": 79, "Ataque": 81, "Meio-campo": 79, "Defesa": 78, "image": "imagens/west-ham.png"},
    {"team": "Manchester United", "country": "Inglaterra - Premier League", "Overall": 80, "Ataque": 80, "Meio-campo": 80, "Defesa": 81, "image": "imagens/manchester-united.png"},
    {"team": "Chelsea", "country": "Inglaterra - Premier League",           "Overall": 81, "Ataque": 81, "Meio-campo": 82, "Defesa": 79, "image": "imagens/chelsea.png"},
    {"team": "Manchester City", "country": "Inglaterra - Premier League",   "Overall": 85, "Ataque": 84, "Meio-campo": 86, "Defesa": 83, "image": "imagens/manchester-city.png"},
    {"team": "Liverpool", "country": "Inglaterra - Premier League",         "Overall": 84, "Ataque": 83, "Meio-campo": 84, "Defesa": 84, "image": "imagens/liverpool.png"},
    {"team": "Aston Villa", "country": "Inglaterra - Premier League",       "Overall": 80, "Ataque": 84, "Meio-campo": 80, "Defesa": 79, "image": "imagens/aston-villa.png"},

#seria a
#    {"team": "Atalanta", "country": "Itália - Serie A",             "Overall": 79, "Ataque": 78, "Meio-campo": 78, "Defesa": 78, "image": "imagens/atalanta.png"},
#    {"team": "Lazio", "country": "Itália - Serie A",                "Overall": 79, "Ataque": 80, "Meio-campo": 79, "Defesa": 78, "image": "imagens/lazio.png"},
 #   {"team": "Napoli", "country": "Itália - Serie A",               "Overall": 79, "Ataque": 81, "Meio-campo": 79, "Defesa": 79, "image": "imagens/napoli.png"},
    {"team": "Milano (AC Milan)", "country": "Itália - Serie A",    "Overall": 81, "Ataque": 79, "Meio-campo": 82, "Defesa": 80, "image": "imagens/milano.png"},
    {"team": "Juventus", "country": "Itália - Serie A",             "Overall": 80, "Ataque": 82, "Meio-campo": 79, "Defesa": 77, "image": "imagens/juventus.png"},
    {"team": "Roma", "country": "Itália - Serie A",                 "Overall": 80, "Ataque": 84, "Meio-campo": 79, "Defesa": 81, "image": "imagens/roma.png"},
    {"team": "Lombardia FC (Inter)", "country": "Itália - Serie A", "Overall": 83, "Ataque": 86, "Meio-campo": 83, "Defesa": 83, "image": "imagens/inter.png"},

#bundesliga
    {"team": "FC Bayern München", "country": "Alemanha - Bundesliga",   "Overall": 84, "Ataque": 90, "Meio-campo": 83, "Defesa": 82, "image": "imagens/fc-bayern mnchen.png"},
    {"team": "Bayer 04 Leverkusen", "country": "Alemanha - Bundesliga", "Overall": 83, "Ataque": 82, "Meio-campo": 83, "Defesa": 83, "image": "imagens/leverkusen.png"},
    {"team": "Borussia Dortmund", "country": "Alemanha - Bundesliga",   "Overall": 81, "Ataque": 80, "Meio-campo": 81, "Defesa": 81, "image": "imagens/borussia-dortmund.png"},
    {"team": "RB Leipzig", "country": "Alemanha - Bundesliga",          "Overall": 80, "Ataque": 81, "Meio-campo": 79, "Defesa": 80, "image": "imagens/rb-leipzig.png"},
    

#outros
#    {"team": "Galatasaray SK", "country": "Turquia",                "Overall": 79, "Ataque": 82, "Meio-campo": 78, "Defesa": 77, "image": "imagens/galatasaray.png"},
#    {"team": "Fenerbahçe SK", "country": "Turquia",                 "Overall": 79, "Ataque": 81, "Meio-campo": 79, "Defesa": 78, "image": "imagens/fenerbahce.png"},
    {"team": "Paris Saint-Germain", "country": "França - Liga 1",   "Overall": 82, "Ataque": 81, "Meio-campo": 82, "Defesa": 83, "image": "imagens/psg.png"},

#Internacional
    {"team": "França", "country": "Internacional",      "Overall": 85, "Ataque": 85, "Meio-campo": 84, "Defesa": 85, "image": "imagens/franca.png"},
    {"team": "Inglaterra", "country": "Internacional",  "Overall": 84, "Ataque": 87, "Meio-campo": 85, "Defesa": 82, "image": "imagens/inglaterra.png"},
    {"team": "Alemanha", "country": "Internacional",    "Overall": 84, "Ataque": 79, "Meio-campo": 83, "Defesa": 84, "image": "imagens/alemanha.png"},
    {"team": "Portugal", "country": "Internacional",    "Overall": 84, "Ataque": 85, "Meio-campo": 84, "Defesa": 83, "image": "imagens/portugal.png"},
    {"team": "Espanha", "country": "Internacional",     "Overall": 84, "Ataque": 83, "Meio-campo": 83, "Defesa": 83, "image": "imagens/espanha.png"},
    {"team": "Netherlands", "country": "Internacional", "Overall": 83, "Ataque": 81, "Meio-campo": 83, "Defesa": 84, "image": "imagens/netherlands.png"},
    {"team": "Argentina", "country": "Internacional",   "Overall": 83, "Ataque": 87, "Meio-campo": 84, "Defesa": 81, "image": "imagens/argentina.png"},


    {"team": "Itália", "country": "Internacional", "Overall": 82, "Ataque": 78, "Meio-campo": 82, "Defesa": 81, "image": "imagens/italia.png"}

]

df = pd.DataFrame(data)
recent_matches = deque(maxlen=5) 

def generate_match():
    filtered_teams = df[df['Overall'] >= 79]  
    while True:
        match = filtered_teams.sample(n=2)  
        team1, team2 = match.iloc[0], match.iloc[1]
        match_tuple = frozenset([team1['team'], team2['team']])  
        if abs(team1['Overall'] - team2['Overall']) <= 2 and match_tuple not in recent_matches:
            recent_matches.append(match_tuple) 
            break
    return team1.to_dict(), team2.to_dict()

@app.route('/')
def index():
    team1, team2 = generate_match()
    return render_template('index.html', team1=team1, team2=team2)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
