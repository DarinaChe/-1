
a = input("Хотите принять участие в викторине по мировым столицам: (Y/N) ")
if a == "N":
    print ("До свиданья!")
else:
    q1 = input("Вопрос №1: выберите столицу России: \n 1. Москва \n 2. Санкт-Петербург \n 3. Екатеринбург \n Введите ваш ответ словом: ")
    q2 = input("Вопрос №2: выберите  столицу Белоруссии: \n 1. Брест \n 2. Минск \n 3. Гродно \n Введите ваш ответ словом: ")
    q3 = input("Вопрос №3: выберите  столицу Финлянции: \n 1. Рукка \n 2. Лахти \n 3. Хельсинки \n Введите ваш ответ словом: ")
    q4 = input("Вопрос №4: выберите  столицу Франции: \n 1. Париж \n 2. Марсель \n 3. Лион \n Введите ваш ответ словом: ")
    q5 = input("Вопрос №5: выберите  столицу Германии: \n 1. Гамбург \n 2. Мюнхен \n 3. Берлин \n Введите ваш ответ словом: ")
    q6 = input("И последний вопрос: выберите  столицу Швеции: \n 1. Гётеборг \n 2. Стокгольм \n 3. Уппсала \n Введите ваш ответ словом:  ")
    my_dict_question = {'Столица России': q1, "Столица Белоруссии": q2, "Столица Финлянции": q3,'Столица Франции': q4, 'Столица Германии': q5, 'Столица Швеции': q6}

    import json
    with open('json_dataq.json','w', encoding="utf8") as outfile:
        json.dump(my_dict_question, outfile)

    answer1 = "Москва"
    answer2 = "Минск"
    answer3 = "Хельсинки"
    answer4 = "Париж"
    answer5 = "Берлин"
    answer6 = "Стокгольм"
    my_dict_answer = {'Столица России': answer1, "Столица Белоруссии": answer2, "Столица Финлянции": answer3, 'Столица Франции': answer4,'Столица Германии': answer5, 'Столица Швеции': answer6}

    import json

    with open('json_dataa.json', 'w', encoding="utf8") as outfile:
        json.dump(my_dict_answer, outfile)

    with open('json_dataq.json','r') as json_file:
         my_dict_question= json.load(json_file)


    with open('json_dataa.json','r') as json_file:
         my_dict_answer= json.load(json_file)


    Score = {k: my_dict_answer[k] for k in my_dict_answer if k in my_dict_question and my_dict_question[k] == my_dict_answer[k]}
    print(f"{'Число правильных ответов:'} {len(Score)}")
