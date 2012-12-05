from numpy import sin, exp, cos, pi, arange, array
import matplotlib.pyplot as plt

def A(m, P):
    '''Coeffecients of cosines in Fourier solution.'''
    A_ = -4 * P**2 * sin(pi*m/2) * 2 * m / (pi*m/2)**2 / (pi*m + sin(pi*m))**2
    return A_


def um(x, terms, P):
    m_list = list(arange(1, terms * 2, 2))
    solution = 0
    components = []
    for m in m_list:
        component = A(m, P) * cos(x * pi * m / 2)
        components.append(component)
        solution += component
    solution += 1
    return (solution, components)


def u(x, P):
    solution = (exp(P * x) + exp(-P * x)) / (exp(P) + exp(-P))
    return solution


terms = 4
fig = plt.figure(1, figsize=(11, 8.5))
ax = fig.add_subplot(1, 1, 1)
for (P, color, marker) in zip([0.1, 1, 5], ['k-', 'k--', 'k-.'], ['o', 's', 'd']):
    xl = list(arange(0, 1, 0.01))
    ul = []
    uml = []
    uml_components = []
    for x in xl:
        ul.append(u(x, P))
        (um_val, um_components) = um(x, terms, P)
        uml.append(um_val)
        uml_components.append(um_components)
    ax.plot(xl, ul, color, label=r'$\phi=%.1f$, analytical' % P)
    uml_components = array(uml_components)  # first index is x; second is component
    ax.scatter(xl, uml, label=r'$\phi=%.1f$, %i fourier terms' % (P, terms), facecolor='k', marker=marker)
ax.legend(loc='lower right')
ax.set_xlim((0, 1))
#ax.set_ylim((-1, 1))
ax.set_xlabel(r'$x$, distance from slab centerline')
ax.set_ylabel(r'$u$, dimensionless reactant concentration')
ax.set_title('hw6, no 3.26')
filename = 'hw6_3.26.pdf'
print 'saving', filename
fig.savefig(filename)
#plt.show()
