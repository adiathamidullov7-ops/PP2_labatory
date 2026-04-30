import json

def save_score(score):
    try:
        with open("leaderboard.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(score)

    with open("leaderboard.json", "w") as f:
        json.dump(data, f)


def get_best():
    try:
        with open("leaderboard.json", "r") as f:
            data = json.load(f)
        return max(data)
    except:
        return 0