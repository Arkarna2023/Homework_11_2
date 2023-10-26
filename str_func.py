def get_capital_letters(value):
    """функция, возвращает строку заглавными буквами"""
    return value.upper()

def get_capital_letter(value):
    """функцию, которая делает заглавными первые буквы каждого слова в строке,
    поступившей на вход функции."""
    return value.title()

print(get_capital_letter(hello, world))
print(get_capital_letters(hello))