def find_leapyear(y):
    if not y % 4:
        if not y % 100:
            if not y % 400:
                return "yes"
            else:
                return "no"
        else:
            return "yes"
    else:
        return "no"
