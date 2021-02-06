def my_func(a=2, b=4, c=8, d=10):
  x=(a+b+c+d)/4
  return x
print (my_func())

def st_fum(a=[2, 4, 8, 10]):
  x=sum(a)/len(a)
  return x
print (st_fum())