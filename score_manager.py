import json

class ScoreManager:
    def __init__(self, filename="scores.json"):
        self.filename = filename
        self.scores = {}

    def load_scores(self):
        try:
            with open(self.filename, "r") as file:
                self.scores = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.scores = {}

    def save_scores(self):
        with open(self.filename, "w") as file:
            json.dump(self.scores, file)

    def get_score(self, player):
        return self.scores.get(player, 0)

    def update_score(self, player):
        self.scores[player] = self.get_score(player) + 1
        self.save_scores()