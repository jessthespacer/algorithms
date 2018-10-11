# Iterative numerical integrator

from math import sin, cos

f = lambda x: sin(x)
F = lambda x: -cos(x)

x = 0
a = 0
b = 4
integralAnalytical = F(b) - F(a)

for dx in [1.6, 0.8, 0.4, 0.2, 0.1, 0.05, 0.025, 0.0125, 0.00625, 0.003125, 0.0015625]:
	integralNumerical = 0
	for i in range(int((b - a)/dx) + 1):
		x = i * dx
		integralNumerical += dx * f(x)
	error = integralNumerical / integralAnalytical - 1
	print("RIEMANN SUM")
	print("dx = {}".format(dx))
	print("Numerical solution: {}".format(integralNumerical))
	print("Analytical solution: {}".format(integralAnalytical))
	print("Error: {}".format(error))
	print()

# Now let's switch up the scheme to a trapezoidal approximation:
for dx in [1.6, 0.8, 0.4, 0.2, 0.1, 0.05, 0.025, 0.0125, 0.00625, 0.003125, 0.0015625]:
	integralNumerical = 0
	for i in range(int((b - a)/dx) + 1):
		x = i * dx
		integralNumerical += dx * (f(x - dx) + f(x)) / 2
	error = integralNumerical / integralAnalytical - 1
	print("TRAPEZOIDAL APPROXIMATION")
	print("dx = {}".format(dx))
	print("Numerical solution: {}".format(integralNumerical))
	print("Analytical solution: {}".format(integralAnalytical))
	print("Error: {}".format(error))
	print()