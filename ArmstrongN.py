def proceso(num, suma=0):
  numero = []
  for i in str(num):
    exp = int(i) ** len(str(num))
    numero.append(exp)
    if len(numero) == len(str(num)):
        total = sum(numero)
        return num, total
        numero.clear()


entrada = input()
datos = []

for i in range(int(entrada)):
  entrada2 = input()
  datos.append(entrada2)

for n in datos:
  resul1, resul2 = proceso(int(n))

  if resul1 == resul2:
    print("Armstrong")
  elif resul1 != resul2:
    print("Not Armstrong")



