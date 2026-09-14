def answer() -> int:
    # The learner put a print inside a loop to see what was happening, and it
    # prints far more than the 50K the runner keeps. The green pattern is
    # printed after this returns, so it falls outside what is kept and the
    # colour is amber even though every assertion holds.
    total = 0
    for i in range(5000):
        print(f'debug: i is {i}, total is {total}')
        total += 1
    return 6 * 7
