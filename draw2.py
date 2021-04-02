import matplotlib.pyplot as plt
import scipy.signal as spsig
import numpy as np

def read_data(path):
    _fp = open(path, "r")
    _xlst = []
    _ylst = []

    for i in range(5):
        _fp.readline()

    _cnt = int(_fp.readline())

    for i in range(_cnt):
        _l = _fp.readline().split()
        _xlst.append(int(_l[0]))
        _ylst.append(int(_l[1]))

    # background
    _bg = min(_ylst)
    for i in range(_cnt):
        _ylst[i] -= _bg
    
    # find peaks
    #_peakind = spsig.find_peaks_cwt(_ylst,widths=np.arange(10,500))
    _peakind = []
    _fp.close()
    return _xlst, _ylst, _peakind

x4a,y4a,p4a = read_data("data/101.dat")
x0a,y0a,p0a = read_data("data/102.dat")
x5a,y5a,p5a = read_data("data/103.dat")
x5s,y5s,p5s = read_data("data/104.dat")
x5p,y5p,p5p = read_data("data/105.dat")
x5ps,y5ps,p5ps = read_data("data/106.dat")
x4p,y4p,p4p = read_data("data/107.dat")
x4s,y4s,p4s = read_data("data/108.dat")

xdl = [x0a,x4a,x4p,x4s,x5a,x5p,x5s,x5ps]
ydl = [y0a,y4a,y4p,y4s,y5a,y5p,y5s,y5ps]
pdl = [p0a,p4a,p4p,p4s,p5a,p5p,p5s,p5ps]

# Find peaks manually
pdl = [
    [736, 1557],
    [492,550,611,672,731,791,853,902,967,1317,1377,1436,1497,1556,1616,1678,1729,1790],
    [654,712,771,1478,1538,1595],
    [466,530,585,836,891,963,1291,1355,1411,1660,1716,1787],
    [428,509,578,651,728,802,881,953,1037,1251,1331,1401,1474,1551,1624,1704,1775,1860],
    [640,716,789,1467,1543,1616],
    [420,497,571,870,944,1028,1248,1324,1396,1696,1768,1853],
    [639,713,786,1463,1539,1612]
]


for i in range(8):
    plt.plot(xdl[i],ydl[i])
    plt.scatter([xdl[i][pind-xdl[i][0]] for pind in pdl[i]],[ydl[i][pind-xdl[i][0]] for pind in pdl[i]],color="red",marker="x")
    plt.show()




plt.plot(xdl[0],np.array(ydl[0])/1000,label="I=0",color="blue")
plt.scatter([xdl[0][pind-xdl[0][0]] for pind in pdl[0]],[ydl[0][pind-xdl[0][0]]/1000 for pind in pdl[0]],color="red",marker="x")

plt.plot(xdl[1],np.array(ydl[1])/1000+1.4,label="I=4.01A",color="green")
plt.scatter([xdl[1][pind-xdl[1][0]] for pind in pdl[1]],[ydl[1][pind-xdl[1][0]]/1000+1.4 for pind in pdl[1]],color="red",marker="x")

plt.plot(xdl[4],np.array(ydl[4])/1000+2.0,label="I=5.01A",color="skyblue")
plt.scatter([xdl[4][pind-xdl[4][0]] for pind in pdl[4]],[ydl[4][pind-xdl[4][0]]/1000+2.0 for pind in pdl[4]],color="red",marker="x")

plt.xlabel("X/mV")
plt.ylabel("Y-Y0")
plt.legend()
plt.show()


plt.plot(xdl[1],np.array(ydl[1])/1000,label="All",color="blue")
plt.scatter([xdl[1][pind-xdl[1][0]] for pind in pdl[1]],[ydl[1][pind-xdl[1][0]]/1000 for pind in pdl[1]],color="red",marker="x")

plt.plot(xdl[2],np.array(ydl[2])/1000+0.5,label=r"$\pi$",color="green")
plt.scatter([xdl[2][pind-xdl[2][0]] for pind in pdl[2]],[ydl[2][pind-xdl[2][0]]/1000+0.5 for pind in pdl[2]],color="red",marker="x")

plt.plot(xdl[3],np.array(ydl[3])/1000+1.0,label=r"$\sigma$",color="skyblue")
plt.scatter([xdl[3][pind-xdl[3][0]] for pind in pdl[3]],[ydl[3][pind-xdl[3][0]]/1000+1.0 for pind in pdl[3]],color="red",marker="x")

