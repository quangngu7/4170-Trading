import numpy

data = numpy.array([[7,53,183,439,863,497,383,563,79,973,287,63,343,169,583],
[627,343,773,959,943,767,473,103,699,303,957,703,583,639,913],
[447,283,463,29,23,487,463,993,119,883,327,493,423,159,743],
[217,623,3,399,853,407,103,983,89,463,290,516,212,462,350],
[960,376,682,962,300,780,486,502,912,800,250,346,172,812,350],
[870,456,192,162,593,473,915,45,989,873,823,965,425,329,803],
[973,965,905,919,133,673,665,235,509,613,673,815,165,992,326],
[322,148,972,962,286,255,941,541,265,323,925,281,601,95,973],
[445,721,11,525,473,65,511,164,138,672,18,428,154,448,848],
[414,456,310,312,798,104,566,520,302,248,694,976,430,392,198],
[184,829,373,181,631,101,969,613,840,740,778,458,284,760,390],
[821,461,843,513,17,901,711,993,293,157,274,94,192,156,574],
[34,124,4,878,450,476,712,914,838,669,875,299,823,329,699],
[815,559,813,459,522,788,168,586,966,232,308,833,251,631,107],
[813,883,451,509,615,77,281,613,459,205,380,274,302,35,805]])

# =============================================================================
# data = numpy.array([[7,53,183,439,863],
# [497,383,563,79,973],
# [287,63,343,169,583],
# [627,343,773,959,943],
# [767,473,103,699,303]])
# =============================================================================

# The Hungarian algorithm gives the min. while the problem asks for the max.
# To account for this, simply multiply all the data by -1 and minimize
# This will be the same as finding the max
data = -1*data

# Params
N = data.shape[0]
# Selected Entries
Sel = numpy.zeros_like(data,dtype=bool)
# Unassigned zeros
UA0 = numpy.zeros_like(data,dtype=bool)
# Mask
Mask = numpy.zeros_like(data,dtype=bool)
# Variable to keep track of new assignment selection
Newsel = numpy.array([-1,-1])
NewUA = numpy.array([-1,-1])

# Step 1
S1 = numpy.zeros_like(data)
for i in range(0,N):
    S1[i,:] = data[i,:]-numpy.min(data[i,:])
    ix = numpy.where(S1[i,:]==0)[0][0]
    Sel[i,ix] = True

for i in range(0,N):
    if (numpy.sum(Sel[:,i])>1):
        ix = numpy.where(Sel[:,i]==True)[0][1:]
        Sel[ix,i] = False
        UA0[ix,i] = True

# Step 2
S2 = numpy.zeros_like(data)
for i in range(0,N):
    S2[:,i] = S1[:,i]-numpy.min(S1[:,i])

# Step 3
St = S2

while (UA0.any()==True):
    # Marked Entries
    Mark = numpy.ones_like(data,dtype=bool)
    for i in range(N):
        if (any(Sel[i,:])==True):
            Mark[i,:] = False
    
    for i in range(N):
        if (any(Sel[:,i]) and any(UA0[:,i])):
            if (Newsel[0]==-1):
                ix = numpy.where(Sel[:,i]==True)[0][0]
                Newsel = numpy.array([ix,i])
                NewUA = Newsel
            Mark[:,Newsel[1]] = False
            Mark[NewUA[0],:Newsel[1]] = True
    
    Temp = St+~Mark*10e5
    St = St-Mark*numpy.min(Temp)+~Mark*10e5
    
    for i in range(N):
        if (any(St[i,:]==0)):
            ix = numpy.where(St[i,:]==0)[0][0]
            Sel[i,ix] = True
            UA0[i,:] = False
            Newsel = [i,ix]
            
    for i in range(N):
        if (any(UA0[:,i]==True)):
            ix = numpy.where(UA0[:,i]==True)[0][0]
            NewUA = [ix,i]

print('Max = '+str(-numpy.sum(data*Sel)))



