# -*- coding: utf-8 -*-
"""Black Scholes Option Tool

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iD01Y30WTLDroFZVsVbMmoTcS4hiMZg3
"""

from math import sqrt , exp, log, erf

from decimal import *
getcontext().prec = 5

undprice = float(input("Current Stock Price?: "))   # Stock price at current time
strike = float(input("Strike Price?: "))            # Expected Price By Expiration day
time = float(input("Days to Expiration?: "))        # time until expiration in days
rate = float(input("Current Interest Rate?: "))     # Annualized risk free rate
sigma = float(input("Sigma?: "))                    # Standard Deviation of stock's returns
divrate = float(input("Dividend Rate?: "))          # Dividend yield on stock

#statistics
sigTsquared = sqrt(Decimal(time)/365)*sigma
edivT = exp((-divrate*time)/365)
ert = exp((-rate*time)/365)
d1 = (log(undprice*edivT/strike)+(rate+.5*(sigma**2))*time/365)/sigTsquared
d2 = d1-sigTsquared
Nd1 = (1+erf(d1/sqrt(2)))/2
Nd2 = (1+erf(d2/sqrt(2)))/2
iNd1 = (1+erf(-d1/sqrt(2)))/2
iNd2 = (1+erf(-d2/sqrt(2)))/2

#Outputs
callPrice = round(undprice*edivT*Nd1-strike*ert*Nd2, 2)
putPrice = round(strike*ert*iNd2-undprice*edivT*iNd1, 2)

#Operations
print("")
print("Call Price = " + str(callPrice) )
print("Put Price = " + str(putPrice) )