import turtle

def draw_koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            draw_koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def main():
    # Запитуємо користувача про рівень рекурсії
    level = int(input("Введіть рівень рекурсії для фракталу 'Сніжинка Коха': "))
    
    # Створюємо вікно для малювання
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")

    # Створюємо трикутник
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)
    my_turtle.penup()
    my_turtle.goto(-150, 90)
    my_turtle.pendown()

    # Малюємо кожну сторону трикутника
    for _ in range(3):
        draw_koch_snowflake(my_turtle, level, 300)
        my_turtle.right(120)

    # Завершуємо роботу
    window.mainloop()

if __name__ == "__main__":
    main()
