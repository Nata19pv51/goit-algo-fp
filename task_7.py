import random
import matplotlib.pyplot as plt


def catch_cubes(total_throws):
    sums_counter = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    
    for i in range(0, total_throws):
        number1 = random.randint(1, 6)
        number2 = random.randint(1, 6)
        sum_numbers = number1 + number2
        sums_counter[sum_numbers] += 1
    
    probability = {}
    for key, val in sums_counter.items():
        probability[key] = {}
        probability[key]["probability"] = round(val/total_throws * 100, 2)
        probability[key]["count"] = val

    return probability

def create_plot(data):
    x_values = [k for k in data]
    y_values = [val['probability'] for val in data.values()]

    # 2. Create the plot
    plt.plot(x_values, y_values)

    # 3. Add labels and a title for clarity
    plt.xlabel('Sum')
    plt.ylabel('Probability')
    plt.title('Sums Probability')

    # 4. Display the plot
    plt.show()
    
def print_as_table(data):
    print(f"{'Сума':<10} | {'Кількість':<10} | {'Ймовірність':<15}")
    print("-" * 40)
    for key, val in data.items():
        # Тут data[key] — це твій вкладений словник із помилкою, яку ми виправляли
        print(f"{key:<10} | {val['count']:<10} | {val['probability']:>10}%")
      

if __name__ == "__main__":
    total_throws = 36
    sums = catch_cubes(total_throws)
    print(sums)
    
    # print(f"{'Name':15} | {'Phone':10}")
    # print(f"{'Сума':15}     | {'Імовірність':10}")
    # print("-" * 28)
    # for key, val in sums.items():
    #     print(f"{key:15}       | {val['probability']:10d}% ({val['count']}/{total_throws})")
    print_as_table(sums)
    create_plot(sums)
    