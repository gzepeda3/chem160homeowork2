from random import choices #A
ntrials=15000 #B
player1wins=0 #C
ndice_2=2
ndice_1=3
for i in range(ntrials):  #D
    dice_2=choices(range(1,7),k=ndice_2)  #E
    if dice_2[0]==dice_2[1]: #f
        continue
    else:
        dice_2_sum = dice_2[0] + dice_2[1]

    dice_1=choices(range(1,7),k=ndice_1)    #G
    dice_1.sort(reverse=True)      #H
    dice_1_sum =dice_1[0]+dice_1[1]  #I
    if dice_1_sum > dice_2_sum:
        player1wins +=1

print(player1wins)
ratio = player1wins/ntrials  #J
print(ratio)


