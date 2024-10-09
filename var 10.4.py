f = open('sequence.txt').read().split('\n')


X = []
Y = []


for i in range(len(f)):
    if -3 <= float(f[i]) <= 3:
        X.append(float(f[i]))
    else:
        Y.append(float(f[i]))
    


xpercent = (len(X)/(len(X) + len(Y)))*100
ypercent = (len(Y)/(len(X) + len(Y)))*100


for value in range(10,0,-1):
    tabl = ""
    if value*10 <= xpercent:
        if value == 3:
            tabl += str(xpercent)
        tabl += '\t' + "***"
        tabl += '\t' + "***"
    elif value*10 > xpercent and value*10 <= ypercent:
        if value == 6:
            tabl += str(ypercent)
        tabl += '\t' + "---"
        tabl += '\t' + "***"
    else:
        tabl += '\t' + "---"
        tabl += '\t' + "---"
    print(tabl)