plt.xlabel("X/mV")
plt.ylabel("Y-Y0")
plt.legend()
plt.show()


plt.plot(xdl[4],np.array(ydl[4])/1000,label="All",color="blue")
plt.scatter([xdl[4][pind-xdl[4][0]] for pind in pdl[4]],[ydl[4][pind-xdl[4][0]]/1000 for pind in pdl[4]],color="red",marker="x")

plt.plot(xdl[5],np.array(ydl[5])/1000+0.7,label=r"$\pi$",color="green")
plt.scatter([xdl[5][pind-xdl[5][0]] for pind in pdl[5]],[ydl[5][pind-xdl[5][0]]/1000+0.7 for pind in pdl[5]],color="red",marker="x")

plt.plot(xdl[6],np.array(ydl[6])/1000+1.4,label=r"$\sigma$",color="skyblue")
plt.scatter([xdl[6][pind-xdl[6][0]] for pind in pdl[6]],[ydl[6][pind-xdl[6][0]]/1000+1.4 for pind in pdl[6]],color="red",marker="x")

plt.xlabel("X/mV")
plt.ylabel("Y-Y0")
plt.legend()
plt.show()


for i in range(8):
    print("analysis of %d-th data" % (i+1))
    
    if i == 0:
        print("vR")
        vR=(pdl[i][1]-pdl[i][0])
        print(vR)
        print("factor")
        factor=-2.5/vR
        print(factor)
    if i in [1,4]:
        print("vR")
        vR=(pdl[i][13]-pdl[i][4])
        print(vR)
        print("factor")
        factor=-2.5/vR
        print(factor)
    if i in [2,5,7]:
        print("vR")
        vR=(pdl[i][4]-pdl[i][1])
        print(vR)
        print("factor")
        factor=-2.5/vR
        print(factor)
    if i in [3,6]:
        print("vR")
        vR=((pdl[i][8]-pdl[i][2])+(pdl[i][9]-pdl[i][3]))/2
        print(vR)
        print("factor")
        factor=-2.5/vR
        print(factor)

    print("peaks of %d-th data"%(i+1))
    lx = [xdl[i][pind-xdl[i][0]] for pind in pdl[i]]
    ly = [ydl[i][pind-xdl[i][0]] for pind in pdl[i]]
    if i == 0:
        for j in range(len(lx)):
            print(lx[j],ly[j])
    if i in [1,4]:
        lx1 = lx[:9]
        lx2 = lx[9:]
        ly1 = ly[:9]
        ly2 = ly[9:]
        p1 = lx[4]
        p2 = lx[13]
        ld1 = [xi - p1 for xi in lx1]
        ld2 = [xi - p2 for xi in lx2]
        ld = ld1 + ld2
        nd = [li * factor for li in ld]
        for j in range(len(lx)):
            print(lx[j],ly[j],ld[j],nd[j])
    if i in [2,5,7]:
        lx1 = lx[:3]
        lx2 = lx[3:]
        ly1 = ly[:3]
        ly2 = ly[3:]
        p1 = lx[1]
        p2 = lx[4]
        ld1 = [xi - p1 for xi in lx1]
        ld2 = [xi - p2 for xi in lx2]
        ld = ld1 + ld2
        nd = [li * factor for li in ld]
        for j in range(len(lx)):
            print(lx[j],ly[j],ld[j],nd[j])
    if i in [3.6]:
        lx1 = lx[:6]
        lx2 = lx[6:]
        ly1 = ly[:6]
        ly2 = ly[6:]
        p1 = (lx[2]+lx[3])/2
        p2 = (lx[8]+lx[9])/2
        ld1 = [xi - p1 for xi in lx1]
        ld2 = [xi - p2 for xi in lx2]
        ld = ld1 + ld2
        nd = [li * factor for li in ld]
        for j in range(len(lx)):
            print(lx[j],ly[j],ld[j],nd[j])

fp = open("lorentz.in","r")
sxlst1 = []
sylst1 = []
sxlst2 = []
sylst2 = []
for i in range(18):
    st = fp.readline().split()
    sylst1.append(float(st[0]))
    sxlst1.append(float(st[1]))
fp.readline()
for i in range(18):
    st = fp.readline().split()
    sylst2.append(float(st[0]))
    sxlst2.append(float(st[1]))
fp.close()
