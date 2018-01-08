#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 10:35:39 2018

@author: coreyclip

formats and prints intercept,coefficient, and diagnostic
outputs from sklearn linear regression models

input:
    fitted sklearn model, 
    inputs JSON:
        {
         Y: string
         X: list or string
         }

output:
    prints diagonostic report
    

"""

print("loading report...")

def report(model, inputs):
    y = inputs['Y']
    x = inputs['X']
    coef_json = [{var + ':' + coef} for var, coef in zip(x,model.coef_)]
    print("variables and their coefficients in model")
    print("-" *50)
    print(coef_json)
    print("-" *50)
    print("The intercept for the model is {i}".format(i=model.intercept_))
    for var in coef_json:
        print("for each unit increase in {x}:".format(x=var))
        print("there is a {f} increase in {y}".format(f=coef_json[var],y=y))



