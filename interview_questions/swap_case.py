

if __name__ == '__main__':
    str_to_convert = 'HackerRank.com presents "Pythonist 2".'
    converted_str = "".join([ch.upper() if ch == ch.lower() else ch.lower() for ch in str_to_convert])
    print(str_to_convert)
    print(converted_str)
