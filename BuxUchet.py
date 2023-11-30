import random
import os
from colorama import init, Fore, Style, deinit

init(autoreset=True)

dictBuh = {

    "Раздел I: Внеоборотные активы [01-09]":
    {
        "01": "Основные средства",
         "02": "Амортизация основных средств",
         "03": "Доходные вложения в материальные ценности",
         "04": "Нематериальные активы",
         "05": "Амортизация нематериальных активов",
         "07": "Оборудование к установке",
         "08": "Вложения во внеоборотные активы",
         "09": "Отложенные налоговые активы",
     },

    "Раздел II. Производственные запасы [10-18]":
    {
        "10": "Материалы",
        "11": "Животные на выращивании и откорме",
        "14": "Резервы под снижение стоимости материальных ценностей",
        "15": "Заготовление и приобретение материальных ценностей",
        "16": "Отклонение в стоимости материальных ценностей",
        "19": "Налог на добавленную стоимость по приобретенным ценностям"
    },

    "Раздел III. Затраты на производство [20-29]":
    {
        "20": "Основное производство",
        "21": "Полуфабрикаты собственного производства",
        "23": "Вспомогательные производства",
        "25": "Общепроизводственные расходы",
        "26": "Общехозяйственные расходы",
        "28": "Брак в производстве",
        "29": "Обслуживающие производства и хозяйства"
    },

    "Раздел IV. Готовая продукция и товары [40-46]":
    {
        "40": "Выпуск продукции (работ, услуг)",
        "41": "Товары",
        "42": "Торговая наценка",
        "43": "Готовая продукция",
        "44": "Расходы на продажу",
        "45": "Товары отгруженные",
        "46": "Выполненные этапы по незавершенным работам"
    },

    "Раздел V. Денежные средства [50-59]":
    {
        "50": "Касса",
        "51": "Расчетные счета",
        "52": "Валютные счета",
        "55": "Специальные счета в банках",
        "57": "Переводы в пути",
        "58": "Финансовые вложения",
        "59": "Резервы под обесценение финансовых вложений"
    },

    "Раздел VI. Расчеты [60-79]":
    {
        "60": "Расчеты с поставщиками и подрядчиками",
        "62": "Расчеты с покупателями и заказчиками",
        "63": "Резервы по сомнительным долгам",
        "66": "Расчеты по краткосрочным кредитам и займам",
        "67": "Расчеты по долгосрочным кредитам и займам",
        "68": "Расчеты по налогам и сборам",
        "69": "Расчеты по социальному страхованию и обеспечению",
        "70": "Расчеты с персоналом по оплате труда",
        "71": "Расчеты с подотчетными лицами",
        "73": "Расчеты с персоналом по прочим операциям",
        "75": "Расчеты с учредителями",
        "76": "Расчеты с разными дебиторами и кредиторами",
        "77": "Отложенные налоговые обязательства",
        "79": "Внутрихозяйственные расчеты"
    },

    "Раздел VII. Капитал [80-86]":
    {
        "80": "Уставный капитал",
        "81": "Собственные акции (доли)",
        "82": "Резервный капитал",
        "83": "Добавочный капитал",
        "84": "Нераспределенная прибыль (непокрытый убыток)",
        "86": "Целевое финансирование"
    },

    "Раздел VIII. Финансовые результаты [90-99]":
    {
        "90": "Продажи",
        "91": "Прочие доходы и расходы",
        "94": "Недостачи и потери от порчи ценностей",
        "96": "Резервы предстоящих расходов",
        "97": "Расходы будущих периодов",
        "98": "Доходы будущих периодов",
        "99": "Прибыли и убытки"
    }
}

# Переменная для хранения общего количества значений
total_values_count = sum(len(section) for section in dictBuh.values())

# Функция для подсчета общего количества значений
def count_total_values():
    return total_values_count

print(f"Общее количество счетов: {count_total_values()}")

