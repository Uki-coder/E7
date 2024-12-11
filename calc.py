import scipy as sp
import matplotlib.pyplot as plt
import numpy as np

def linear(x, a, b):
    return b * x + a

def fun(x, mu, n, I, L, R):
    a = x + 0.5*L
    b = x - 0.5*L
    return (mu*n*I/(2*L)) * ( (a/np.sqrt((R**2) + a**2)) - (b/np.sqrt((R**2) + (b**2))) )

def calc(input_bzb, input_bzz, input_bib, input_bii,\
         output_bi, output_mu, output_errors, r, n, l, i0):
    bz = np.loadtxt(input_bzb)
    z = np.loadtxt(input_bzz)
    z -= 220

    bi = np.loadtxt(input_bib)
    i = np.loadtxt(input_bii)

    z_linspace = np.linspace(z[0] + 20, z[-1] -20, 1000)
    i_linspace = np.linspace(i[0] - i0*0.05, i[-1]+i0*0.05, 1000)

    plt.rcParams['text.usetex'] = True

    fig, ax = plt.subplots()
    ax.set_xlabel('$z$ [mm]')
    ax.set_ylabel('$B$ [mT]')
    plt.grid(True)

    ax.errorbar(z, bz, xerr=1, yerr=0.01, color='red', label = 'pomiary', fmt='.')
    ax.plot(z_linspace, -fun(z_linspace/1000, mu=4 * np.pi * 10 ** -7, n=n, I=i0, L=l/1000, R=r/1000)*1000, color='blue', label = 'oczekiwana zależność $B(z)$')
    ax.legend(loc='best')
    plt.show()

    ######################################################

    fig, ax = plt.subplots()
    ax.set_xlabel('$I$ [A]')
    ax.set_ylabel('$B$ [mT]')
    plt.grid(True)

    res = sp.stats.linregress(i, bi/1000)
    mu = res.slope * (l/1000)/n
    error_mu = l/1000*res.stderr/n + res.slope*0.001/n

    ''''
    with open(output_mu, 'w+') as f:
        f.write(str(mu)  + 'pm' + str(error_mu))

    with open(output_errors, 'w+') as f:
        f.write('slope: ' + str(res.stderr) \
               + '\n intercept: ' + str(res.intercept_stderr))

    with open(output_bi) as f:
        f.write('slope: ' + str(res.slope) \
               + '\n intercept: ' + str(res.intercept))
    '''

    np.savetxt(output_bi, np.array([res.slope, res.intercept]))
    np.savetxt(output_mu, np.array([mu, error_mu]))
    np.savetxt(output_errors, np.array([res.stderr, res.intercept_stderr]))


    ax.errorbar(i,bi, xerr = 0.01, yerr = 0.01, color = 'red', label = 'pomiary', fmt='.')
    ax.plot(i_linspace, linear(i_linspace, res.intercept, res.slope)* 1000,\
            color = 'blue', label = 'dopasowana prosta')
    ax.legend(loc='best')
    plt.show()

