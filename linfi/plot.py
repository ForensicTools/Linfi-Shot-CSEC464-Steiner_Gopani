#!/usr/bin/python3

import pylab
import pandas
import math
import matplotlib.cm as cm



# read file
df = pandas.read_csv('ausearchOut',  error_bad_lines=False)


df.columns = ['NODE', 'EVENT','DATE','TIME','SERIAL_NUM','EVENT_KIND','SESSION','SUBJ_PRIME','SUBJ_SEC','SUBJ_KIND','ACTION','RESULT','OBJ_PRIME','OBJ_SEC','OBJ_KIND','HOW']

col_list = ['TIME','OBJ_PRIME','HOW']

df=df[col_list]

print(len(df))
row_count = len(df)
i = 0
# TIME, OBJ_PRIME, HOW


time = []
fil = []
proc = []

procSet = set()
legend = {}


while i < row_count:

    time.append(df.TIME[i])  
    fil.append(str(df.OBJ_PRIME[i]))
    if not isinstance(df.TIME[i], str):
        if math.isnan(df.TIME[i]):
            time.append("1")
    if not isinstance(df.OBJ_PRIME[i], str):
        if math.isnan(df.OBJ_PRIME[i]):
            fil.append("nan")
    if not isinstance(df.HOW[i], str):
        if math.isnan(df.HOW[i]):
            proc.append("nan")
            procSet.add("nan")
    else:
        
        #time.append(df.TIME[i])
        #fil.append(df.OBJ_PRIME[i])
        proc.append(df.HOW[i])
        procSet.add(df.HOW[i])

    i=i+1


pylab.figure(1)
#pylab.xticks(range(row_count), time)
#pylab.plot(range(row_count), fil, "g")

#colors = cm.rainbow(range(len(procSet)))
colors = ['r', 'g', 'b', 'g', 'y']
# make color legend
#for p, c in zip(procSet, colors):
#    legend[p]=c


i=0
for p in procSet:
    legend[p] = colors[i%len(colors)]
    i=i+1

print("Legend")
print(legend)
i=0
while i<len(time):
    
    pylab.scatter(time[i], fil[i], color=legend[proc[i]], label=proc[i])
    i=i+1


# apply settings to graph
pylab.grid(True)

pylab.xlabel('Time')
pylab.ylabel('File')

pylab.show()

