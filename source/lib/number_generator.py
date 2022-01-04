import random

def get_random_number_list(length, min_num, max_num)-> list:
    values = []
    for i in range(length):
        values.append(format(random.uniform(min_num, max_num), ".2F"))
    return values
    
if __name__ == '__main__':
    values = get_random_number_list(length=30, min_num=0, max_num=0.3)
    for i in values:
        print(i)