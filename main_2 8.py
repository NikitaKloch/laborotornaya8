import sys
from datetime import datetime, timedelta
import datetime


# Фамилия
# Имя
# Номер телефона
# Дата рождения (ДД ММ ГГГГ)

if __name__ == '__main__':
    spisok = []
    new_spisok = []

    def title_name():
        title_name = '| {:^4} | {:^30} | {:^15} | {:^30} | {:^30} | '.format(
                    "№",
                    "Фамилия",
                    "Имя",
                    "Телефон",
                    "Дата рожения"
                )
        return title_name

    def setka_table():
        setka_table = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 15,
                '-' * 30,
                '-' * 30
            )
        return setka_table

    def output_table(kek):
        post = []
        for idx, spisok_new in enumerate(kek, 1):
            post.append(
                '| {:>4} | {:<30} | {:<15} | {:<30} | {:<30} | '.format(
                    idx,
                    spisok_new.get('surname', ''),
                    spisok_new.get('name', ''),
                    spisok_new.get('phone', ''),
                    spisok_new.get('data', 0)
                )
            )
        return post

    listing = []
    
    while True:
        command = input(">>> ").lower()
    
    
        if command  == 'exit':
            break
    
    
        elif command == 'add':
            surname = input('Фамилия: ')
            name = input('Имя: ')
            phone = input('Телефон: ')
    
            day, month, year = input('Дата рожения (ДД ММ ГГГГ): ').split(' ')
            dates = f'{day} {month} {year}'
    
            time_list = {
            'surname': surname,
            'name': name,
            'phone': phone,
            'data': dates
            }
    
            listing.append(time_list)
    
            if len(listing) > 1:
                listing.sort(key=lambda item: item.get('data', ''))
    
        elif command == 'list':
            print(setka_table())
            print(title_name())
            print(setka_table())
    
            for isss in output_table(listing):
                print(isss)
    
            print(setka_table())
    
        elif command == 'phone':
            search_phone = input('Введите номер телефона: ')
            new_listing = []
            for phone_item in listing:
                if search_phone == phone_item['phone']:
                    new_listing.append(phone_item)
    
            if len(new_listing) > 0:
                print(setka_table())
                print(title_name())
                print(setka_table())
                for issssa in output_table(new_listing):
                    print(issssa)
                print(setka_table())
            else:
                print('Такого номера не найдено!', file=sys.stderr)
        elif command == 'help':
                print('Список команд:\n')
                print('add - добавить пользователя.')
                print('list - вывести список пользователей.')
                print('find <Номер телефона> - запросить пользователей по номеру телефона.')
                print('help - Справочник.')
                print('exit - Завершить пработу программы.')
        else:
            print(f'Команда <{command}> не существует.', file=sys.stderr)
            print('Введите <help> для просмотра доступных команд')
