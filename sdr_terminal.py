import sys
import numpy as np
import matplotlib.pyplot as plt


def pie_chart(maxG, done):
    data = (np.arange(1, maxG + 1)) / np.sum(np.arange(1, maxG + 1))
    colours = list()
    expose = 0.01 * np.ones(maxG)
    label = np.arange(1, maxG + 1)
    for i in np.arange(1, maxG + 1):
        if i <= done:
            colours.append("darkorange")
        else:
            colours.append("gold")
    plt.pie(data, colors=colours, explode=expose, labels=label, startangle=90, counterclock=False)
    plt.title("Punkte nach dem " + str(done) + ". Spiel")
    plt.show()


def punkte(p1, p2):
    print("Der Zwischenstand ist")
    print(player1 + ": " + str(p1))
    print(player2 + ": " + str(p2))


def next_game():
    global spiel  # bogdie af
    global p1
    global p2
    global p1_old
    global p2_old
    spiel += 1
    print("Das nächste Spiel heist: \n" + str(spiel) + ": " + data[spiel - 1])
    korrekteEingabe = False
    while not korrekteEingabe:
        winner = input("Wer hat gewonnen? \n")
        p1_old = p1
        p2_old = p2
        if winner == "p1":
            p1 = p1 + spiel
            korrekteEingabe = True
        elif winner == "p2":
            p2 = p2 + spiel
            korrekteEingabe = True
        else:
            print("Das habe ich nicht verstanden")


def reset_last_game():
    global spiel
    global p1
    global p2
    global p1_old
    global p2_old
    p1 = p1_old
    p2 = p2_old
    print("Das Spiel " + data[spiel] + " wurde revidiert")
    spiel -= 1


commads = {"t": lambda: pie_chart(maxS, spiel), "p": lambda: punkte(p1, p2), "n": lambda: next_game(), "r": reset_last_game, "exit": lambda: sys.exit(0)}

with open(sys.argv[3], "r") as f:
    data = f.readlines()
player1 = sys.argv[1]
player2 = sys.argv[2]
p1, p2, p1_old, p2_old, spiel = 0, 0, 0, 0, 0
maxS = len(data)
print("Hallo! der Spieler p1 ist " + player1 + " und der Spieler p2 ist " + player2)
print("Eine kurze Anleitung: \n mit t wird die Tortengrafik eingeblendet \n mit p werden die Punkte numerisch angezeigt \n mit exit kann das Spiel vorzeitig beendet werden \n mit n wird das nächste Spiel eingeleitet, Dieses fragt dann nach dem Gewinner in der Form von p1 oder p2")
print("Das Spiel geht los")
while spiel < maxS and p1 <= np.sum(np.arange(1, maxS + 1)) / 2 and p2 <= np.sum(np.arange(1, maxS + 1)) / 2:
    eingabe = input("Was soll ich tun? \n")
    if eingabe in commads:
        commads[eingabe]()
if p1 < p2:
    res = player2
elif p1 > p2:
    res = player1
else:
    res = "an beide Spieler"
print("Glückwunsch " + res)
