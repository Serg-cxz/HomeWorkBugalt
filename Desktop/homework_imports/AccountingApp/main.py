import emoji
import datetime  # Импортируем модуль для работы с датой

# Импортируем функции из наших пакетов
from application.db.people import get_employees
from application.salary import calculate_salary

# Этот блок выполняется только если мы запускаем этот файл напрямую
if __name__ == '__main__':
    # Выводим текущую дату
    print(f"📅 Сегодня: {datetime.date.today()}")

    # Вызываем наши функции
    get_employees()
    calculate_salary()

print(emoji.emojize('Работа завершена! :thumbs_up:'))