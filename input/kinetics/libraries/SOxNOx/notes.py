
"""
S + NO = SO + N ; S + NO = SN + O. much uncertainty '96 shock tube: http://www.sciencedirect.com/science/article/pii/S0082078496802633
S + NO2 = SO + NO
SH + NO2 <=> HSO + NO
SH + N2O <=> HSO + N2
SO + N <=> S + NO
SO + NO2 <=> SO2 + NO
SO2 + NO2 <=> NO + SO3
SO2 + N <=> SO + NO
HSO + NO2 <=> HOSO + NO
SO3 + N <=> SO2 + NO
SO2+SO2=SO3+SO take from [Marshall2007a]:37 if RMG can't generate it
Gimenez-Lopez, M. Martinez, A. Millera, R. Bilbao, M.U. Alzueta, Comb. Flame 2011, 158(1), 48-56, doi: 10.1016/j.combustflame.2010.07.017
report on:
SO+O2=SO2+O2
SO+OH=HOSO
but the source [24] isn't clear
also HOSO + H, HOSO2 + O2
SO3 + H2O <=> H2SO4 dimer?
add eq:
H2O = H2Odimer
H2Odimer
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 O u0 p2 c0 {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
Frequencies:
http://pubs.acs.org/doi/abs/10.1021/jp054722u
http://pubs.acs.org/doi/abs/10.1021/jp067499p
http://pubs.acs.org/doi/abs/10.1021/j100185a016
Out of scope:
HNC: http://pubs.acs.org/doi/abs/10.1021/acs.energyfuels.6b02085
H + H2S = H2 + SH   http://pubs.acs.org/doi/abs/10.1021/jp984242l
Train RMG with Table 5 for CH3SH + H: http://pubs.acs.org/doi/abs/10.1021/jp512966a
Chemical Kinetic Data Base for Propellant Combustion I. Reactions Involving NO, NO2, HNO, HNO2, HCN and N2O
http://aip.scitation.org/doi/abs/10.1063/1.555890
Chemical Kinetic Data Base for Propellant Combustion. II. Reactions Involving CN, NCO, and HNCO
http://aip.scitation.org/doi/abs/10.1063/1.555914
"""