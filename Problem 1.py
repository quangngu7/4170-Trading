import numpy
#import matplotlib.pyplot as plt

def combocoin(targval,coinval):
    if (targval<0):
        return 0
    if (coinval.shape[0]==1):
        return 1
    else:
        N = int(numpy.floor_divide(targval,coinval[0]))+1
        out = numpy.zeros((N,))
        for i in range(N):
            out[i] = combocoin(targval-i*coinval[0],coinval[1:])
        return numpy.sum(out)

# Some preliminary tests
# =============================================================================
# coinval = numpy.array([5,1])    
# test = combocoin(25,coinval)
# 
# coinval = numpy.array([5,1])    
# test = combocoin(15,coinval)
# 
# coinval = numpy.array([5,1])    
# test = combocoin(5,coinval)
# 
# coinval = numpy.array([5,1])    
# test = combocoin(0,coinval)
# 
# coinval = numpy.array([10,5,1])    
# test = combocoin(30,coinval)
# 
# =============================================================================
coinval = numpy.array([100,50,20,10,5,1])    
print('Number of Different ways:'+str(combocoin(500,coinval)))











