entrada = list(map(int, input().split()))

t1 = entrada[1]-entrada[0]
t2 = entrada[2]-entrada[1]

if (t1<0 and t2>=0) or (t1>0 and t2>=t1) or (t1<0 and t2>t1) or (t1==0 and t2>0):
    print(":)")
else:
    print(":(")