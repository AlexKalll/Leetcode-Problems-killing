with open("dsum.in") as f:
	n = int(f.readline())

# To sum of digits
strn = str(n)
s = sum([int(i) for i in strn])

# Writing to output:
with open("dsum.out", "w") as f:
	print(s, file=f)