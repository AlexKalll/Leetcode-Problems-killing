
with open("committee.in") as f:
	n, m = map(int, f.readline().split()) 
sumarr = []
minsum = float('inf')
maxsum = -float('inf')
minidx, maxidx = 0, 0
with open("committee.in") as f:
    for i in range(n +1):
        if i == 0:
            sumarr.append(0)
            continue
        sumarr.append(sum(map(int, f.readline().split())))
        if sumarr[i] < minsum:
              minidx = i
              minsum = sumarr[i]
        if sumarr[i] > maxsum:  
              maxidx = i
              maxsum = sumarr[i]
# Writing to output:
with open("committee.out", "w") as f:
	print(minidx , maxidx , file=f)