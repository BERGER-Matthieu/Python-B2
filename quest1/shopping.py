def remember_the_milk(shopping_list):
    shopping_list = clean_list(shopping_list)
    shopping_list_len = len(shopping_list)

    if len(shopping_list) == 0:
        return shopping_list

    milk = False
    new_products_list = []

    for product in shopping_list:
        if product.split()[-1] == "Milk":
            milk = True

    if not milk:
        shopping_list.append(f"{shopping_list_len + 1}/ Milk")
 
    return shopping_list

def clean_list(shopping_list):
    new_shopping_list = []

    for i in range(len(shopping_list)):
        new_shopping_list.append(f"{i+1}/ {shopping_list[i].strip().capitalize()}")

    return new_shopping_list
