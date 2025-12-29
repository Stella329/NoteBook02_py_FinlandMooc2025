# Hint: it might be best to first read through all the lines in the file and pop them into a list, which is then easier to manipulate in the way described in the exercise.

def make_receipt_book(filename: str):
    """aim: combine multiple files' data into one;
    NB: The recipe ends with an empty line, with the exception of the final recipe in the file which just ends with the end of the file"""
    receipe_book = []

    with open (filename) as file:
        dish = []

        for line in file:
            line = line.strip()     # 处理行末'\n'
            if line:        # 判断是否为空
                dish.append(line)
            else:       # 遇到空行
                if dish:        # 遇到空行时：如果当前菜谱有内容则添加+重置菜谱，开启下一道菜
                    receipe_book.append(dish)
                    dish = []

        # 处理最后一个菜谱（没有空行结尾）
        if dish:
            receipe_book.append(dish)
    return receipe_book



# Part 1: Search for recipes based on the name of the recipe

def search_by_name(filename: str, word: str) -> list: 
    '''The function should go through the file and select all recipes whose name contains the given search string. The names of these recipes are then returned in a list.'''
    found_names = []
    receipe_book = make_receipt_book(filename)
    for lst in receipe_book:
        if word.lower() in lst[0].lower():
            found_names.append(lst[0])

    return found_names


# Part 2 Search for recipes based on the preparation time

def search_by_time(filename: str, prep_time: int)->list: 
    '''The function should go through the file and select all recipes whose preparation time is at most the number given.
    The names of these recipes are again returned in a list, but the preparation time should be appended to each name.'''
    found = []
    receipe_book = make_receipt_book(filename)
    for lst in receipe_book:
        if int(lst[1]) <= prep_time:
            name = lst[0]
            return_line = f'{name}, preparation time {lst[1]} min'
            found.append(return_line)
    return found


# Part3 Search for recipes based on the ingredients

def search_by_ingredient(filename: str, ingredient: str) -> list:
    '''The function should go through the file and select all recipes whose ingredients contain the given search string.
    The names of these recipes are returned in a list just like in the second part, with the preparation time appended'''
    found = []
    receipe_book = make_receipt_book(filename)
    for lst in receipe_book:
        if ingredient in lst[2:]:
            name = lst[0]
            return_line = f'{name}, preparation time {lst[1]} min'
            found.append(return_line)
    return found


if __name__ == "__main__":
    # found_recipes = search_by_name("recipes1.txt", "cake")

    # print (found_recipes)
    # for recipe in found_recipes:
    #     print(recipe)

    # found_recipes = search_by_time("recipes1.txt", 20)

    # for recipe in found_recipes:
    #     print(recipe)


    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)