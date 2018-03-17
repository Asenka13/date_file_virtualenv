import csv
answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
answer_list = []
for each_answer in answers:
    answer_list.append([each_answer, answers.get(each_answer)])

with open('answers.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';')
    for answer in answer_list:
        writer.writerow(answer)
