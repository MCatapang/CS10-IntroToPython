# A ball is throw at a 45deg angle from a height of
# 5 ft with an initial velocity of 75 ft/s. The
# height of the ball at time t can be approximated
# by the equation y = -16t^2 + 53t + 5. Find the
# height of the ball at t = 2 seconds.

# Created to take user input

t = int(input("How many seconds has passed after you threw the ball?: "))
height = ((-1)*16*pow(t, 2)) + (53*t) + 5

print(f"The height of the ball after {t} seconds is {height} ft.")