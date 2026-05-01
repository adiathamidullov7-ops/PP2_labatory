import json
import os

FILE = r"C:\Users\adiat\Music\pp2_adia\TSIS3\leaderboard.json"


# ===================== LOAD DATA =====================
def load_data():
    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []


# ===================== SAVE SCORE =====================
def save_score(name, score):
    data = load_data()

    # добавляем новый результат
    data.append({
        "name": name,
        "score": score
    })

    # сортировка по убыванию
    data.sort(key=lambda x: x["score"], reverse=True)

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


# ===================== BEST SCORE =====================
def get_best():
    data = load_data()

    if not data:
        return None

    return max(data, key=lambda x: x["score"])


# ===================== TOP LIST =====================
def get_top(n=5):
    data = load_data()
    data.sort(key=lambda x: x["score"], reverse=True)
    return data[:n]