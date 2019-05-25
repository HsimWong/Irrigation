# -*- coding: utf-8 -*-

import numpy as np


def membership_shumilitylow(shumidity):
    if shumility < 40:
        grade = 1
    elif temp < 70:
        grade = (-1 / 30) * (temp - 40) + 1
    else:
        grade = 0
    return grade


def membership_shumidityhigh(shumidity):
    if shumility < 40:
        grade = 0
    elif temp < 70:
        grade = (1 / 30) * (temp - 40)
    else:
        grade = 1
    return grade


def membership_ahumiditylow(ahumidity):
    if ahumidity < 20:
        grade = 1
    elif ahumidity < 50:
        grade = (-1 / 30) * (ahumidity - 20) + 1
    else:
        grade = 0
    return grade


def membership_ahumiditycomfrot(ahumidity):

    if 30 < ahumidity < 50:
        grade = (1 / 20) * (ahumidity - 30)
    elif 50 < ahumidity < 70:
        grade = (-1 / 20) * (ahumidity - 50) + 1
    else:
        grade = 0
    return grade

def membership_ahumidityhigh(ahumidity):
    if ahumidity < 50:
        grade = 0
    elif ahumidity < 80:
        grade = (1 / 30) * (ahumidity - 50) 
    else:
        grade = 1
    return grade

def membership_light(light):
    if light < 800:
        grade = 0
    elif light < 1200:
        grade = (1 / 400) * (light - 800) 
    else:
        grade = 1
    return grade

def membership_precipIntensitylow(precipIntensity):
    if ahumidity < 2:
        grade = 1
    elif ahumidity < 3.5:
        grade = (-1 / 1.5) * (ahumidity - 2) + 1
    else:
        grade = 0
    return grade


def membership_precipIntensitynormal(precipIntensity):

    if 2.5 < precipIntensity < 5:
        grade = (1 / 2.5) * (precipIntensity - 2.5)
    elif 5< precipIntensity < 7.5:
        grade = (-1 / 2.5) * (precipIntensity - 5) + 1
    else:
        grade = 0
    return grade

def membership_precipIntensityhigh(precipIntensity):
    if precipIntensity < 6.5:
        grade = 0
    elif precipIntensity < 8:
        grade = (1 / 1.5) * (precipIntensity - 6.5) 
    else:
        grade = 1
    return grade

def membership_nowater(operating_range_water):
    if operating_range_water < 100:
        grade = (-1 / 100) * operating_range_water + 1
    else:
        grade = 0
    return grade

def membership_lesswater(operating_range_water):
    if operating_range_water < 100:
        grade = (1 / 100) * operating_range_temp
    elif operating_range_temp < 200:
        grade = (-1 / 100) * (operating_range_temp - 100) + 1
    else:
        grade = 0
    return grade


def membership_normalwater(operating_range_water):
    if operating_range_water < 100:
        grade = 0
    elif operating_range_water < 200:
        grade = (1 / 100) * (operating_range_temp - 100)
    elif operating_range_water < 300:
        grade = (-1 / 100) * (operating_range_temp -200)+ 1
    else:
        grade = 0
    return grade


def membership_morewater(operating_range_water):
    if operating_range_water < 200:
        grade = 0
    elif operating_range_temp < 300:
        grade = (1 / 100) * (operating_range_water - 200)
    else:
        grade = 0
    return grade


def AND(*args):
    return max(args)


def OR(*args):
    return min(args)


def Consequent(membership_func, horizontal_axis_list, Antecedent):

    R = []
    for i in horizontal_axis_list:
        grade = membership_func(i)
        if grade > Antecedent:
            R.append(Antecedent)
        else:
            R.append(grade)
    return R


if __name__ == '__main__':
    shumidity=float(input('soil humidity'))
    ahumidity=float(input('air humidity：'))
    light=float(input('light：'))
    precipIntensity=float(input('precipIntensity：'))

    shumilitylow_grade = membership_shumilitylow(shumidity)
    shumidityhigh_grade = membership_shumidityhigh(shumidity)
    ahumiditylow_grade = membership_ahumiditylow(ahumidity)
    ahumiditycomfrot_grade = membership_ahumiditycomfrot(ahumidity)
    ahumidityhigh_grade = membership_ahumidityhigh(ahumidity)
    light_grade = membership_light(light)
    precipIntensitylow_grade = membership_precipIntensitylow(precipIntensity)
    precipIntensitynormal_grade = membership_precipIntensitynormal(precipIntensity)
    shumidityhigh_grade = membership_precipIntensityhigh(precipIntensity)

    operating_range_water = np.linspace(0, 350, 2100)

    Antecedent = AND(shumidityhigh_grade, shumidityhigh_grade)  
    R1 = Consequent(membership_nowater, operating_range_water, Antecedent)

    Antecedent = OR(shumilitylow_grade, ahumidityhigh_grade)
    R2 = Consequent(membership_lesswater, operating_range_water, Antecedent)

    Antecedent = OR(shumilitylow_grade, precipIntensitynormal_grade)
    R3 = Consequent(membership_lesswater, operating_range_water, Antecedent)

    Antecedent = OR(shumilitylow_grade, ahumiditycomfrot_grade)
    R4 = Consequent(membership_normalwater, operating_range_water, Antecedent)

    Antecedent = OR(shumilitylow_grade, precipIntensitylow_grade)
    R5 = Consequent(membership_normalwater, operating_range_water, Antecedent)

    Antecedent = OR(shumilitylow_grade, light_grade)
    R6 = Consequent(membership_morewater, operating_range_water, Antecedent)

    Antecedent = OR(shumilitylow_grade, ahumiditylow_grade)
    R7 = Consequent(membership_morewater, operating_range_water, Antecedent)

    B = []
    for i in range(len(operating_range_water)):
        grade = AND(R1[i], R2[i], R3[i], R4[i], R5[i], R6[i], R7[i])
        B.append(grade)

    delta_t = 21 / len(operating_range_water)
    denominator = 0  
    for i in range(1, len(B)):
        denominator += delta_t * ((B[i] + B[i - 1]) / 2)
    numerator = 0 
    for i in range(1, len(B)):
        t = (operating_range_water[i] + operating_range_water[i - 1]) / 2
        numerator += delta_t * t * ((B[i] + B[i - 1]) / 2)

    center = numerator / denominator
    print("浇水量 : {:.2f} [degree Celsius]".format(center))
