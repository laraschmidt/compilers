import sys
import pylab as pl
import numpy as np
from matplotlib.pyplot import *

colors = [
    'IndianRed',
    'LimeGreen',
    'Pink',
    'LightSalmon'
]

fig = pl.figure()
fig.suptitle('Convergence', fontsize=14, fontweight='bold')
p1 = Rectangle((0, 0), 1, 1, fc="IndianRed")

p2 = Rectangle((0, 0), 1, 1, fc="LimeGreen")

p3 = Rectangle((0, 0), 1, 1, fc="Pink")

p4 = Rectangle((0, 0), 1, 1, fc="LightSalmon")
legend([p1, p2, p3 ,p4], ["Full Execution", "Opt Execution", "Full Compilation", "Opt Compilation"])

inputfile = open(sys.argv[1],"r")
outputfile = open(sys.argv[2], "w")
Full_compilation_ms = 0
Opt_compilation_ms = 0
Full_execution_ms = 0
Opt_execution_ms = 0
Full_compilation_us = 0
Opt_compilation_us = 0
Full_execution_us = 0
Opt_execution_us = 0
lastexec = 0
start = 0
end = 0
for line in inputfile:
    linearray = line.split();
    if len(linearray)<6 :
        continue
    try:
        if (linearray[0]=='Esha_time' and linearray[2]=='execution') :
            if linearray[1]=='Full' :
                if lastexec != 0:
                    times = list(xrange(start,end+1,1))
                    x = np.linspace(times[0], times[-1], 2) 
                    pl.fill_between(x, 25-(lastexec*5), 30-(lastexec*5), lw=0, color=colors[lastexec])
                    lastexec = 0
                    start = end
                Full_execution_ms+=int(float(Full_execution_us)/1000)
                Full_execution_us%=1000
                Full_execution_us+=int(linearray[5])
                end = end + Full_execution_us
            else:
                if lastexec != 1:
                    times = list(xrange(start,end+1,1))
                    x = np.linspace(times[0], times[-1], 2) 
                    pl.fill_between(x, 25-(lastexec*5), 30-(lastexec*5), lw=0, color=colors[lastexec])
                    lastexec = 1
                    start = end
                Opt_execution_ms+=int(float(Opt_execution_us)/1000)
                Opt_execution_us%=1000
                Opt_execution_us+=int(linearray[5])
                end = end + Opt_execution_us
    
        if (linearray[0]=='Esha_time' and linearray[2]=='compilation'):
            if len(linearray)<7 :
                continue
            if linearray[1]=='Full':
                if lastexec != 2:
                    times = list(xrange(start,end+1,1))
                    x = np.linspace(times[0], times[-1], 2) 
                    pl.fill_between(x, 25-(lastexec*5), 30-(lastexec*5), lw=0, color=colors[lastexec])
                    lastexec = 2
                    start = end
                Full_compilation_ms+=int(float(Full_compilation_us)/1000)
                Full_compilation_us%=1000
                Full_compilation_us+=int(linearray[6])
                end = end + Full_compilation_us
            else:
                if lastexec != 3:                    
                    times = list(xrange(start,end+1,1))
                    x = np.linspace(times[0], times[-1], 2) 
                    pl.fill_between(x, 25-(lastexec*5), 30-(lastexec*5), lw=0, color=colors[lastexec])
                    lastexec = 3
                    start = end
                Opt_compilation_ms+=int(float(Opt_compilation_us)/1000)
                Opt_compilation_us%=1000
                Opt_compilation_us+=int(linearray[6])
                end = end + Opt_compilation_us
    except ValueError:
        continue
pl.ylim([5,40])
pl.grid(True)
savefig('foo.png', bbox_inches='tight')
outputfile.writelines("Full compilation time is ")
outputfile.write('%d ms  %d us \n' %(Full_compilation_ms,Full_compilation_us))
outputfile.writelines("Full execution time is ")
outputfile.write('%d ms  %d us \n' %(Full_execution_ms, Full_execution_us))
outputfile.writelines("Opt compilation time is ")
outputfile.write('%d ms  %d us \n' %(Opt_compilation_ms,Opt_compilation_us))
outputfile.writelines("Opt execution time is ")
outputfile.write('%d ms  %d us \n' %(Opt_execution_ms,Opt_execution_us))
outputfile.writelines("Total execution time is ")
Total_us=Full_compilation_us+Full_execution_us+Opt_compilation_us+Opt_execution_us
Total_ms = Full_compilation_ms+Full_execution_ms+Opt_compilation_ms+Opt_execution_ms+Total_us/1000
Total_us = Total_us%100
outputfile.write('%d ms  %d us \n' %(Total_ms,Total_us))

inputfile.close()
outputfile.close()
