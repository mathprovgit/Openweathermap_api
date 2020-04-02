# -*- coding: utf-8 -*-
"""
This script is a thermodynamical media model for Humid Air

the script intend to calculate the thermodinamical variable of humid air 

Validity range: 
    T  = ]0-100] °C
    Hr = [0-100] %
    V  > 0       m3/h

Elaborated By:
    mathieu Provost 

"""

from media_model_water import p_h2o_sat, rho_h2o_g, cp_h2o_g, h_h2o_g
from numpy import arctan, log10

# necessary constant for the calculation
p = 1.013 #atmos press in bar

M_O2 = 32       #Molar mass of O2 in g/mol
M_N2 = 28.02    #Molar mass of N2 in g/mol
M_Ar = 39.94    #Molar mass of Ar in g/mol
M_CO2 = 39.94   #Molar mass of CO2 in g/mol

x_dryair_O2 = 0.2316 # mass fraction of O2 in dryair
x_dryair_N2 = 0.7557 # mass fraction of N2 in dryair
x_dryair_Ar = 0.0123 # mass fraction of Ar in dryair
x_dryair_CO2 = 1 - x_dryair_O2 - x_dryair_N2 - x_dryair_Ar # mass fraction of CO2 in dryair

R = 8.314772 # universal gas constant

#definition of the necessary functions for Humid air
def p_h2o(T, Hr):
    """
    
   Partial pressure of h2o gas in Humid air in bar
    
    input variavbles: 
        - T temperature in K
        - Hr relative Humidity in %


    """
    return (Hr / 100) * p_h2o_sat(T) #bar
 

def Ha_air(T, Hr):
    """
    
   Absolute Humidity of Humid air in kg/kg
    
    input variavbles: 
        - T temperature in K
        - Hr relative Humidity in %

    """
    return (0.6222 * p_h2o(T, Hr) * 100 / ((p * 100) - (p_h2o(T, Hr) * 100)))

def Hr_air(T,Ha):
    """
    
    Relative Humidity of Humid air in kg/kg
    
    input variavbles: 
        - T temperature in K
        - Ha temperature in kg/kg

    """
    psat = p_h2o_sat(T) 
    hr = ((100 * p) * Ha) / ((Ha * psat) + (0.6222 * psat))
    return hr
    

def x_Humid_air_h2o(T, Hr): 
    """
    
    mass fraction of h2o gas in Humid air in kg/kg
    
    input variavbles: 
        - T temperature in K
        - Hr relative Humidity in %

    """
    return Ha_air(T, Hr) / (1 + Ha_air(T, Hr))
 
def x_Humid_air_O2(T, Hr):    
    """
    
    mass fraction of O2 gas in Humid air in kg/kg
    
    input variavbles: 
        - T temperature in K
        - Hr relative Humidity in %

    """
    return x_dryair_O2 / (1 + Ha_air(T, Hr))
 
def x_Humid_air_N2(T, Hr): 
    """
    
    mass fraction of N2 gas in Humid air in kg/kg
    
    input variavbles: 
        - T temperature in K
        - Hr relative Humidity in %

    """
    return x_dryair_N2 / (1 + Ha_air(T, Hr))
 
def x_Humid_air_Ar(T, Hr): 
    """
    
    mass fraction of Ar gas in Humid air in kg/kg
    
    input variavbles: 
        - T temperature in K
        - Hr relative Humidity in %

    """

    return x_dryair_Ar / (1 + Ha_air(T, Hr))
 
def x_Humid_air_CO2(T, Hr): 
    """
    
    mass fraction of CO2 gas in Humid air in kg/kg
    
    input variavbles: 
        - T temperature in K
        - Hr relative Humidity in %

    """
    return x_dryair_CO2 / (1 + Ha_air(T, Hr))
 
def rho_O2(T):
    """
    
    Volumic Mass of O2 gas in kg/m3
    
    input variavbles: 
        - T temperature in K
        
    """
    return (1.013 * 100 * M_O2) / (T * R)
 
def rho_N2(T): 
    """
    
    Volumic Mass of Nitrogen gas in kg/m3
    
    input variavbles: 
        - T temperature in K
        
    """

    return (1.013 * 100 * M_N2) / (T * R)
 
def rho_Ar(T): 

    """
    
    Volumic Mass of Argon gas in kg/m3
    
    input variavbles: 
        - T temperature in K
        
    """
    return (1.013 * 100 * M_Ar) / (T * R)
 
def rho_CO2(T):

    """
    
    Volumic Mass of CO2 in kg/m3
    
    input variavbles: 
        - T temperature in K
        
    """
    return (1.013 * 100 * M_CO2) / (T * R)
 
