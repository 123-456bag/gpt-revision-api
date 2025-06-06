from fastapi import FastAPI, Query

app = FastAPI()

chapitres = [
    "Fonctions", "Dérivation", "Études de signes", "Suites", "Limites", "Continuité",
    "Primitives", "Intégrales", "Probabilités", "Variables aléatoires", "Lois binomiales",
    "Lois exponentielles", "Géométrie analytique", "Produit scalaire", "Nombres complexes"
]

planning = []
for i, chapitre in enumerate(chapitres):
    planning.append({
        "type": "rappel",
        "topic": chapitre,
        "recap": f"Rappel du chapitre {i+1} : {chapitre}",
        "exercise": f"Exercice d'entraînement sur le thème : {chapitre}"
    })

for i in range(1, 16):
    planning.append({
        "type": "annale",
        "topic": f"Annale de bac n°{i}",
        "recap": f"Sujet type bac n°{i} : entraînement en condition réelle",
        "exercise": f"Résous l'annale n°{i} (à retrouver sur le site APMEP ou ton manuel)"
    })

@app.get("/daily-session")
def get_day(day: int = Query(..., ge=1, le=30)):
    data = planning[day - 1]
    return {
        "day": day,
        "type": data["type"],
        "topic": data["topic"],
        "recap": data["recap"],
        "exercise": data["exercise"]
    }