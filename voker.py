import keyboard
import time

settings = open('settings.txt','r')
cold_snap = ''
ghost_walk = ''
tornado = ''
EMP = ''
alacrity = '' 
chaos_meteor = '' 
sun_strike = ''
forge_spirit = ''
ice_wall = ''
deafening_blast = ''
cast_delay = 0.1

for line in settings:
	splited = line.split(' ')
	if splited[0] == 'cold_snap':
		cold_snap = str(splited[2])

	if splited[0] == 'ghost_walk':
		ghost_walk = str(splited[2])

	if splited[0] == 'cold_snap':
		cold_snap = str(splited[2])

	if splited[0] == 'tornado':
		tornado = str(splited[2])

	if splited[0] == 'EMP':
		EMP = str(splited[2])

	if splited[0] == 'alacrity':
		alacrity = str(splited[2])

	if splited[0] == 'chaos_meteor':
		chaos_meteor = str(splited[2])

	if splited[0] == 'sun_strike':
		sun_strike = str(splited[2])

	if splited[0] == 'forge_spirit':
		forge_spirit = str(splited[2])

	if splited[0] == 'ice_wall':
		ice_wall = str(splited[2])

	if splited[0] == 'deafening_blast':
		deafening_blast = str(splited[2])

	if splited[0] == 'delay':
		cast_delay = float(splited[2])

print(F"БИНДЫ ИНИЦИАЛИЗИРОВАНЫ:\n[cold_snap] - {cold_snap}\n[ghost_walk] - {ghost_walk}\n[tornado] - {tornado}\n[e.m.p] - {EMP}\n[alacrity] - {alacrity}\n[chaos_meteor] - {chaos_meteor}\n[sun_strike] - {sun_strike}\n[forge_spirit] - {forge_spirit}\n[ice_wall] - {ice_wall}\n[deafening_blast] - {deafening_blast}\n[ЗАДЕРЖКА нажатия СФЕР] - {cast_delay}")
print("\n\n\n-----------------------------------------------STARTED-----------------------------------------------")


while True:

	if keyboard.is_pressed(cold_snap): #cold snap
		keyboard.send('q')
		time.sleep(cast_delay)
		keyboard.send('q')
		time.sleep(cast_delay)
		keyboard.send('q')
		time.sleep(cast_delay)
		keyboard.send('r')
	if keyboard.is_pressed(ghost_walk):#ghost walk
		keyboard.send('q')
		time.sleep(cast_delay)
		keyboard.send('q')
		time.sleep(cast_delay)
		keyboard.send('w')
		time.sleep(cast_delay)
		keyboard.send('r')
	if keyboard.is_pressed(ice_wall): #ice wall
		keyboard.send('q')
		time.sleep(cast_delay)
		keyboard.send('q')
		time.sleep(cast_delay)
		keyboard.send('e')
		time.sleep(cast_delay)
		keyboard.send('r')
	if keyboard.is_pressed(EMP): #emp
		keyboard.send('w')
		time.sleep(cast_delay)
		keyboard.send('w')
		time.sleep(cast_delay)
		keyboard.send('w')
		time.sleep(cast_delay)
		keyboard.send('r')
	if keyboard.is_pressed(tornado): #tornado
		keyboard.send('w')
		time.sleep(cast_delay)
		keyboard.send('w')
		time.sleep(cast_delay)
		keyboard.send('q')
		time.sleep(cast_delay)
		keyboard.send('r')
		time.sleep(cast_delay)
	if keyboard.is_pressed(alacrity): #alacrity
		keyboard.send('w')
		time.sleep(cast_delay)
		keyboard.send('w')
		time.sleep(cast_delay)
		keyboard.send('e')
		time.sleep(cast_delay)
		keyboard.send('r')
	if keyboard.is_pressed(deafening_blast): #blast
		keyboard.send('q')
		time.sleep(cast_delay)
		keyboard.send('w')
		time.sleep(cast_delay)
		keyboard.send('e')
		time.sleep(cast_delay)
		keyboard.send('r')
	if keyboard.is_pressed(sun_strike): #sun strike
		keyboard.send('e')
		time.sleep(cast_delay)
		keyboard.send('e')
		time.sleep(cast_delay)
		keyboard.send('e')
		time.sleep(cast_delay)
		keyboard.send('r')
	if keyboard.is_pressed(forge_spirit): #forge
		keyboard.send('e')
		time.sleep(cast_delay)
		keyboard.send('e')
		time.sleep(cast_delay)
		keyboard.send('q')
		time.sleep(cast_delay)
		keyboard.send('r')
	if keyboard.is_pressed(chaos_meteor): #meteor
		keyboard.send('e')
		time.sleep(cast_delay)
		keyboard.send('e')
		time.sleep(cast_delay)
		keyboard.send('w')
		time.sleep(cast_delay)
		keyboard.send('r')
