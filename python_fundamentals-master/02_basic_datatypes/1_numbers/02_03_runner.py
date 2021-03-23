'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''
# looking fo value in km/hr
# 30 minutes = 0.5 hours
# 30 seconds = 0.5 minutes
# 30.5 minutes total

miles_to_km = 10 * 1.6 # 16km
minutes_to_hours = 30.5 / 60
avg_speed = miles_to_km / minutes_to_hours
print(f"The average speed of our runner is: {avg_speed:.2f} km/hr")

