def greedy_algorithm (items, budget):
    sorted_items = sorted(items.items(), key=lambda item: item[1]["calories"]/item[1]["cost"], reverse=True)
    total_calories = 0
    menu_lst = []
    
    for name, info in sorted_items:
        while budget >= info["cost"]:
            budget -= info["cost"]
            total_calories += info["calories"]
            menu_lst.append(name)
    return (total_calories, menu_lst)


def dynamic_programming(items, budget):
    n = len(items)
    meals = list(items.keys())
    cost = [item["cost"] for item in items.values()]
    calory = [item["calories"] for item in items.values()]
    
    # Будуємо таблицю K
    K = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
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
    
    residual = budget
    for i in range(n, 0, -1):
        if K[i][residual] != K[i-1][residual]:
            selected_items.append(meals[i-1])
            residual -= cost[i-1]
            
    return total_calories, selected_items


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

print(greedy_algorithm(items, 85))
print(dynamic_programming(items, 85))
