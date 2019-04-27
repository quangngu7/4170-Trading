import numpy
import matplotlib.pyplot as plt

# Let P(D=k) be the probability that a dice rolls k
PD1 = numpy.ones((10,))/10
PD2 = numpy.ones((5,))/5

# O = D1 + D1 + D1 + D1
PO = numpy.convolve(PD1,PD1)
PO = numpy.convolve(PO,PD1)
PO = numpy.convolve(PO,PD1)

# G = D2 + D2 + D2 + D2 + D2 + D2 + D2 + D2
PG = numpy.convolve(PD2,PD2)
PG = numpy.convolve(PG,PD2)
PG = numpy.convolve(PG,PD2)
PG = numpy.convolve(PG,PD2)
PG = numpy.convolve(PG,PD2)
PG = numpy.convolve(PG,PD2)
PG = numpy.convolve(PG,PD2)

# Let P(O=k) be the probability that Oberyn rolls k where 4 <= k <= 40
fig = plt.figure()
plt.grid(True)
plt.xlabel('Sum of Rolls')
plt.ylabel('pdf')
plt.title('Oberyn Roll PDF')
plt.plot(numpy.arange(4,41),PO)

# Let P(G=k) be the probability that Gregor rolls k where 8 <= k <= 40
fig = plt.figure()
plt.grid(True)
plt.xlabel('Sum of Rolls')
plt.ylabel('pdf')
plt.title('Gregor Roll PDF')
plt.plot(numpy.arange(8,41),PG)

# Probability that Gregor wins P(G>O) -> P(G-O>0)
POG = numpy.convolve(PO,PG)
fig = plt.figure()
plt.grid(True)
plt.xlabel('Sum of Rolls')
plt.ylabel('pdf')
plt.title('Gregor-Oberyn Roll PDF')
start = 8-40
X = numpy.arange(start,start+69)
plt.plot(X,POG)

# Probability that Gregor wins, we want to sum P(G-O) from 1 to 36
print('Probability that Gregor wins = '+str(numpy.sum(POG[33:])))
















