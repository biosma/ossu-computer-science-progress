# We will have a fixed initial amount and the ability to choose a value for the rate of return, r.
# Given an initial deposit amount, our goal is to find
# the lowest rate of return that enables us to save enough money for the down payment in 3 years.

initial_deposit = float(input("Enter your initial deposit: "))
cost_of_dream_home = float(800000)
portion_down_payment = 0.25
months = 36
tolerance = 100

steps = 0
low = 0.0
high = 1.0
r = (high + low) / 2

while True:
    amount_saved = initial_deposit * (1 + r/12) ** months
    error = amount_saved - cost_of_dream_home * portion_down_payment
    if abs(error) < tolerance:
        break
    if amount_saved > cost_of_dream_home * portion_down_payment:
        high = r
    else:
        low = r
    r = (high + low) / 2
    steps += 1
    if(steps > 1000):
        print("It is not possible to reach the down payment in 3 years with that initial deposit.")
        r = None
        break
        
if r is not None:
    print(f"Best rate of return: {r:.4f}")
    print(f"Steps in bisection search: {steps}")