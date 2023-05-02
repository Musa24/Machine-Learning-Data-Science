import numpy as np
import matplotlib.pyplot as plt
# Get The User Inputs
a1 = int(input("a1:"))
b1 = int(input("b1:"))
a2 = int(input("a2:"))
c2 = int(input("c2:"))

# Create functions


def fun1(x):
    return a1 * x + b1


def fun2(x):
    return a2 * x**2 + c2

#  Find the intersection points by solving the equation f1(x) = f2(x)


def calc_points_intersection():
    x_values = np.arange(-10, 10, 0.001)
    y_values_1 = fun1(x_values)
    y_values_2 = fun2(x_values)

    intersection_points = []
    for i in range(len(x_values) - 1):
        if np.sign(y_values_1[i] - y_values_2[i]) != np.sign(y_values_1[i + 1] - y_values_2[i + 1]):
            x_intersect = (x_values[i] + x_values[i + 1]) / 2
            y_intersect = fun1(x_intersect)
            intersection_points.append((x_intersect, y_intersect))
            print(intersection_points)

    return intersection_points


# intersection_points = calc_points_intersection()

# print(intersection_points)


# Plot the graphs of the two equations and the intersection points
x_values = np.arange(-10, 10, 0.001)
y_values_1 = fun1(x_values)
y_values_2 = fun2(x_values)

plt.plot(x_values, y_values_1, label='y = {}x + {}'.format(a1, b1))
plt.plot(x_values, y_values_2, label='y = {}x^2 + {}'.format(a2, c2))
intersection_points = calc_points_intersection()
print(intersection_points)
for point in intersection_points:
    plt.plot(1, 7, 'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphs of Two Equations')
plt.legend()
plt.show()
