from sympy import *
init_printing()
x, y, t= symbols("x, y, t")
u,v=symbols("u, v")
tau = symbols("tau")
g = Function("g_k")
a1k = Function("a_{1,k}")
a2k = Function("a_{2,k}")
Ak = Function("A_k")

gfunc = g(x,y,t)
a1f = a1k(x,y,t)
a2f = a2k(x,y,t)
Akf = Ak(x,y,t)

fNS = gfunc - tau*(a1f*u+a2f*v+Akf)*gfunc
d_fNS_x = diff(fNS, x)
d_fNS_y = diff(fNS, y)
d_fNS_x2 = diff(d_fNS_x, x)
d_fNS_xy = diff(d_fNS_x, y)
d_fNS_y2 = diff(d_fNS_y, y)

"""
print(latex(fNS))
print('\n')
preview(fNS)

print(latex(d_fNS_x))
print('\n')
preview(d_fNS_x)

print(latex(d_fNS_y))
print('\n')
preview(d_fNS_y)

print(latex(d_fNS_x2))
print('\n')
preview(d_fNS_x2)

print(latex(d_fNS_xy))
print('\n')
preview(d_fNS_xy)


print(latex(d_fNS_y2))
print('\n')
preview(d_fNS_y2)
"""

x = -u*t
dfx = d_fNS_x*x
dfy = (y-u*t)*d_fNS_y

dfx=simplify(dfx)
preview(dfx)

dfy=simplify(dfy)
preview(dfy)


