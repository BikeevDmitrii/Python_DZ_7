def export():
    with open('input.txt', encoding='UTF8') as source, open('file.txt', 'a', encoding='UTF8', newline='') as destination:
        for line in source:
            destination.write(line)
    source.close()
    destination.close()
    return
export()
