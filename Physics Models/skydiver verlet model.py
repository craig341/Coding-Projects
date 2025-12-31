import math
import matplotlib.pyplot as plt

p0 = 1.225  # initial air density

H = 104000  # max height
h0 = 10000  # initial height
# hF = 2000  # final height
hF = 0
h = h0

m = 100  # skydiver mass

deployment_t = 10  # parachute deployment time
deployment_t_counter = deployment_t
skydiver_A = 2  # skydiver cross-sectional area
total_A = 160  # skydiver + parachute cross-sectional area
A = skydiver_A

cD = 0.4  # drag coefficient

g = 9.81

t = 0
dt = 0.1

x = 0
v = 0

x_vals = []
v_vals = []
a_vals = []
t_vals = []

deployed = False
while h > hF:
    p = p0 * math.e ** (-h / H)
    alpha = g - 0.5 * cD * p * A * v ** 2 / m
    V = v + alpha * dt

    if h <= 2000:
        deployed = True

        if deployment_t_counter > 1e-9:
            A += (total_A - skydiver_A) / (deployment_t / dt)
            deployment_t_counter -= dt

    x = x + v * dt + 0.5 * dt ** 2
    h = h0 - x
    p = p0 * math.e ** (-h / H)
    beta = g - 0.5 * cD * p * A * V ** 2 / m

    v = v + 0.5 * (alpha + beta) * dt

    x_vals.append(round(x, 3))
    v_vals.append(round(v, 3))
    a_vals.append(round(beta, 3))
    t_vals.append(t)

    t = t + dt

# print(v_vals[-1])

plt.figure()
plt.plot(t_vals, x_vals)
plt.title("Displacement vs Time")
plt.xlabel("t (s)")
plt.ylabel("x (m)")

plt.figure()
plt.plot(t_vals, v_vals)
plt.title("Velocity vs Time")
plt.xlabel("t (s)")
plt.ylabel("v (m/s)")

plt.figure()
plt.plot(t_vals, a_vals)
plt.title("Acceleration vs Time")
plt.xlabel("t (s)")
plt.ylabel("a (m/s²)")

plt.show()
