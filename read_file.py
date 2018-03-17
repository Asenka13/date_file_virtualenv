import win_unicode_console
win_unicode_console.enable()
summ_words = 0
with open('referat.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.isspace() == False:
            summ_words += line.count(' ') + 1
            print(line)
    print(summ_words)
