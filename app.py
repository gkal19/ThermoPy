#!/usr/bin/python

# Variáveis
#---------------

CELSIUS = float(input("Escolha um valor em graus Celsius: "))
FAHRENHEIT = float(input("Escolha um valor em graus Fahrenheit: "))
KELVIN = float(input("Escolha um valor em Kelvin: "))

FTOC = FAHRENHEIT - 32  # Fahrenheit para Celsius
FTOK = (FAHRENHEIT - 32) / 1.8  # Fahrenheit para Kelvin

KTOF = KELVIN * 1.8  # Kelvin para Fahrenheit

# Unidades
#---------------

    # Celsius
    #---------------
print("Convertendo seu valor de Celsius para Fahrenheit, o resultado é:\n",
      CELSIUS * 1.8 + 32)
print("Convertendo seu valor de Celsius para Kelvin, o resultado é:\n", CELSIUS + 273.15)

    # Fahrenheit
    #---------------
print("Convertendo seu valor de Fahrenheit para Celsius, o resultado é:")
print(FTOC / 1.8)
print("Convertendo seu valor de Fahrenheit para Kelvin, o resultado é:")
print(FTOK + 273)

    # Kelvin
    #---------------
print("Convertendo seu valor de Kelvin para Celsius, o resultado é:\n", KELVIN - 273.15)
print("Convertendo seu valor de Kelvin para Fahrenheit, o resultado é:", )
print(KTOF - 459.67)
