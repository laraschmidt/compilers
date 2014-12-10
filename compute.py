import math
import numpy
count = 0;
exect = [];
ocomp = [];
fcomp = [];
overhead = [];

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
      
for i in [exect, ocomp, fcomp, overhead]:
  print numpy.average(i), " +/- " , numpy.std(i);
      
      
