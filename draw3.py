import matplotlib.pyplot as plt
import scipy.signal as spsig
import numpy as np

fp = open("lorentz.in","r")
sxlst = [2,1.5,1,0.5,0,-0.5,-1,-1.5,-2,2,1.5,1,0.5,0,-0.5,-1,-1.5,-2]
sylst1 = [-0.724,-0.548,-0.364,-0.179,0.000,0.182,0.370,0.518,0.715,-0.724,-0.542,-0.364,-0.179,0.000,0.182,0.370,0.524,0.709]
sylst2 = [-0.911,-0.665,-0.456,-0.234,0.000,0.225,0.465,0.683,0.939,-0.911,-0.668,-0.456,-0.234,0.000,0.222,0.465,0.680,0.939]

pl1= np.polyfit(sxlst,sylst1,1,full=True)
print(pl1)
p1 = np.poly1d(pl1[0])
pl2 =np.polyfit(sxlst,sylst2,1,full=True)
print(pl2)
p2 = np.poly1d(pl2[0])

plt.plot(sxlst, [p1(xi) for xi in sxlst],label="y=%fx+%f"%(pl1[0][0],pl1[0][1]))
plt.scatter(sxlst,sylst1,color="red",marker="x")
plt.xlabel(r"$\Delta (M_Jg) $")
plt.ylabel(r"$\Delta\tilde{\nu}/cm^{-1}$")
plt.title("I=4.01 A")
plt.legend()
plt.show()
plt.plot(sxlst, [p2(xi) for xi in sxlst],label="y=%fx+%f"%(pl2[0][0],pl2[0][1]))
plt.scatter(sxlst,sylst2,color="red",marker="x")
plt.xlabel(r"$\Delta (M_Jg) $")
plt.ylabel(r"$\Delta\tilde{\nu}/cm^{-1}$")
plt.title("I=5.01 A")
plt.legend()
plt.show()