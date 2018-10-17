from time import sleep

while True:
    line = open("/proc/stat", "r").readline()
    line = line.split()   #aufteilen des strings in eine liste
    line.pop(0)           #erstes element "cpu" löschen
    line =  [int(i) for i in line]    #in int konvertieren
    totaltime = sum(line)
    idletime = line[3]
    workingtime = totaltime - idletime
    cpupercent = (workingtime/totaltime)*100
    print("CPU-Auslastung: % 2f" %cpupercent, "%")
    sleep(2)     #2 sekunden warten
