def seasons(month: int) -> str:
    if month == 1 and 2 and 12:
        return "winter"
    elif month == 3 and 4 and 5:
        return "spring"
    elif month == 6 and 7 and 8:
        return "summer"
    elif month == 9 and 10 and 11:
        return "autumn"
    