x=raw_input('Informe a quantidade de dias, horas, minutos e segundos (d h m s): ')
dias, horas, minutos, segundos = x.split(" ")

resp = int(segundos) + (int(minutos)*60) + (int(horas)*3600) + (int(dias)*86400)

print(resp)
