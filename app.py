#!/usr/bin/python

# Unidades
#---------------
Celsius = float(input("Escolha um valor em graus Celsius: "))
Fahrenheit = float(input("Escolha um valor em graus Fahrenheit: "))
Kelvin = float(input("Escolha um valor em Kelvin: "))

# Variáveis
#---------------
FtoC = Fahrenheit - 32  # Fahrenheit para Celsius
FtoK = (Fahrenheit - 32) / 1.8  # Fahrenheit para Kelvin

KtoF = Kelvin * 1.8  # Kelvin para Fahrenheit

# Celsius
#---------------
print("Convertendo seu valor de Celsius para Fahrenheit, o resultado é:\n",
      Celsius * 1.8 + 32)

print("Convertendo seu valor de Celsius para Kelvin, o resultado é:\n", Celsius + 273.15)

# Fahrenheit
#---------------
print("Convertendo seu valor de Fahrenheit para Celsius, o resultado é:")
print(FtoC / 1.8)

print("Convertendo seu valor de Fahrenheit para Kelvin, o resultado é:")
print(FtoK + 273)

# Kelvin
#---------------
print("Convertendo seu valor de Kelvin para Celsius, o resultado é:\n", Kelvin - 273.15)

print("Convertendo seu valor de Kelvin para Fahrenheit, o resultado é:", )
print(KtoF - 459.67)
