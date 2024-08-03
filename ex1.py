from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value

model = LpProblem("Maximize_Production", LpMaximize)

limonad = LpVariable("Limonad", lowBound=0, cat='Continuous')
fruktovyj_sik = LpVariable("Fruktovyj_sik", lowBound=0, cat='Continuous')

model += limonad + fruktovyj_sik

model += 2 * limonad + 1 * fruktovyj_sik <= 100, "Water"
model += 1 * limonad <= 50, "Sugar"
model += 1 * limonad <= 30, "Lemon_Juice"
model += 2 * fruktovyj_sik <= 40, "Fruit_Puree"

model.solve()

print(f"Кількість виробленого Лимонаду: {limonad.varValue}")
print(f"Кількість виробленого Фруктового соку: {fruktovyj_sik.varValue}")
print(f"Максимальна кількість вироблених продуктів: {value(model.objective)}")
