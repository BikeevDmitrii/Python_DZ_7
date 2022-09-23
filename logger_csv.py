from controller import a, b, c, d

def logs():
    import csv 
    with open('Telephone_book.csv', 'a', encoding='UTF8', newline='') as csv_file: 
        writer = csv.writer(csv_file) 
        g= [a,b,c,d]
        writer.writerow(g)
    csv_file.close()
    return 

logs()