# Функция для вывода всех значений без выбора раздела
def display_all_values():
    for section_name, section in dictBuh.items():
        print(f"\nРаздел '{section_name}':")
        for account, value in section.items():
            print(f"Счет {Fore.GREEN}{account}{Style.RESET_ALL}: {value}")


# Функция для очистки консоли
def clear_console():
    if os.name == 'nt':
        os.system('cls')  # Для Windows
    else:
        os.system('clear')  # Для macOS и Linux

# Функция для вывода названия раздела по номеру
def get_section_name(section_number):
    sections = list(dictBuh.keys())
    if section_number >= 1 and section_number <= len(sections):
        return sections[section_number - 1]
    else:
        return None

# Функция для вывода конкретного раздела и его значений
def display_section(section_name):
    while True:  # Добавляем цикл для возможности возврата
        if section_name in dictBuh:
            section = dictBuh[section_name]
            print(f"\nРаздел '{section_name}':")
            for account, value in section.items():
                print(f"Счет {account}: {value}")

            print("\nВыберите действие:")
            print("1 - Вернуться к выбору действий;")
            print("2 - Выйти из раздела.")

            sub_choice = input("\nВведите номер выбора: ")

            if sub_choice == "1":
                return  # Возвращаемся к выбору действий
            elif sub_choice == "2":
                break  # Выходим из текущего раздела
            else:
                print(f"\n{Fore.RED}Неверный выбор. Пожалуйста, выберите существующий номер действия.{Style.RESET_ALL}\n")
        else:
            print(f"\nРаздел '{section_name}' не найден в словаре.\n")
            return  # Возвращаемся к выбору действий

# Функция для игры "угадайку"
def guess_account():
    while True:
        print("\nВыберите действие:\n")
        print("1 - Играть в 'угадайку';")
        print("2 - Очистить консоль;")
        print("3 - Вывести название раздела и его значения;")
        print("4 - Вывести все значения в разделе;")
        print("5 - Выйти из программы.")

        choice = input("\nВведите номер выбора: ")

        if choice == "1":
            print("\nВыберите раздел:\n")
            sections = list(dictBuh.keys())
            for i, section in enumerate(sections, start=1):
                print(f"{i} - {section}")

            section_choice = int(input("\nВведите номер раздела: "))

            section_name = get_section_name(section_choice)
            if section_name is not None:
                random_account = random.choice(list(dictBuh[section_name].keys()))
                correct_answer = dictBuh[section_name][random_account]
                user_guess = input(f"Угадайте название счета с номером {Fore.GREEN}{random_account}{Style.RESET_ALL} из раздела '{section_name}': ")

                if user_guess.lower() in correct_answer.lower():
                    print(f"\n{Fore.GREEN}Правильно! Правильный ответ:{Style.RESET_ALL} {correct_answer}\n")
                else:
                    print(f"\n{Fore.RED}Неправильно.{Style.RESET_ALL} {Fore.GREEN}Правильный ответ:{Style.RESET_ALL} {correct_answer}\n")
            else:
                print(f"\n{Fore.RED}Неверный выбор раздела.{Style.RESET_ALL}\n")
        elif choice == "2":
            clear_console()
        elif choice == "3":
            print("\nВыберите раздел:\n")
            sections = list(dictBuh.keys())
            for i, section in enumerate(sections, start=1):
                print(f"{i} - {section}")

            section_choice = int(input("\nВведите номер раздела: "))
            section_name = get_section_name(section_choice)

            if section_name is not None:
                display_section(section_name)
            else:
                print(f"{Fore.RED}Неверный выбор раздела.{Style.RESET_ALL}\n")
        elif choice == "4":
            display_all_values()  # Вывести все значения без выбора раздела
        elif choice == "5":
            break
        else:
            print(f"\n{Fore.RED}Неверный выбор. Пожалуйста, выберите существующий номер действия.{Style.RESET_ALL}\n")

deinit()

# Запуск программы
guess_account()