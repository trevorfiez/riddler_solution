from pulp import *


x11 = LpVariable("x11", 0, 1, LpBinary)
x12 = LpVariable("x12", 0, 1, LpBinary)
x2 = LpVariable("x2", 0, 8, LpInteger)
x3 = LpVariable("x3", 0, 4, LpInteger)

prob = LpProblem("riddler_problem", LpMaximize)
prob += x11 * 200 + x12 * 300 + x2 * 50 + x3 * 25
prob += x11 * 400 + x12 * 800 + x2 * 150 + x3 * 50 <= 1000
prob += x11 + x12 <= 1

status = prob.solve(GLPK(msg=0))
print(LpStatus[status])

print(value(x11))
print(value(x12))
print(value(x2))
print(value(x3))
