def solve():
    try:
        raw = input("Enter time units (n): ").strip()
        n = int(raw)
        if n < 0:
            print("Time must be non-negative.")
            return
    except Exception:
        print("Please enter a valid integer for time.")
        return

    items = [
        ('T', 5, 1500),  # Theatre
        ('P', 4, 1000),  # Pub
        ('C', 10, 3000), # Commercial Park
    ]

   
    NEG = -10**18
    dp = [NEG] * (n + 1)
    prev = [(-1, -1)] * (n + 1)  
    dp[0] = 0

    # Iterate finish times from 0..n; add any item that fits
    for t in range(n + 1):
        if dp[t] == NEG:
            continue
        for i, (_, cost, earn) in enumerate(items):
            nt = t + cost
            if nt <= n:
                val = dp[t] + earn * (n - nt)
                if val > dp[nt]:
                    dp[nt] = val
                    prev[nt] = (t, i)

    # Best profit is max over all finish times <= n (idle time allowed at end)
    best_t = max(range(n + 1), key=lambda x: dp[x])
    best_profit = dp[best_t]
    if best_profit < 0:
        best_profit = 0
        counts = {'T': 0, 'P': 0, 'C': 0}
    else:
        counts = {'T': 0, 'P': 0, 'C': 0}
        t = best_t
        while t > 0 and prev[t][0] != -1:
            pt, idx = prev[t]
            code, cost, _ = items[idx]
            counts[code] += 1
            t = pt

    print(f"Earnings: ${best_profit}")
    print(f"T: {counts['T']} P: {counts['P']} C: {counts['C']}")

if __name__ == "__main__":
    solve()
