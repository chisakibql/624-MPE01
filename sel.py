def findid(lst1,lst2):
    reslst = []
    for i in lst1:
        flg = 0
        for j in lst2:
            if i == j:
                flg = 1
                break
        if flg:
            reslst.append(i)
    return reslst

mlst = [-1,0,1]
dmlst = [-1,1]
dglst = [-1/2,1/2]
alst = [1,1.5,2]

gglst = []

for a in alst:
    print("a\tm\tdm\tdg\tg1\tg2")
    tmplst = []
    for m in mlst:
        for dm in dmlst:
            for dg in dglst:
                g2 = dm * (m*dg-a)
                g1 = g2-dg
                print(a,m,dm,dg,g1,g2)
                tmplst.append((g1,g2))
    gglst.append(tmplst)
    print("")

print(findid(findid(gglst[0],gglst[1]),gglst[2]))