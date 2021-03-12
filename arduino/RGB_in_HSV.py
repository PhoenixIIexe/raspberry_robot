def hsv(RGB):
    RGB = [RGB[i] / 255 for i in range(3)]
    MAX = max(RGB)
    MIN = min(RGB)

    try:
        if MAX == RGB[0] and RGB[1] >= RGB[2]:
            H = 60 * (RGB[1] - RGB[2]) / (MAX - MIN)
        elif MAX == RGB[0] and RGB[1] < RGB[2]:
            H = 60 * (RGB[1] - RGB[2]) / (MAX - MIN) + 360
        elif MAX == RGB[1]:
            H = 60 * (RGB[2] - RGB[0]) / (MAX - MIN) + 120
        elif MAX == RGB[2]:
            H = 60 * (RGB[0] - RGB[1]) / (MAX - MIN) + 240
    except ZeroDivisionError:
        H = 0

    if MAX == 0:
        S = 0
    else:
        S = 1 - MIN / MAX

    V = MAX

    return [round(H, 2), round(S, 2), round(V, 2)]
