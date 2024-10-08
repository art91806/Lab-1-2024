plot_list = [[0 for i in range(10)] for i in range(10)]
yresult = [0 for i in range(10)]
xresult = [0 for i in range(10)]

i = 0
for x in range(100):
    if x%3 == 0:
        yresult[i] = x / 3
        xresult[i] = x
        i += 1
    if i >= 10:
        break


step = round(abs(yresult[0] - yresult[9]) / 9, 2)

for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][j] = step * (8-i) + step



for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - yresult[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k+1] = 25



for i in range(len(plot_list)):
    plot_list[i][0] = round(plot_list[i][0])



for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(int(plot_list[i][j])) + '\t'
        elif plot_list[i][j] == 0:
            line += '---'
        else:
            line += '!!'
    print(line)

final = ""
for i in range(1,10):
    final = final + str(xresult[i]) + " "
print('\t0\t'f'{final}')