dic = {
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6,
    '0': 6
    }

x = int(input())

for _ in range(x):
    y = input()
    total = 0
    for j in y:
        total += dic[j]
    print(f"{total} leds")
    