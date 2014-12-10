import math
import numpy
count = 0;
exect = [];
ocomp = [];
fcomp = [];
comp = []
overhead = [];
summ = [];

with open('results') as f:
  for line in f.readlines():
    piece = line.split(" ");
    if len(piece) < 2:
      continue;
    if piece[0] == "Full":
      fcomp.append(int(piece[4]) + int(piece[7])/1000.0);
      count = count + 1;
    if piece[0] == "Opt":
      ocomp.append(int(piece[4]) + int(piece[7])/1000.0);
    if piece[0] == "Our":
      overhead.append(int(piece[4])  + int(piece[7])/1000.0);
    if piece[1] == "execution":
      exect.append(int(piece[4])  + int(piece[7])/1000.0);
      
for i in range(0,len(ocomp)):
  comp.append(fcomp[i] + ocomp[i]);
  summ.append(fcomp[i] + ocomp[i] + exect[i] + overhead[i]);   

print ocomp
print comp
print fcomp

for i in [exect, ocomp, fcomp, overhead, comp, summ]:
  print numpy.average(i), " +/- " , numpy.std(i);
      
      
