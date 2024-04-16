import datetime
import math

s = 45 #swim time [min]
b_h = 3 #bike time [h]
b_min = 30 #bike time [min]
r_h = 1 #run time [h]
r_min = 50 #run time [min]

w_min = 11 #total change time (Zone 1 + Zone 2) [min]

total = datetime.timedelta(minutes=s) + datetime.timedelta(hours=b_h, minutes=b_min) + datetime.timedelta(hours=r_h, minutes=r_min) + datetime.timedelta(minutes=w_min)

print('Gesamtzeit:' ,total)

# Pace Calculation
# Distances
swim = 1900 #[m]
bike = 90 #[km]
run = 21 #[km]

#Calculation of swim pace
s_pace = s/(swim/100)*60 #[sec]
s_pace_min = math.floor(s_pace/60)
s_pace_sec = math.floor(s_pace % 60)
print('s_pace: ',s_pace_min,':',s_pace_sec,' min/100m')

#Calculation of bike pace
b_total_time = b_h*60+b_min #[min]
b_total_time = b_total_time/60 #[h]
b_pace = round(bike/b_total_time,2)
print('b_pace:',b_pace,' km/h')

#Calculation of run pace
r_total_time = r_h*60+r_min #[min]
r_pace = round(r_total_time/run,2)
print('r_pace:',r_pace,' min/km')