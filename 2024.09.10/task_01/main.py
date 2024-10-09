def split_text(txt: str, separas: list[str]) -> list[str]:
    result: list[str] = ['']
    waiting_for_serparator: bool = True

    for symbol in txt:
    return result
if __name__ == '__main__':
    test_str = "Вышел корень из тумана. Вынул ножик из кармана. Раз, два, всё."
    separators: list[str] = [';', '.']
    print(split_text(test_str, separators)