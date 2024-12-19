import random
import numpy as np
import matplotlib.pyplot as plt
def objective_function(x):
# Example higher-degree function: f(x) = -x^4 + 4x^3 -6x + 4
    return -x**4 + 4 * x**3 - 6 * x + 4

def hill_climbing(objective_function, start, step_size, lower_bound, upper_bound, max_iterations=1000):
# Start with a random point in the range
    current_x= start
    current_value= objective_function(current_x)

    for _ in range(max_iterations):
    # Generate neighbors by moving left and right
        left_x = current_x-step_size
        right_x = current_x+ step_size
        # Ensure neighbors are within bounds
        left_x = max(left_x, lower_bound)
        right_x = min(right_x, upper_bound)

        # Evaluate the neighbors
        left_value= objective_function(left_x)
        right_value= objective_function(right_x)

        # Choose the neighbor with the highest value
        if left_value > current_value:
            current_x= left_x
            current_value = left_value
        elif right_value > current_value:
            current_x= right_x
            current_value = right_value
        else:
            # No improvement found, break the loop
            break

    return current_x, current_value

def plot_function(objective_function, lower_bound, upper_bound, max_x=None, max_value=None, start_x=None):
    x = np.linspace(lower_bound, upper_bound, 400)
    y = objective_function(x)
    # plt.plot(x, y, label="f(x) = -x^4 + 4x^3 -6x^2 + 4x + 10")
    plt.plot(x, y, label="f(x) = -x^4 + 4x^3 -6x + 4")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Objective Function with Hill Climbing Result")
    start_value = objective_function(start)
    if start is not None and start_value is not None:
        plt.plot(start, start_value, 'go', label=f"Initial: f({start:.2f}) = {start_value:.2f}")
    if start_x is not None:
        plt.plot(start_x, objective_function(start_x), 'bo', label=f"Start: x = {start_x:.2f}")
    if max_x is not None and max_value is not None:
        plt.plot(max_x, max_value, 'ro', label=f"MaximumFound: f({max_x:.2f}) = {max_value:.2f}")
    plt.legend()
    plt.grid(True)
    plt.show()

    
# Parameters
lower_bound= -1.3
upper_bound= 3.63
start = random.uniform(lower_bound, upper_bound)
step_size= 0.01
# Apply hill climbing to maximize the function
max_x, max_value= hill_climbing(objective_function, start, step_size, lower_bound, upper_bound)
print(f"Initialpoint: x = {start:.2f}")
print(f"Maximum value of the function found: f({max_x:.2f}) = {max_value}")
# Plot the function and the maximum point found by hill climbing
plot_function(objective_function, lower_bound, upper_bound, max_x, max_value, start)