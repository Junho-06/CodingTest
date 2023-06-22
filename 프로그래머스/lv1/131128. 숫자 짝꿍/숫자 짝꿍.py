from collections import Counter

def solution(X, Y):

    summary = []
    
    Xcount = [0] * 10
    Ycount = [0] * 10
    
    for i in X:
        Xcount[int(i)] += 1
    
    for i in Y:
        Ycount[int(i)] += 1
        
    for i in range(10):
        count = min(Xcount[i], Ycount[i])
        if count > 0:
            summary.append(str(i) * count)
    
    #시간 초과
    #Xcount = [0] * 10
    #Ycount = [0] * 10
    
    #for i in X:
        #Xcount[int(i)] += 1
    
    #for i in Y:
        #Ycount[int(i)] += 1
        
    #for i in range(10):
        #count = min(Xcount[i], Ycount[i])
        #if count > 0:
            #summary += str(i) * count
    
    #시간초과
    #X = str(X)
    #Y = str(Y)

    #Xcount = [0] * 10
    #Ycount = [0] * 10

    #for i in X:
        #Xcount[int(i)] += 1

    #for i in Y:
        #Ycount[int(i)] += 1
        
    #for i in range(10):
        #count = min(Xcount[i], Ycount[i])
        #if count > 0:
            #summary += str(i) * count


    
    #시간초과
    #Xcounter = Counter(list(X))
    #Ycounter = Counter(list(Y))
    
    #for i in range(10):
        #if Xcounter[str(i)] > 0 and Ycounter[str(i)] > 0:
            #summary += str(min(Xcounter[str(i)], Ycounter[str(i)]) * str(i))
    
    #시간초과
    #Xcounter = Counter(list(X))
    #Ycounter = Counter(list(Y))
    #leng = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    #for i in leng:
        #if Xcounter[i] > 0 and Ycounter[i] > 0:
            #if Xcounter[i] > Ycounter[i]:
                #summary += str(Ycounter[i] * str(i))
            #else:
                #summary += str(Xcounter[i] * str(i))
    
    #시간초과
    #Xlist = []
    #Ylist = []
    
    #for i in range(10):
        #Xlist.append(X.count(str(i)))
        #Ylist.append(Y.count(str(i)))
        
    #for idx, att in enumerate(Xlist):
        #if Xlist[idx] > 0 and Ylist[idx] > 0:
            #if Xlist[idx] > Ylist[idx]:
                #summary += Ylist[idx] * str(idx)
            #else:
                #summary += att * str(idx)
    
    #시간초과
    #for att in X:
        #if att in Y:
            #summary += att
            #Y = Y.replace(att, '', 1)
            #index = Y.index(att)
            #Y = Y[:index] + Y[index+1:]

            
    summary = "".join(sorted(summary, reverse=True))
        
    if len(summary) == 0:
        return "-1"
    
    if summary[0] == '0':
        return "0"

    return summary