import random

opts="ABCDEFGHIJKLMNOPQRSTUVWXYZ012345678901234567890123456789"

for i in range(10000000):
  plate="".join(random.sample(opts, 7))
  print("{0}\tMeaningless notes about car with plate {0}".format(plate))

