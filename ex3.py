from constant import g
def energy(m, h, v):
  U=m*h*g
  K=(m*v**2)/2
  E=U+K
  print (E)
energy(10, 8, 5)
