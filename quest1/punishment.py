def do_punishment(first_part, second_part, nb_lines):
    concat = f"{first_part} {second_part}"
    res = ""

    for i in range(nb_lines):
        res += concat
        
        if i != nb_lines-1:
            res += " "

    return res
