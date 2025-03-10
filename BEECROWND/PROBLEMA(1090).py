c1, c2, c3, t1, t2, t3, q1, q2, q3 = 0, 0, 0, 0, 0, 0, 0, 0, 0
def uma(j):
    m = 0
    global c1, c2, c3, t1, t2, t3, q1, q2, q3
    while j>=3:
        k = j
        if c1 > 0 and c2 >0 and c3 > 0:
            c1-=1
            c2-=1
            c3-=1
            m+=1
            j-=3
        if t1 > 0 and t2 >0 and t3 > 0:
            t1-=1
            t2-=1
            t3-=1
            m+=1
            j-=3
        if q1 > 0 and q2 >0 and q3 > 0:        
            q1-=1
            q2-=1
            q3-=1
            m+=1
            j-=3    
        if c1 > 0 and t2 > 0 and q3>0:
            c1 -=1
            t2-=1
            q3-=1
            m+=1
            j-=3
        if c1 > 0 and q2 > 0 and t3>0:
            c1 -=1
            q2-=1
            t3-=1
            m+=1
            j-=3
        if t1 > 0 and c2 > 0 and q3>0:
            t1 -=1
            c2-=1
            q3-=1
            m+=1
            j-=3
        if t1 > 0 and q2 > 0 and c3>0:
            t1 -=1
            q2-=1
            c3-=1
            m+=1
            j-=3
        if q1 > 0 and t2 > 0 and c3>0:
            q1 -=1
            t2-=1
            c3-=1
            m+=1
            j-=3
        if q1 > 0 and c2 > 0 and t3>0:
            q1 -=1
            c2-=1
            t3-=1
            m+=1
            j-=3
        if c1 > 2:
            c1-=3
            j-=3
            m+=1
        if c2 > 2:
            c2-=3
            j-=3
            m+=1
        if c3 > 2:
            c3 -=3
            j-=3
            m+=1
        if t1 > 2:
            t1 -=3
            j-=3
            m+=1
        if t2 > 2:
            t2 -=3
            j-=3
            m+=1
        if t3 > 2:
            t3 -=3
            j-=3
            m+=1
        if q1 > 2:
            q1 -=3
            j-=3
            m+=1
        if q2 > 2:
            q2 -=3
            j-=3
            m+=1
        if q3 > 2:
            q3 -=3
            j-=3
            m+=1
        if j == k:
            break
    return m

def duas(j):
    global c1, c2, c3, t1, t2, t3, q1, q2, q3
    m = 0
    while j>=3:
        k = j
        if c1 > 0 and t2 > 0 and q3>0:
            c1 -=1
            t2-=1
            q3-=1
            m+=1
            j-=3
        if c1 > 0 and q2 > 0 and t3>0:
            c1 -=1
            q2-=1
            t3-=1
            m+=1
            j-=3
        if t1 > 0 and c2 > 0 and q3>0:
            t1 -=1
            c2-=1
            q3-=1
            m+=1
            j-=3
        if t1 > 0 and q2 > 0 and c3>0:
            t1 -=1
            q2-=1
            c3-=1
            m+=1
            j-=3
        if q1 > 0 and t2 > 0 and c3>0:
            q1 -=1
            t2-=1
            c3-=1
            m+=1
            j-=3
        if q1 > 0 and c2 > 0 and t3>0:
            q1 -=1
            c2-=1
            t3-=1
            m+=1
            j-=3
        if c1 > 0 and c2 >0 and c3 > 0:
            c1-=1
            c2-=1
            c3-=1
            m+=1
            j-=3
        if t1 > 0 and t2 >0 and t3 > 0:
            t1-=1
            t2-=1
            t3-=1
            m+=1
            j-=3
        if q1 > 0 and q2 >0 and q3 > 0:        
            q1-=1
            q2-=1
            q3-=1
            m+=1
            j-=3    
        if c1 > 2:
            c1-=3
            j-=3
            m+=1
        if c2 > 2:
            c2-=3
            j-=3
            m+=1
        if c3 > 2:
            c3 -=3
            j-=3
            m+=1
        if t1 > 2:
            t1 -=3
            j-=3
            m+=1
        if t2 > 2:
            t2 -=3
            j-=3
            m+=1
        if t3 > 2:
            t3 -=3
            j-=3
            m+=1
        if q1 > 2:
            q1 -=3
            j-=3
            m+=1
        if q2 > 2:
            q2 -=3
            j-=3
            m+=1
        if q3 > 2:
            q3 -=3
            j-=3
            m+=1
        if j == k:
            break
    return m

def tres(j):
    m = 0
    global c1, c2, c3, t1, t2, t3, q1, q2, q3
    while j>=3:
        k = j
        if c1 > 2:
            c1-=3
            j-=3
            m+=1
        if c2 > 2:
            c2-=3
            j-=3
            m+=1
        if c3 > 2:
            c3 -=3
            j-=3
            m+=1
        if t1 > 2:
            t1 -=3
            j-=3
            m+=1
        if t2 > 2:
            t2 -=3
            j-=3
            m+=1
        if t3 > 2:
            t3 -=3
            j-=3
            m+=1
        if q1 > 2:
            q1 -=3
            j-=3
            m+=1
        if q2 > 2:
            q2 -=3
            j-=3
            m+=1
        if q3 > 2:
            q3 -=3
            j-=3
            m+=1
        if c1 > 0 and c2 >0 and c3 > 0:
            c1-=1
            c2-=1
            c3-=1
            m+=1
            j-=3
        if t1 > 0 and t2 >0 and t3 > 0:
            t1-=1
            t2-=1
            t3-=1
            m+=1
            j-=3
        if q1 > 0 and q2 >0 and q3 > 0:        
            q1-=1
            q2-=1
            q3-=1
            m+=1
            j-=3    
        if c1 > 0 and t2 > 0 and q3>0:
            c1 -=1
            t2-=1
            q3-=1
            m+=1
            j-=3
        if c1 > 0 and q2 > 0 and t3>0:
            c1 -=1
            q2-=1
            t3-=1
            m+=1
            j-=3
        if t1 > 0 and c2 > 0 and q3>0:
            t1 -=1
            c2-=1
            q3-=1
            m+=1
            j-=3
        if t1 > 0 and q2 > 0 and c3>0:
            t1 -=1
            q2-=1
            c3-=1
            m+=1
            j-=3
        if q1 > 0 and t2 > 0 and c3>0:
            q1 -=1
            t2-=1
            c3-=1
            m+=1
            j-=3
        if q1 > 0 and c2 > 0 and t3>0:
            q1 -=1
            c2-=1
            t3-=1
            m+=1
            j-=3
        if j == k:
            break
    return m
        

while True:
    n = int(input())
    if n == 0:
        break
    else:
        
        for i in range(n):
            carta = input().split()
            if carta[0] == "um":
                if carta[1] == "circulo":
                    c1 += 1
                elif carta[1] == "triangulo":
                    t1 += 1
                else:
                    q1 += 1
            elif carta[0] == 'dois':
                if carta[1] == "circulos":
                    c2 += 1
                elif carta[1] == "triangulos":
                    t2 += 1
                else:
                    q2 += 1
            else:
                if carta[1] == "circulos":
                    c3 += 1
                elif carta[1] == "triangulos":
                    t3 += 1
                else:
                    q3 += 1
            
        j = n

        m = max(uma(j), duas(j), tres(j))
        
        print(m)