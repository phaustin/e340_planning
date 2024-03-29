---
jupytext:
  cell_metadata_filter: all
  encoding: '# -*- coding: utf-8 -*-'
  formats: ipynb,py:percent,md:myst
  notebook_metadata_filter: all,-language_info,-toc,-latex_envs
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.9.1
kernelspec:
  display_name: Python 3
  language: python
  name: python3
latex_metadata:
  chead: E340 Day 5
  lhead: Quiz solutions
---

+++ {"ctype": "question", "qnum": "1"}

1.  Suppose we have a one layer atmosphere with ε=1 above a black
    surface as in Dessler Fig. 4.6 or the one layer model on page 3 of the Day 5 reading. 
    Does adding a second opaque (ε=1)
    layer (Dessler Figure 4.7 or the two layer model on page 4) increase the greenhouse effect, decrease
    the greenhouse effect, or leave the greenhouse effect unchanged?
    
    A.  increase
    
    B.  decrease
    
    C.  no change

+++

Q1 answer -- A) increase -- if a layer is added, then in equilibrium the surface temperature has to go up because you are now out of balance (the shortwave downward flux hasn't changed).  Equilibrium will only be restored when the new black layer comes into balance with the downwelling shortwave.  

+++ {"ctype": "question", "qnum": "2"}

2.  Suppose a planet's average surface temperature is about $T_g$ = 350 K. In the one-layer
    semi-transparent atmosphere shown below (and seen in your reading),
    what would the approximate long-wave atmospheric emissivity ε need to be 
    to maintain value of $T_g$, if the average shorwave flux was $I_0=500\ W\,m^{-2}$. (Hint, look at equations 5-6 in the reading).
    
    A.  0.54
    
    B.  0.61
    
    C.  0.77
    
    D.  0.82
    
    E.  0.93

+++ {"ctype": "question", "qnum": "2"}

![fig1](media_day5_resize/image1.png)

+++

Answer -- D) 0.82-- using the onelayer equations from the Day 5 reading and solve for epsilon:

```{code-cell} ipython3
:ctype: answer
:qnum: '2'

sigma=5.67e-8
I0=500
TG=350
eps_2=(-2*I0/(sigma*TG**4.))
eps = eps_2 + 2
print(f"epsilon is {eps:5.2f}")
```

+++ {"ctype": "question", "qnum": "3"}

3. Given a one-layer atmosphere like problem 2, but with $\epsilon=0.8$, $T_G$=300 K, $T_1$=265 K, $I_0$ = 300 $W\,m^{-2}$,  calculate the greenouse effect. (choose the closest number)
 
A. -130 $W\,m^2$

B. +10  $W\,m^2$

C. +110 $W\,m^2$

D. +140 $W\,m^2$

E. +180 $W\,m^2$

+++

Answer: D) 

```{code-cell} ipython3
:ctype: answer
:qnum: '3'

epsilon=0.8
I0=300.
TG=300
T1=265
G=sigma*TG**4.
I1=epsilon*sigma*T1**4.
print(f"G={G:5.2f} W/m^2")
leaving = I1 + (1 - epsilon)*G
print(f"flux leaving earth is {leaving:5.2f} W/m^2")
print(f"greenhouse effect is {G - leaving:5.2f} W/m^")
```

+++ {"ctype": "question", "qnum": "4"}

4.  According to the figure in Trenberth et al. 2009 below, how big is the Earth's greenhouse effect?
 
A.  85 $W\,m^{-2}$

B. 157 $W\,m^{-2}$

C. 254 $W\,m^{-2}$

D. 285 $W\,m^{-2}$

E. 333 $W\,m^{-2}$

+++ {"ctype": "question", "qnum": "3"}

![fig2](media_day5_resize/image2.png)

+++ {"ctype": "answer", "qnum": "4"}

Answer: B) -239 - (-396) = 157 W/m^2

```{code-cell} ipython3

```
