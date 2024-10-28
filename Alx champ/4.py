# a func that returns the prime factors of a number with their exponents

def prime_factors(n):
    ans = {}
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            ans[d] = ans.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        ans[n] = ans.get(n, 0) + 1
    return ans
# Reading input
product = 1
with open("expression.in") as f:
	m = int(f.readline())
	n = int(f.readline())
	nums = list(map(int, f.readline().split()))
	
for i in nums:
    product *= i


# Writing to output:
if product **(1/m) == int(product **(1/m)):
    with open("expression.out", "w") as f:
        print(1, file=f)
        inprime = prime_factors(int(product **(1/m)))
        for i in inprime:
            print(i, inprime[i], file=f)
else:
    with open("expression.out", "w") as f:
        print(0, file=f)
	