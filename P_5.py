from itertools import permutations

def solve(w1, w2, res):
    letters = list(set(w1 + w2 + res))
    if len(letters) > 10:
        print("No solution")
        return

    first_letters = {w1[0], w2[0], res[0]}

    for p in permutations(range(10), len(letters)):
        d = dict(zip(letters, p))

        if any(d[ch] == 0 for ch in first_letters):
            continue

        n1 = int(''.join(str(d[ch]) for ch in w1))
        n2 = int(''.join(str(d[ch]) for ch in w2))
        n3 = int(''.join(str(d[ch]) for ch in res))

        if n1 + n2 == n3:
            print("Solution:", d)
            print(n1, "+", n2, "=", n3)
            return

    print("No solution")

# Example
solve("SEND", "MORE", "MONEY")
