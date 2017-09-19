import re

source = open('text1.txt', mode='r', encoding='ansi')
short = open('short.txt', mode='r', encoding='ansi')
result1 = open('text2.txt', mode='w', encoding='ansi')
sovpad = open('text2.txt', mode='r', encoding='ansi')
final = open('result.txt', mode='w', encoding='ansi')
finalr = open('result.txt', mode='r', encoding='ansi')
stoch1 = open('stoch.txt', mode='w', encoding='ansi')
stoch2 = open('stoch.txt', mode='r', encoding='ansi')
#beztch1 = open('beztch.txt', mode='w', encoding='ansi')

for line1 in short.readlines():
    socr = line1.split()
for line2 in source.readlines():
    razdel = line2.split()

for s1 in razdel:
    if s1 in socr:
        stoch1.write(s1 + ' ')
#        s22 = s1.replace(".", " ")
#        beztch1.write(s22 + ' ')
stoch1.close()
#beztch1.close()

for line3 in stoch2.readlines():
    stch = line3.split()

for t in stch:
    for i in range(len(razdel)):
        razdel[i] = razdel[i].replace(t, t[:(len(t)-1)])

for line4 in razdel:
    razdel2 = " ".join(razdel)
result1.write(razdel2)
result1.close()

sovpad2 = [line.strip() for line in sovpad]

regex = r"(?![\.]\s+)(?![^\.]\s+[\(\"`'»])([\"\`\']?[А-ЯA-Zа-я«\d][^\.\!\?]*(.)*?)(?=[\.\!\?](\s|\Z))"
allres = re.findall(regex, str(sovpad2))
allres2 = list(allres)
for item in allres2:
    for item2 in item:
        if len(item2)>1:
            item3=item2.split("\n")
            for item4 in item3:
                final.write("%s\n" % str(item4 + "."))
final.close()
'''
beztch2 = open('beztch.txt', mode='r', encoding='ansi')

for line6 in beztch2.readlines():
    beztch = line6.split()

for line7 in finalr.readlines():
    fin1 = line7.split()

    for t2 in beztch:
        for i in range(len(fin1)):
            fin1[i] =fin1[i].replace(t2 + ' ', t2 + '.')
'''

source.close()
short.close()
result1.close()
sovpad.close()

