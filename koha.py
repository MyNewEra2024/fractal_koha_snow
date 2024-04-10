import matplotlib.pyplot as plt

def koch_square(ax, start, end, level):
    if level == 0:
        ax.plot([start[0], end[0]], [start[1], end[1]], color='b')
        return

    x_ = (start[0] + end[0]) / 2
    y_ = (start[1] + end[1]) / 2

    alf_1 = (((x_ - start[0]) * 0.47) / 0.5) + start[0]
    bet_1 = (((y_ - start[1]) * 0.47) / 0.5) + start[1]

    alf_2 = ((-0.47 * (end[0] - x_)) / 0.5) + end[0]
    bet_2 = ((-0.47 * (end[1] - y_)) / 0.5) + end[1]

    alf_3 = x_ - (start[1] - bet_1)
    bet_3 = y_ + start[0] - alf_1

    koch_square(ax, start, (alf_1, bet_1), level - 1)
    koch_square(ax, (alf_1, bet_1), (alf_3, bet_3), level - 1)
    koch_square(ax, (alf_3, bet_3), (alf_2, bet_2), level - 1)
    koch_square(ax, (alf_2, bet_2), end, level - 1)

def draw_koch_square(ax):
    n = 4
    x = [0, 0, 300, 300]
    y = [0, 300, 300, 0]

    for i in range(4):
        if i < 3:
            koch_square(ax, (x[i], y[i]), (x[(i + 1) % 4], y[(i + 1) % 4]), n)
        else:
            koch_square(ax, (x[i], y[i]), (x[0], y[0]), n)

fig, ax = plt.subplots()
draw_koch_square(ax)
ax.set_aspect('equal')
plt.show()