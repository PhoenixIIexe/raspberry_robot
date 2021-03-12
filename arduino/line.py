#Указывать файл внизу
def database_of_data(file_name):
    file_action = int()
    file_information = str()
    i = int(0)

    while file_action != -1:
        main_new_file = []
        file_action = int(input("Видите цифру функции, которую хотите использовать \n Добавить пользователя: 1, Изменить данные пользователя: 2, Удалить пользователя: 3, Вывести данные базы: 4, Очистеть базу данных: 5. \n"))
        if file_action == 1:
            file = open(str(file_name),'a')
            file_information = input("Добавьте информацию: ")
            file.write(file_information + '\n') 
        elif file_action == 2: 
            file = open(str(file_name),'r')
            file_information = int(input("Номер пользователя? ")) - 1
            new_file = list(file.readlines())
            #print(new_file)
            for i in range(0,len(new_file)):
                if i != file_information:
                    main_new_file.append(new_file[i])
                else:
                    file_information = input("Добавьте информацию: ")
                    main_new_file.append(file_information + '\n')
            #print(main_new_file)
            file.close()
            file = open(str(file_name),'w')
            file.write(''.join(main_new_file))
        elif file_action == 3:
            file = open(str(file_name),'r')
            file_information = int(input("Номер пользователя? ")) - 1
            new_file = list(file.readlines())
            #print(new_file)
            for i in range(0,len(new_file)):
                if i != file_information:
                    main_new_file.append(new_file[i])
            #print(main_new_file)
            file.close()
            file = open(str(file_name),'w')
            file.write(''.join(main_new_file))
        elif file_action == 4:
            file = open(str(file_name),"r")
            print(file.read())
        elif file_action == 5:
            file = open(str(file_name),"w")
            file.close()
        file.close()

name_file = input("Укажите свой файл с .txt ") #Укажите свой файл
database_of_data(name_file)