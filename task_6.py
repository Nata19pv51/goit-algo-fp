def greedy_algorithm (items, budget):
    # items.sort(key=lambda x: x., reverse=True)
    sorted_items = sorted(items.items(), key=lambda item: item[1]["calories"]/item[1]["cost"], reverse=True)
    # print(sorted_by_cost)
    total_calories = 0
    menu_lst = []
    
    for name, info in sorted_items:
        # for property, val in data.items():
        if budget >= info["cost"]:
            budget -= info["cost"]
            total_calories += info["calories"]
            menu_lst.append(name)
    return (total_calories, menu_lst)


def dynamic_programming(items, budget):
    # створюємо таблицю K для зберігання оптимальних значень підзадач
    n = len(items)
    
    meals = list(items.keys())
    cost = [item["cost"] for item in items.values()]
    calory = [item["calories"] for item in items.values()]
    K = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    
    # будуємо таблицю K знизу вгору
    for i in range(n + 1):
        for w in range(budget + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif cost[i - 1] <= w:
                # Вирішуємо: брати страву чи ні?
                K[i][w] = max(calory[i - 1] + K[i - 1][w - cost[i - 1]], K[i - 1][w])
            else:
                # Якщо страва занадто дорога, залишаємо попередній результат
                K[i][w] = K[i - 1][w]

    total_calories = K[n][budget]
    selected_items = []
    
    for i in range(n, 0, -1):
        if K[i][budget] != K[i-1][budget]:
            selected_items.append(meals[i-1])
            budget -= cost[i-1]
    return total_calories, selected_items


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
# sorted_by_cost = dict(sorted(items.items(), key=lambda item: item[1]["calories"]/item[1]["cost"], reverse=True))
# print(sorted_by_cost)
print(greedy_algorithm(items, 150))
print(dynamic_programming(items, 150))
