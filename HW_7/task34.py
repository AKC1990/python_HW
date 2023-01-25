def check_rhyme(string):
    vowel_letters = 'ёуеэоаыяию'
    result_list = list()
    for i in string.split():
        count = 0
        for j in i:
            if j in vowel_letters:
                count += 1
        result_list.append(count)
    
    for i in range(len(result_list)-1):
        if result_list[i] != result_list[i+1]:
            return 'Пам парам'
    return 'Парам пам-пам'                

text = 'пара-ра-рам рам-пам-папам пара-па-дам'
print(check_rhyme(text))