def rho_Humid_air(T, Hr): 
    """
    
    Volumic Mass of Humid Air in kg/m3
    
    input variavbles: 
        - T temperature in K
        - Hr relative Humidity in %

        
    """
    return 1 / ((x_Humid_air_h2o(T, Hr) / rho_h2o_g(T)) + (x_Humid_air_O2(T, Hr) / rho_O2(T)) + (x_Humid_air_N2(T, Hr) / rho_N2(T)) + (x_Humid_air_Ar(T, Hr) / rho_Ar(T)) + (x_Humid_air_CO2(T, Hr) / rho_CO2(T)))
 
def cp_O2(T):
    """
    
    specific of heat capacity of Oxygen gas in kJ/kg.K
    
    input variavbles: 
        - T temperature in K
        
    """
    return (885.4 + 0.071 * (T) + 0.000277 * (T) ** 2 - 0.000000143 * (T) ** 3 - 0.000000004 * (T) ** -2) / 1000
 
def cp_N2(T): 
    """
    
    specific of heat capacity of Nitrogen gas in kJ/kg.K
    
    input variavbles: 
        - T temperature in K
        
    """
    return (1049.9 - 0.158 * (T) + 0.000439 * ((T) ** 2) - 0.000000166 * ((T) ** 3) - 0.000000016 * ((T) ** -2)) / 1000
 
def cp_Ar(T):
    """
    
    specific of heat capacity of Argon gas in kJ/kg.K
    
    input variavbles: 
        - T temperature in K
        
    """
    return 520.3 / 1000
 
def cp_CO2(T): 
    """
    
    specific of heat capacity of CO2 gas in kJ/kg.K
    
    input variavbles: 
        - T temperature in K
        
    """
    return (617.3 + 0.95 * (T) - 0.000388 * (T) ** 2 + 0.00000005 * (T) ** 3 + 0.000000189 * (T) ** -2) / 1000
 
def cp_Humid_air(T, Hr):
    """
    
    specific of heat capacity of Humid air in kJ/kg.K
    
    input variavbles: 
        - T temperature in K
        - Hr relative Humidity in %
        
    """
    return x_Humid_air_h2o(T, Hr) * cp_h2o_g(T) + x_Humid_air_O2(T, Hr) * cp_O2(T) + x_Humid_air_N2(T, Hr) * cp_N2(T) + x_Humid_air_Ar(T, Hr) * cp_Ar(T) + x_Humid_air_CO2(T, Hr) * cp_CO2(T)
 
def cp_dry_air(T): 
    """
    
    specific of heat capacity of dry Air in kJ/kg.K
    
    input variavbles: 
        - T temperature in K
        
    """
    return 0.2316 * cp_O2(T) + 0.7557 * cp_N2(T) + 0.0123 * cp_Ar(T) + (1 - 0.2316 - 0.7557 - 0.0123) * cp_CO2(T)
 
def h_dry_air(T): 
    """
    
    enthalpy of dry Air in kJ/kg
    
    input variavbles: 
        - T temperature in K
        
    """
    return cp_dry_air(T) * T - cp_dry_air(273.15) * 273.15
 
def h_humid_air(T, Hr):
    """
    
    enthalpy of Humid Air in kJ/kg
    
    input variavbles: 
        - T temperature in K
        - Hr relative Humidity in %
        
    """
    return h_dry_air(T) * (x_Humid_air_O2(T, Hr) + x_Humid_air_N2(T, Hr) + x_Humid_air_Ar(T, Hr) + x_Humid_air_CO2(T, Hr)) + x_Humid_air_h2o(T, Hr) * h_h2o_g(T)
  

def T_dew(T,Hr):
    """
    
    Determines the dew point Temperature in K 
    
    input variavbles: 
        - T temperature in K
        - Hr relative Humidity in %
        
    """
    
    Td = -233.426+(1730.63/(8.07131-log10(p_h2o((T), Hr)*750.06375541921)))
    return Td+273.15 

def T_wet_bulb(T,Hr):
    """
    
    Determines the wet-buld Temperature in K 
    
    input variavbles: 
        - T temperature in K
        - Hr relative Humidity in %
        
    """
    Twb = (T-273.15) * arctan(0.151977 * (Hr+8.313659) ** (1/2))+arctan((T-273.15)+Hr)-arctan(Hr-1.676331)+0.00391838 * (Hr) ** (3/2) * arctan(0.023101 * Hr)-4.686035
    return Twb+273.15 
   
