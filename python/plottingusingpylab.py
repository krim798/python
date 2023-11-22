#basic graph plotting using pylab
import pylab as plt
mySamples=[]
myLinear=[]
myQuadratic=[]
myCubic=[]
myExponential=[]

for i in range(0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
plt.figure("lin")
plt.plot(mySamples,myLinear,'b-',label="linear",linewidth=2.0)
plt.legend(loc='upper left')
plt.ylim(0,1000)
plt.xlabel("samples")
plt.ylabel("Linear")
plt.title("Linear fn")

plt.figure("quad")
plt.plot(mySamples,myQuadratic,'ro',label='Quadratic',linewidth=3.0)
plt.title("Quad fn")
plt.ylim(0,1000)
plt.legend()
plt.xlabel("Samples")
plt.ylabel("Quadratic")

plt.figure("cubic")
plt.plot(mySamples,myCubic,'g^',label='Cubic',linewidth=4.0)
plt.title("Cubic fn")
plt.legend()
plt.xlabel("Samples")
plt.ylabel("Cubic")

plt.figure("exponential")
plt.plot(mySamples,myExponential,'r--',label='exponential',linewidth=5.0)
plt.xlabel("Sample")
plt.yscale('log')
plt.title("Expo fn")
plt.legend()
plt.ylabel("exponential")

plt.figure("lin quad")
plt.clf()
plt.subplot(211)
plt.ylim(0,1000)
plt.plot(mySamples,myLinear,'b-',label="linear",linewidth=2.0)
plt.legend(loc='upper left')
plt.subplot(212)
plt.ylim(0,1000)
plt.plot(mySamples,myQuadratic,'ro',label='Quadratic',linewidth=3.0)
plt.legend()
plt.title("Quad fn")
