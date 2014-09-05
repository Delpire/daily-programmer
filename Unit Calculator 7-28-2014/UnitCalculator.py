#!/usr/bin/env python3

import re;
import sys;

#Ratios for unit conversion.
ratios = [[1, 39.3701, 0.000621371, 32.4077929, 0, 0, 0, 0],
            [0.0254, 1, 0.0000157828, 0.82315794, 0, 0, 0, 0],
            [1609.34, 63360, 1, 52155.287, 0, 0, 0, 0],
            [0.0308567758, 1.21483369, 0.0000191735116, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0.0625, 0.0283495, 0.00006432688],
            [0, 0, 0, 0, 16, 1, 0.453592, 0.00102923],
            [0, 0, 0, 0, 35.274, 2.20462, 1, 0.0022691173],
            [0, 0, 0, 0, 15545.6, 971.6, 440.7, 1]];
 
#Abbreviated, singular, and plural unit names.
units = [ "m" , "in",  "mi",  "apc", "oz", "lb", "kg" ,"hhdBe" ];
fullUnits = [ "meter" , "inch",  "mile",  "attoparsec", "ounce", "pound", "kilogram" ,"hogshead" ];
fullUnitsPlural = [ "meters" , "inches",  "miles",  "attoparsecs", "ounces", "pounds", "kilograms" ,"hogsheads" ];

#Grab and format the user input.
input = input("Convert: ");
input = re.match(r"([0-9]+|[0-9]+[.0-9]+)([ ]?)([a-z]+)([ ]+)([a-z]+)([ ]+)([a-z]+)", input, re.I);

#Grab the amount to convert, unit to convert, and unit to convert to.
fromAmount = input.groups()[0];
fromUnit = input.groups()[2];
toUnit = input.groups()[6];

#Check to see if the user entered a abbreviated, singular or plural unit.
if fromUnit not in units:
    if fromUnit not in fullUnits:
        if fromUnit not in fullUnitsPlural:
            print(str(fromUnit) + " is not a valid unit");
            sys.exit();
        else:
            fromUnitIndex = fullUnitsPlural.index(fromUnit);
    else:
        fromUnitIndex = fullUnits.index(fromUnit);
else:
    fromUnitIndex = units.index(fromUnit);

#Check to see if the user entered a abbreviated, singular or plural unit.
if toUnit not in units:
    if toUnit not in fullUnits:
        if toUnit not in fullUnitsPlural:
            print(str(toUnit) + " is not a valid unit");
            sys.exit();
        else:
            toUnitIndex = fullUnitsPlural.index(toUnit);
    else:
        toUnitIndex = fullUnits.index(toUnit);
else:
    toUnitIndex = units.index(toUnit);

#Exit if unit cannot be converted.
if ratios[fromUnitIndex][toUnitIndex] == 0:
	print("Cannot convert " + fromUnit + " to " + toUnit + ".");
	sys.exit();
	
#Convert the unit.
toAmount = float(fromAmount[0]) * ratios[fromUnitIndex][toUnitIndex];

#Print the conversion.
print(str(fromAmount) + " " + str(fromUnit) + " is " + str(toAmount) + " " + str(toUnit));