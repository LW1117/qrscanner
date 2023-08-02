from save import savedata
from openlink import openlink
from browse import scan

data = None
while True:
    print('\n1.Scan\n2.Display data\n3.Open link\n4.Save\n5.Exit')
    choice = int(input('Enter your choice : '))
    if choice == 1:
        data = scan()
    elif choice == 2:
        print(f'\n\n{data}')
    elif choice == 3:
        openlink(data)
    elif choice == 4:
        savedata(data)
    elif choice == 5:
        exit()
