import matplotlib.pyplot as ptl
import numpy as np
import pandas as pd
import scipy.stats as stats
import pymc3 as pm
import theano.tensor as tt
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

np.random.seed(1984)
%matplotlib inline

# El problema de la moneda
# de 100 lanzamientos 80 caras

n = 100
caras = 80

# Creamos el modelo
niter = 2000
with pm.Model() as modelo_moneda:
    # a_priori
    p = pm.Beta("p", alpha=2, beta=2)
    # likelihood
    y = pm.Binomial("y", n=n, p=p, observed=caras)

with modelo_moneda:
    trace = pm.sample(niter)

pm.traceplot(trace, varnames=["p"])
pass

pm.summary(trace)
