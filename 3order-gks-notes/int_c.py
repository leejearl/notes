from sympy import *
init_printing()
x, y, t, tt = symbols("x, y, t, t'")
tau = symbols("tau")
deltaT = symbols("\Delta{t}")

c1 = 1-exp(-t/tau)
int_c1 = integrate(c1, (t, 0, deltaT))
int_c1 = ratsimp(int_c1)

c2 = (t+tau)*exp(-t/tau)-tau
int_c2 = integrate(c2, (t, 0, deltaT))
int_c2 = ratsimp(int_c2)

c3 = t-tau+tau*exp(-t/tau)
int_c3 = integrate(c3, (t, 0, deltaT))
int_c3 = ratsimp(int_c3)

c4 = -exp(-t/tau)*(t**2+2*t*tau)
int_c4 = integrate(c4, (t, 0, deltaT))
int_c4 = ratsimp(int_c4)

c5 = t**2-2*tau*t
int_c5 = integrate(c5, (t, 0, deltaT))
int_c5 = ratsimp(int_c5)

c6 = -t*tau*(1+exp(-t/tau))
int_c6 = integrate(c6, (t, 0, deltaT))
int_c6 = ratsimp(int_c6)

c7 = exp(-t/tau)
int_c7 = integrate(c7, (t, 0, deltaT))
int_c7 = ratsimp(int_c7)

c8 = -t*c7
int_c8 = integrate(c8, (t, 0, deltaT))
int_c8 = ratsimp(int_c8)

c9 = t**2*c7
int_c9 = integrate(c9, (t, 0, deltaT))
int_c9 = ratsimp(int_c9)

print(latex(int_c1))
print('\n')
preview(c1)
preview(int_c1)

print(latex(int_c2))
print('\n')
preview(c2)
preview(int_c2)

print(latex(int_c3))
print('\n')
preview(c3)
preview(int_c3)

print(latex(int_c4))
print('\n')
preview(c4)
preview(int_c4)

print(latex(int_c5))
print('\n')
preview(c5)
preview(int_c5)

print(latex(int_c6))
print('\n')
preview(c6)
preview(int_c6)

print(latex(int_c7))
print('\n')
preview(c7)
preview(int_c7)

print(latex(int_c8))
print('\n')
preview(c8)
preview(int_c8)

print(latex(int_c9))
print('\n')
preview(c9)
preview(int_c9)

