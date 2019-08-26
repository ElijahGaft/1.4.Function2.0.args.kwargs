import json
from pprint import pprint
### В коментариях есть попытки запихнуть всё в json файл

class PhoneBook:
    def __init__(self, title):
        self.title = title
        self.id = []
        # with open(self.title + '.json', 'w', encoding='utf8') as f:
        #     info = {self.title: []}
        #     json.dump(info, f, ensure_ascii=False, indent=2)
        return

    def add_contact(self, name, surname, phone_num, *args, **kwargs):
        self.name = name
        info = Contact(self.title, self.name, surname, phone_num, *args, **kwargs)
        print(f'В телефонную книгу {self.title} был добавлен контакт с именем {self.name}\n')
        print(info)
        self.id.append(info.create_dict())
        # global new_json
        # with open(self.title + '.json', 'r', encoding='utf8') as f:
        #     old_info = json.load(f)
        #     a = info.create_json()
        #     old_info.get(self.title).append(a)
        #     new_json = old_info
        # with open(self.title + '.json', 'w', encoding='utf8') as f:
        #     json.dump(new_json, f, ensure_ascii=False, indent=2)
        return info

    def show_contacts(self):
        # with open(self.title + '.json', encoding='utf8') as f:
        #     info = json.load(f)
        #     pprint(info) # pprint тоже выводит, но в другом порядке, ПОЧЕМУ?
        for i in self.id:
            print(i)# pprint тоже выводит, но в другом порядке, ПОЧЕМУ?
        return

    def delete_contact(self, del_num):
        for i in self.id:
            if i.get('Телефон') == del_num:
                self.id.remove(i)
        return

    def find_favorite_contact(self):
        for i in self.id:
            if i.get('В избранных') == 'да':
                print('В избранных: ', i)
        return
    def find_contact(self, name, surname):
        for i in self.id:
            if (i.get('Имя') == name) and (i.get('Фамилия') == surname):
                print('Вот информация о контакте: ', i)
        return


class Contact:
    def __init__(self, title, name, surname, phone_num, *args, favorite_contact=False, **kwargs):
        self.title, self.name, self.surname, self.phone_num = title, name, surname, phone_num
        self.favorite_contact = favorite_contact
        if self.favorite_contact == False:
            self.favorite_contact = 'нет'
        else:
            self.favorite_contact = 'да'
        self.args = args
        self.kwargs = kwargs
        return

    def __str__(self):
        additional_inf = ''
        for i in self.args:
            additional_inf = additional_inf + 'Доп. тел.: {}\n\t'.format(i)
        for i in self.kwargs:
            additional_inf = additional_inf + '{}: {}\n\t'.format(i,self.kwargs.get(i))
        info = ('Имя: {0}\nФамилия: {1}\nТелефон: {2}\nВ избранных: {3}\nДополнительная информация:\n\t{4}\n'.
                format(self.name, self.surname, self.phone_num, self.favorite_contact, additional_inf))
        return info

    def create_dict(self):
        additional_inf = {}
        for i in self.args:
            additional_inf['Доп. тел.'] = i
        for i in self.kwargs:
            additional_inf[i] = self.kwargs.get(i)
        info = {'Имя': self.name, 'Фамилия': self.surname, 'Телефон': self.phone_num,
                'В избранных': self.favorite_contact, 'Дополнительная информация': additional_inf}
        return info


if __name__ == '__main__':
    first_book = PhoneBook('first_book')
    first_book.add_contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    first_book.add_contact('Jho', 'Smith', '+74567809', telegram='@jhony', email='jhony@smith.com')
    first_book.show_contacts()
    first_book.delete_contact('+74567809')
    first_book.show_contacts()

    first_book.add_contact('Jhon', 'Smith', '+71234567809', favorite_contact=True, telegram='@jhony',
                           email='jhony@smith.com')
    first_book.find_favorite_contact()
    first_book.find_contact('Jhon', 'Smith')

