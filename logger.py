from controller import get_num

def log():
    with open('file.txt', 'a', encoding='UTF8') as file:
        file.write(get_num() + '\n')
    file.close()

log()
