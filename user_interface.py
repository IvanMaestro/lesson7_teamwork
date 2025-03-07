import excep


def load_menu_main():
    menu = {}
    menu[1] = ('Рациональные числами', 'rational')
    menu[2] = ('Комплексные числами', 'complex')
    menu[0] = ('выход', 'exit')
    return menu


def load_menu_operation():
    menu = {}
    menu[1] = ('Сложение', 'sum')
    menu[2] = ('Вычитание', 'sub')
    menu[3] = ('Умножение', 'mult')
    menu[4] = ('Деление', 'div')
    menu[5] = ('Возведение в степень', 'pow')
    menu[6] = ('Вычисление корня числа', 'sqrt')
    menu[0] = ('назад', 'back')
    return menu


def load_menu_operation_div():
    menu = {}
    menu[1] = ('Обычное деление', 'div')
    menu[2] = ('Целочисленное деление', 'div_int')
    menu[3] = ('Остаток от деления', 'rem_div')
    menu[0] = ('назад', 'back')
    return menu


def print_menu(menu_title, menu_data):
    print(f'----- {menu_title} -----')

    for key_menu, title_menu in menu_data.items():
        print(key_menu, '-', title_menu[0])


def get_select_menu(menu):
    select_str = input('выберите пункт меню: ')
    while not select_str.isdigit() or int(select_str) not in menu.keys():
        print('error - указан неверный пункт меню!')
        select_str = input('выберите пункт меню: ')
    return int(select_str)


def input_rational_number(title=''):
    print('Введите рациональное число: ')
    number_str = input(f'{title}:')
    number = excep.check_input_data(number_str)
    while number is None:
        print('введённая строка должна быть числом!')
        number_str = input(f'{title}:')
        number = excep.check_input_data(number_str)
    return number


def print_rational_number(value, prefix=''):
    print(f'{prefix}: {value}')


def input_complex_number(postfix=''):
    print('Комплексное число имеет вид A+Bi, где A и B – действительные числа, i – так называемая мнимая единица')
    numberA_str = input(f'Введите значение A {postfix}: ')
    numberA = excep.check_input_data(numberA_str)
    while numberA is None:
        print('введённая строка должна быть числом!')
        numberA_str = input(f'Введите значение A {postfix}: ')
        numberA = excep.check_input_data(numberA_str)

    numberB_str = input(f'Введите значение B {postfix}: ')
    numberB = excep.check_input_data(numberB_str)
    while numberB is None:
        print('введённая строка должна быть числом!')
        numberB_str = input(f'Введите значение B {postfix}: ')
        numberB = excep.check_input_data(numberB_str)

    complex_number = complex(numberA, numberB)
    print(complex_number)

    return complex_number


def print_complex_number(value, prefix=''):
    print(f'{prefix}: {value}')


def input_operation_data(operator, type_number='rational'):
    if type_number == 'rational':
        input_func_number = input_rational_number
    else:
        input_func_number = input_complex_number

    if operator == 'sum':
        number1 = input_func_number('Введите 1-е слогаемое')
        number2 = input_func_number('Введите 2-е слогаемое')
        return [number1, number2]
    if operator == 'sub':
        number1 = input_func_number('Введите уменьшаемое')
        number2 = input_func_number('Введите вычитаемое')
        return [number1, number2]
    if operator == 'mult':
        number1 = input_func_number('Введите 1-й множитель')
        number2 = input_func_number('Введите 2-й множитель')
        return [number1, number2]
    if operator == 'div' or operator == 'div_int' or operator == 'rem_div':
        number1 = input_func_number('Введите делимое')
        number2 = input_func_number('Введите делитель')
        if number2 == 0:
            print('Делить на 0 нельзя!')
            return None
        return [number1, number2]
    if operator == 'pow':
        number1 = input_func_number('Введите число')
        number2 = input_func_number('Введите степень')
        return [number1, number2]
    if operator == 'sqrt':
        number1 = input_func_number('Введите число')
        return [number1]
    else:
        return None
