import shelve

# blt = ['bacon', 'lettuce', 'tomato', 'bread']
# beans_on_toast = ['beans', 'bread']
# scramble_eggs = ['eggs', 'butter', 'milk']
soup = ['tin of soup']
# pasta = ['pasta', 'cheese']

with shelve.open('recipes') as recipes:
    # recipes['blt'] = blt
    # recipes['beans_on_toast'] = beans_on_toast
    # recipes['soup'] = soup
    # recipes['pasta'] = pasta
    # recipes['scramble_eggs'] = scramble_eggs
    # recipes['soup'] = soup

    # recipes['blt'].append('butter')

    temp_list = recipes['blt']
    temp_list.append('butter')
    recipes['blt'] = temp_list

    temp_list = recipes['pasta']
    temp_list.append('tomato')
    recipes['pasta'] = temp_list

    for snack in recipes:
        print(snack, recipes[snack])

