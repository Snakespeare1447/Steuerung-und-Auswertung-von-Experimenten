#Konvention: In Richtung der Erde (nach unten) ist die negative Richtung.
import math
import matplotlib.pyplot as plt

V = 0.000001                  #Volumen in m³
v01 = 15000
v02 = 25000
v03 = 35000  
m = 7.874*(10**(-3))          #Masse in kg 
h0 = 150000                   #Eintrittshöhe
M = 0.02896                   #mittlere molare Masse der Luft in kg/mol
R = 8.314                     #Gaskonstante
rho0 = 1.292                  #Normluftdichte am Erdboden in kg/m³
T = 298.15                    #Temperatur entspricht 25°C
cw =   0.45                   #Luftwiderstandsbeiwert (hier einer relativ glatten Kugel)
delta_t = 0.01                #Zeitinkrement
t0 = 0                        #Startzeit
G = 6.67408*(10**(-11))       #Gravitationskonstante
Erdradius = 6378137 
Erdmasse = 5.9722*(10**24)
A = math.pi*(0.75*V/math.pi)**(2/3)     #Querschnittsfläche
g = 9.81                                #Erdbeschleunigung auf Meereshöhe (hier nur für barom. höhenformel verwendet)

def Luftdichte(rho0, M, g, h, R, T):
    rho = rho0*math.exp((-M*g*h)/(R*T))
    return rho

def Reibungskraft(cw, A, rho, v):
    Fr = 0.5*cw*A*rho*(v**2)
    return Fr

def Beschleunigung(m, Erdmasse, Fr, G, h):
    aneu =  ((G*m*Erdmasse)/((Erdradius+h)**2)-Fr)/m
    return aneu

def Geschwindigkeit(a, delta_t, v):
    vneu = a*delta_t + v
    return vneu

def Höhe(v,delta_t, h):
    hneu = h-v*delta_t
    return hneu

#durchführung der berechnungen:
#initialisierung der startwerte:
t = t0 
h = h0
v = v01
rho = Luftdichte(rho0, M, g, h, R, T)
Fr = Reibungskraft(cw, A, rho, v)
a = Beschleunigung(m, Erdmasse, Fr, G, h)

a_list = [a]
v_list = [v]
h_list = [h]
t_list = [t]

while h>=0:
    t = t+delta_t
    rho = Luftdichte(rho0, M, g, h, R, T)
    Fr = Reibungskraft(cw, A, rho, v)    
    h = Höhe(v,delta_t, h)
    v = Geschwindigkeit(a, delta_t, v)
    a = Beschleunigung(m, Erdmasse, Fr, G, h)
    a_list.append(a)
    v_list.append(v)
    h_list.append(h)
    t_list.append(t)
    
#graphische Ausgabe:

fig = plt.figure(1, figsize = (11,8))

ax1 = fig.add_subplot(221)
x = t_list
y = h_list
ax1.plot(x, y, color='royalblue', marker='.', linestyle='none')
ax1.set_xlabel('Zeit [s]')
ax1.set_ylabel('Höhe [m]')
plt.grid()

ax2 = fig.add_subplot(222)
x = v_list
y = h_list
ax2.plot(x, y, color='cyan', marker='.', linestyle='none')
ax2.set_xlabel('Geschwindigkeit [m/s]')
ax2.set_ylabel('Höhe [m]')
plt.grid()

ax3 = fig.add_subplot(223)
x = h_list
y = a_list
ax3.plot(x, y, color='darkmagenta', marker='.', linestyle='none')
ax3.set_xlabel('Höhe [m]')
ax3.set_ylabel('Beschleunigung [m/s²]')
plt.grid()

ax4 = fig.add_subplot(224)
x = t_list
y = v_list
ax4.plot(x, y, color='magenta', marker='.', linestyle='none')
ax4.set_xlabel('Zeit [s]')
ax4.set_ylabel('Geschwindigkeit [m/s]')
plt.grid()

fig.tight_layout()
fig.show()

print('Zeit bis zum Auftreffen: ',t, 's')
print('Geschwindigkeit beim Auftreffen: ', v, 'm/s')