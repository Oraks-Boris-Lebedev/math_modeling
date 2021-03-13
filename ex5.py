from math import pi
def f(key=0, h=0, l=0, r=0 ,a=0, b=0):
  if key==0:
    S=(h*l)/2
  if key==1:
    S=pi*r**2
  if key==3:
    S=a*b
  print (S)
f(key=0, h=4, l=2)