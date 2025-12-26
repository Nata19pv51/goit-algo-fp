import turtle


def fraktal_pifagor(length, level, t):
    # Базовий випадок
    if level <= 0:
        return
    
    t.forward(length)
    # Повертаємо вправо на 30 градусів
    t.right(30)
    fraktal_pifagor(length * 0.75, level-1, t)
    # Повертаємось назад + 30 градусів, щоб повернути вліво
    t.left(60)
    fraktal_pifagor(length * 0.75, level-1, t)
    # Вирівнюємо курсор - повертаємо вправо на 30 градусів
    t.right(30)
    
    t.penup()
    t.backward(length) # Повертаємося назад до основи
    t.pendown()
    
def draw_fraktal():
    window = turtle.Screen()
    window.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.color("red")
    t.pensize(2)
    t.left(90)
    
    try:
        user_level = int(input("Enter the recursion depth: "))
        t.penup()
        t.goto(0, -200)
        t.pendown()
        
        fraktal_pifagor(100, user_level, t)
    except ValueError:
        print("Enter int number!")   

    print("Drawing is done")

    window.exitonclick()

if __name__ == "__main__":
    draw_fraktal()