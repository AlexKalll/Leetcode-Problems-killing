
with open("tourney.in") as f:
    n, m = map(int, f.readline().split())
citys = {}

with open("tourney.in") as f:
    for i in range(m+1):
            if i == 0:
                status, city =  f.readline().split()
                continue
            status, city =  f.readline().split()
            city = int(city)
            if city in citys.keys():
                change = citys[city][1] + 1
                citys[city] = [f'{status}', change]
            else:
                citys[city] = [f'{status}', 1]
print(citys)

havingconcert = []
mostchange = 0
for city in citys:
    if citys[city][0] == 'D':
        havingconcert.append(city)
    if citys[city][1] > mostchange:
        mostchangecity = city
        mostchange = citys[city][1]
havingconcert.sort() 

nomessage = 0
for i in range(1, n + 1):
      if i not in citys.keys():
            nomessage += 1

# Writing to output:
with open("tourney.out", "w") as f:
    print(f'{" ".join(str(i) for i in havingconcert)}' ,  file=f)
    print(mostchangecity, file=f)
    print(nomessage, file=f)

print(havingconcert)
print(mostchangecity)
print(nomessage)