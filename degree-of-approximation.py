#written and tested by Katie Humphreys 
print('Enter degree of angle:')
degrees = float(input())
x = (degrees * 3.1415926) / 180
sinx = x - (x**3 / (3*2*1)) + (x**5 / (5*4*3*2*1)) - (x**7 / (7*6*5*4*3*2*1))
cosx = 1 - (x**2 / (2*1)) + (x**4 / (4*3*2*1)) - (x**6 / (6*5*4*3*2*1))
tanx = x + (1/3) * (x**3) + (2/15) * (x**5) + (17/315) * (x**7)
print('The sin of x is ' + str(sinx))
print('The cos of x is ' + str(cosx))
print('The tan of x is ' + str(tanx))
