import matplotlib.pyplot as plt
fig = plt.figure(figsize=(11, 8.5))
ax = fig.add_subplot(1, 1, 1)
import numpy as np
sin, exp, sqrt, pi, arange = np.sin, np.exp, np.sqrt, np.pi, np.arange

L = 2
g = .8
K = .7


def fn(U, n):
    fn_ = U ** 2 * g * sqrt(L / 2) * \
          (2 - sin(2 * pi * n) / pi / n)
    #fn_ = sin(2 * pi * n) / pi / n
    return fn_


def ln(U, n):
    return U ** 2 + (2 * pi * n / L) ** 2


def eta(t, U, terms):
    eta_ = 0
    for n in range(1, terms + 1):
        eta_ += fn(U, n) / ln(U, n) * (1 - exp(-ln(U, n) * K * t)) * \
                sqrt(2 / L) * (L / 2 / pi / n * sin(2 * pi * n) - L)
    eta_ += g * L
    return eta_


tmin = 0.0
tmax = 0.1
timeresolution = 100
dt = (tmax - tmin) / timeresolution

tl = list(arange(tmin, tmax, dt))
nl = arange(0,3*pi, .01)

for (U, color) in zip([1, 2, 5], ['k--', 'k-', 'k-.']):
    etal = [eta(t, U, 20) for t in tl]
    ax.plot(tl, etal, color, label=r'$U=%i$' % U)
    lnl = [ln(U, n) for n in nl]
    fnl = [fn(U, n) for n in nl]
    #ax.plot(nl, fnl)

ax.legend()
ax.set_title('hw6, no 7.3')
filename = 'hw6_7.3.pdf'
print 'saving', filename
fig.savefig(filename)
#plt.show()
