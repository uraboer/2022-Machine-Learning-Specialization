import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    """
    Compute the sigmoid of z

    Parameters
    ----------
    z : array_like
        A scalar or numpy array of any size.

    Returns
    -------
     g : array_like 
         sigmoid(z)
    """
    ### END CODE HERE ###

    return 1/(1+np.exp(-z))

def plot_data(X, y):

    # Find Indices of Positive and Negative Examples
    pos = y == 1
    neg = y == 0

    # Plot examples
    plt.plot(X[pos, 0], X[pos, 1], 'r+', label="y=1")
    plt.plot(X[neg, 0], X[neg, 1], 'ko', label="y=0")