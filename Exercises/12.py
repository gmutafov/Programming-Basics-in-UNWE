A = float(input())
N = float(input())
i = float(input())

P = i * A / (1 - (1 + i) ** -N)

print(f"{P:.3f}")