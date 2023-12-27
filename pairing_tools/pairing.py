from allpairspy import AllPairs

parameters = [
    ["Brand X", "Brand Y"],
    ["98", "NT", "2000", "XP"],
    ["Internal", "Modem"],
    ["Salaried", "Hourly", "Part-Time", "Contr."],
    [6, 10, 15, 30, 60],
]

print("PAIRWISE:")
with open('pair.log', 'w') as f :
    for i, pairs in enumerate(AllPairs(parameters)):
        print("{:2d}: {}".format(i, pairs))

        f.write("{:2d}: {}".format(i, pairs)+'\n')
