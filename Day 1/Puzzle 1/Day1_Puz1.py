with open("Day 1/Puzzle 1/Day1_Puz1.txt") as file:
    contents = file.read()
summ=0
alpa={
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}
for i in contents.split("\n"):
    fwd,bwd=0,0
    for key, val in alpa.items():
        i = i.replace(key, val)
    for j in i:
        if j.isdigit():
            fwd=j
            if bwd==0:
                bwd=j
    summ += int(fwd+bwd)
print(summ)