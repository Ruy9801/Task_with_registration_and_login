
def registration():

    with open('data.txt','a') as file:

        email = input('Enter email: ')
        password = input('Enter password: ')
        if '@email.' in email or '@gmail.' in email:
            file.write(f'\n{email}\n{password}')
            print('Регистрация завершена')
        else:
            print('Вы неправильно ввели email!')




def login():
    with open('data.txt') as file:

        checkemail = input('Enter your email: ')
        checkpassword = input('Enter your password: ')

        log = file.readlines()
        logs = [i.replace('\n','') for i in log]

        
        if checkemail in logs:
            if checkpassword in logs:
                print('Доступ разрещен!')
        else:
            print('В доступе отказано')

