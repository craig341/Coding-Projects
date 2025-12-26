import random
import matplotlib.pyplot as plt

bag = []


def refill():
    global bag

    bag = []

    for _ in range(9):
        bag.append('red')

    for _ in range(7):
        bag.append('yellow')

    for _ in range(4):
        bag.append('green')


def take_button():
    button_i = random.randrange(0, len(bag)-1)
    bag.pop(button_i)
    return bag[button_i]


def my_func(iterations):
    refill()

    total_bags = 0
    two_colours = 0
    colours_taken = []
    # Lists to store data for plotting
    iteration_counts = []
    percentage_values = []
    for i in range(iterations):
        for _ in range(3):
            colours_taken.append(take_button())

        # print('Taken: ', end='')
        # for i, colour in enumerate(colours_taken):
        #     if i == 2:
        #         print(colour)
        #     else:
        #         print(colour + ', ', end='')

        if colours_taken.count('red') == 2 or colours_taken.count('yellow') == 2 or colours_taken.count('green') == 2:
            two_colours += 1

        refill()
        colours_taken = []
        total_bags += 1
        # print(f'P(two colours) = {two_colours}/{total_bags} = {100*two_colours/total_bags}%')
        # print('===========================')

    print(f'P(two colours) = {two_colours}/{total_bags} = {100*two_colours/total_bags}%')
    iteration_counts.append(iterations)
    percentage_values.append(100 * two_colours / total_bags)
    return iteration_counts, percentage_values

all_iterations = []
all_percentages = []

for i in range(10, 1000, 10):  
    x_vals, y_vals = my_func(i)
    all_iterations.extend(x_vals)
    all_percentages.extend(y_vals)

plt.plot(all_iterations, all_percentages)
plt.xlabel('Iterations')
plt.ylabel('Percentage of Two-Colours Outcomes')
plt.title('Probability of Drawing Exactly Two Buttons of the Same Colour')
plt.grid(True)
plt.show()