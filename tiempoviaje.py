duracion_primer_tramo = float(input("Ingrese la duración del primer tramo del vuelo en horas: "))
duracion_primera_escalas = float(input("Ingrese la duración de la primera escala en horas: "))
duracion_segundo_tramo = float(input("Ingrese la duración del segundo tramo del vuelo en horas: "))
duracion_segunda_escalas = float(input("Ingrese la duración de la segunda escala en horas: "))
duracion_tercer_tramo = float(input("Ingrese la duración del tercer tramo del vuelo en horas: "))

tiempo_total = duracion_primer_tramo + duracion_primera_escalas
tiempo_total += duracion_segundo_tramo 
tiempo_total += duracion_segunda_escalas 
tiempo_total += duracion_tercer_tramo 

print(f"El tiempo total es de: {tiempo_total} horas")