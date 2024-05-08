def palindrom_chek(text: str) -> str:
    if text == text[::-1]:
        return "Palindrom"
    else:
        return  "Ne palindrom"

