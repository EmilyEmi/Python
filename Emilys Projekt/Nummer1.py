import random

wörter = ["nett","blöd","toll","klein","verrückt","sympathisch","uncool","komisch","cool"]

sentence = []

for part in wörter:
    r = random.randint(0, len(part) -1)
    sentence.append(part[r])

print(" ".join(sentence))
