"""----------programa para -------------------
-----------convertir temperatura--------------
----------------------------------------------"""

print("-------------------------------------")
print("-----Conversor de temperatura--------")
print("-------------------------------------")

#input
C=int(input("Digite la cantidad de grados Celcius: "))

#procedure
K = C+273.15
F = 1.8*C+32

#output
print("Conversiones:\n")
print(str(C) + "Grados celcius es igual a \n" + str(K) + " Grados kelvin \n"+ str(F) +" Grados fahrenheit")

