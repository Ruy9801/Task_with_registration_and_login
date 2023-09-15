



def create():
    with open('database.txt', 'r') as files:
        count_id = files.read().split('\n')

    with open('database.txt', 'a') as file:
        numid = len(count_id)

        title = input('Введите название продукта: ').title()
        price = int(input('Введите цену: '))
        category = input('Введите категорию: ').title()
        

        dict1 = {
            'id': numid,
            'title': title,
            'price': price,
            'categry': category
        
        }
        file.write(str(f'{dict1}\n'))
    print(f'Новый продукт создан под id: {numid}')
        

        


def read():
    with open('database.txt', 'r') as file:
        print(file.read())
   


def get_one(id):

    with open('database.txt','r') as file:
        read = file.read().split('\n')
        print(read[id-1])




def update(ids):

    with open('database.txt','r') as file:

        part1 = file.read().split('\n')
        title = input('Введите название товара: ').title()
        price = int(input('Введите цену товара: '))
        category = input('Введите категорию товара: ').title()

        dict1 = {
            'id': ids,
            'title': title,
            'price': price,
            'categry': category
        }
    print('Продукт успешно изменён!')

    with open('database.txt', 'w') as file1:
        part1[ids - 1] = dict1
        print(dict1)
        for i in part1:
            if i == '':
                file1.write(str(f'{i}'))
            elif i == i:
                file1.write(str(f'{i}\n'))
            




def delete(index):
    with open('database.txt', 'r') as file:
        part1 = file.read().split('\n')
        if index > len(part1):
            print('\n\tid not found!\n')
        
        else:

            with open('database.txt', 'w') as file1:
                part1[index - 1] = 'Deleted product  id: 3'
                for i in part1:
                    file1.write(str(f'{i}\n'))
                print('\nDeleted!\n')








while True:

    def main():
        print('Привет, вам доступны следующие функции:\n\tPOST\n\tGET\n\tDETAIL\n\tPUT\n\tDELETE')
        method = input('Введите одну из функции: ').upper()

        if method == 'GET':
            read()

        elif method == 'DETAIL':
            id = int(input('Введите id: '))
            get_one(id)

        elif method == 'POST':
            create()


        elif method == 'PUT':
            id = int(input('Введите id: '))
            update(id)

        elif method == 'DELETE':
            id = int(input('Введите id: '))
            delete(id)


    main()
