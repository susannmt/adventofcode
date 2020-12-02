expences = [int(e) for e in open("input.txt").readlines()]

for i in range(len(expences)):
    for j in range(len(expences)):
        if expences[i]+expences[j] == 2020:
            print(expences[i], expences[j], expences[i]*expences[j])



for i in range(len(expences)):
    for j in range(len(expences)):
        for k in range(len(expences)):
            if expences[i]+expences[j]+expences[k] == 2020:
                print(expences[i], expences[j], expences[k], expences[i]*expences[j]*expences[k])
