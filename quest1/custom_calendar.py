ntd = {
    1 : "monday",
    2 : "tuesday",
    3 : "wednesday",
    4 : "thursday",
    5 : "friday",
    6 : "saturday",
    7 : "sunday"
}

dtn = {
    "monday" : 1,
    "tuesday" : 2,
    "wednesday" : 3,
    "thursday" : 4,
    "friday" : 5,
    "saturday" : 6,
    "sunday" : 7
}

def day_from_number(number):
    if number > 7 or number < 1:
        return None
    return ntd[number]

def day_to_number(day):
    if day in dtn :
        return dtn[day]
    return None
