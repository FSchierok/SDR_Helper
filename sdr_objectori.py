import sys
import numpy as np
import matplotlib.pyplot as plt


class GameMaster:

    def __init__(self, GameList, *PlayerNames):
        self.commands = {"t": self.pie_chart, "p": self.punkte, "n": self.next_game, "r": self.reset_last_game, "exit": lambda: sys.exit(0), "l": self.list_player}
        self.Players = list()
        self.IDs = dict()
        self.Data = GameList
        self.CurrentGame = 0
        for PlayerName in PlayerNames:
            self.Players.append(Player(PlayerName))
        self.score = self.Players

    def pie_chart(self):
        data = (np.arange(1, len(self.Data) + 1) / np.sum(np.arange(1, len(self.Data) + 1)))
        color = list()
        explodes = 0.01 * np.ones(len(self.Data))
        label = np.arange(1, len(self.Data) + 1)
        for i in np.arange(1, len(self.Data) + 1):
            if i <= self.CurrentGame:
                color.append("gold")
            else:
                color.append("darkorange")
        plt.pie(data, colors=color, explode=explodes, labels=label, startangle=90, counterclock=False)
        plt.title("Punkte nach dem " + str(self.CurrentGame) + ". Spiel")
        plt.show()

    def punkte(self):
        print("Der Zwischenstand ist")
        for Player in self.Players:
            print(Player.Name + ": " + str(Player.Points))

    def next_game(self):
        self.CurrentGame += 1
        print("Das nächste Spiel heist: \n" + str(self.CurrentGame) + ": " + self.Data[self.CurrentGame - 1])
        InputCheck = False
        while not InputCheck:
            Winner = input("Wer hat gewonnen? \n")
            if self.check_int(Winner):
                if (int(Winner) < len(self.Players)):
                    self.Players[int(Winner)].add_points(self.CurrentGame)
                    InputCheck = True
                    for Player in self.Players:
                        Player.add_points(0)
                        self.score.sort(key=lambda Obj: Obj.Points)
                else:
                    print("Ungültiger Spieler")

    def check_int(self, i):
        try:
            int(i)
            return True
        except ValueError:
            return False

    def reset_last_game(self):
        for Player in self.Players:
            Player.load_old_points()

    def list_player(self):
        print("Angemeldete Spieler:")
        for Player in self.Players:
            print(Player.Name)

    def run(self):
        while (self.CurrentGame < len(self.Data) and self.score[0].Points < (self.score[1].Points + np.sum(np.arange(1, len(self.Data) + 1)) - np.sum(np.arange(1, self.CurrentGame + 1)))):
            command = input("Was soll ich tun? \n")
            if command in self.commands:
                self.commands[command]()
            else:
                print("Ungültige Eingabe")
        print(self.score[0].Name + " hat gewonnen")


class Player:
    def __init__(self, PlayerName):
        self.Points = 0
        self.PointsOld = 0
        self.Name = PlayerName

    def add_points(self, AddPoints):
        self.PointsOld = self.Points
        self.Points += AddPoints

    def load_old_points():
        self.Points = self.PointsOld


with open(sys.argv[1]) as f:
    GameData = f.readlines()
myGameMaster = GameMaster(GameData, *sys.argv[2:])
myGameMaster.run()
