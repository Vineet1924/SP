participants = int(input("Enter Number of participants : "))
score = []

for i in range(1, participants + 1) :
    score_var = int(input("Enter Score for Participant " + str(i) + " : "))
    score.append(score_var)

score.sort()
print("Runner UP Score : " + str(score[participants - 2]))