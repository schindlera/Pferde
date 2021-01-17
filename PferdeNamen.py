# Try to guess start-Position
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
d = {}
for i in alphabet: d[i] = 0
total = 0
expected = 30
StartLetter = "X"
EndLetter = "S"
with open("Pferde.txt", 'r') as sample:
    NextIsName = False
    for line in sample.readlines():
        if NextIsName:
            d[line[0]] += 1
            total += 1
            NextIsName = False
        else:
            if len(line) and line[0] in '01':
                NextIsName = True
start = alphabet.find(StartLetter)
end  = alphabet.find(EndLetter)
if end<start: end += 26

StartNo = 0
for c in alphabet2[start:end]:
    StartNo += d[c]/total*expected
    print (c,d[c])

print (StartNo)
print (len(alphabet))
print (total)
print (d)