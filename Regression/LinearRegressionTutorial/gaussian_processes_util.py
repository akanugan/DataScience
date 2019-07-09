import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def plot_gp(mu, cov, X, X_train=None, Y_train=None, samples=[]):
    X = X.ravel()
    mu = mu.ravel()
    #  1.96 is based on the fact that 95% of the area of a normal distribution is within 1.96 standard deviations of the mean
    uncertainty = 1.96 * np.sqrt(np.diag(cov))
    
    plt.fill_between(X, mu + uncertainty, mu - uncertainty, alpha=0.1)
    plt.plot(X, mu, label='Mean')
    for i, sample in enumerate(samples):
        plt.plot(X, sample, lw=1, ls='--', label=f'Sample {i+1}')
    if X_train is not None:
        plt.plot(X_train, Y_train, 'rx')
    plt.legend()

def plot_gp_2D(gx, gy, mu, X_train, Y_train, title, i):
    ax = plt.gcf().add_subplot(1, 2, i, projection='3d')
    ax.plot_surface(gx, gy, mu.reshape(gx.shape), cmap=cm.coolwarm, linewidth=0, alpha=0.2, antialiased=False)
    ax.scatter(X_train[:,0], X_train[:,1], Y_train, c=Y_train, cmap=cm.coolwarm)
    ax.set_title(title)

def plot_scatter(mu, cov, X):
    mu_val  =  mu.ravel()[0]
    sig_val =  cov.item((0,0))
    cor_coeff =  cov.item((0,X.shape[0]-1))
    plt.scatter(X, X, color='red', s=10, marker='o', label="$\mu$ ="+str(mu_val)+
                ", $s$ ="+str(round(sig_val,2))+", corr-coeff ="+str(round(cor_coeff,2)))
    plt.legend(loc='upper left')
    #plt.show()

