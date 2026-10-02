"""Recompute the delivered O3− grid; sources and assumptions are in the entry longDesc."""
from pathlib import Path
import math
import json
import numpy as np

R = 8.31446261815324
NA = 6.02214076e23
KB = 1.380649e-23
HPLANCK = 6.62607015e-34
C = 299792458.0
MASS = .04799875 / NA
OMEGA = np.array([975., 550., 880.])
THETA = HPLANCK * C * 100 * OMEGA / KB
# Arnold et al., p. 917 text and p. 921 conclusion: 1.36 A, 111.8 deg.
ANGLE = math.radians(111.8)
LENGTH = 1.36e-10
COORDS = np.array([[0.,0.,0.],
                   [LENGTH*math.sin(ANGLE/2),LENGTH*math.cos(ANGLE/2),0.],
                   [-LENGTH*math.sin(ANGLE/2),LENGTH*math.cos(ANGLE/2),0.]])
COORDS -= COORDS.mean(axis=0)
INERTIA = sum(MASS/3 * (np.dot(v,v)*np.eye(3)-np.outer(v,v)) for v in COORDS)
MOMENTS = np.linalg.eigvalsh(INERTIA)
ROT_THETA = HPLANCK**2 / (8*math.pi**2*KB*MOMENTS)
O2_H298_0 = 8.683  # JANAF O-029, zero-temperature H-H(Tr) column.
HF0 = -58.47       # ATcT v1.156 Ozonide selected formation enthalpy, 0 K row.

def rrho(t):
    x = THETA/t
    qtrans = (2*math.pi*MASS*KB*t/HPLANCK**2)**1.5 * KB*t/1e5
    qrot = math.sqrt(math.pi) / 2 * t**1.5 / math.sqrt(np.prod(ROT_THETA))
    s = R*(math.log(qtrans)+2.5 + math.log(qrot)+1.5 + math.log(2))
    s += R * float(np.sum(x/np.expm1(x) - np.log1p(-np.exp(-x))))
    hinc = 4*R*t + R*float(np.sum(THETA/np.expm1(x)))
    cp = 4*R + R*float(np.sum(x*x*np.exp(-x)/(1-np.exp(-x))**2))
    return hinc/1000, s, cp

temperatures = [298.15,300.] + list(map(float,range(350,1001,50)))
hinc,sref,cpref = rrho(298.15)
h_ref = HF0+hinc-1.5*O2_H298_0
cps = [rrho(t)[2] for t in temperatures]
slope=(cps[1]-cps[0])/(temperatures[1]-temperatures[0]); intercept=cps[0]-slope*298.15
dh=(slope*(298.15**2-298**2)/2+intercept*.15)/1000
ds=slope*.15+intercept*math.log(298.15/298)

print(json.dumps(dict(Tdata=[298.]+temperatures,
    Cpdata=[cps[0]-.15*slope]+cps, H298=h_ref-dh, S298=sref-ds,
    Cp0=4*R, CpInf=7*R, E0=HF0,
    rows={str(t):dict(h=HF0+rrho(t)[0]-1.5*O2_H298_0,s=rrho(t)[1],cp=rrho(t)[2])
          for t in temperatures}),indent=2))
