def get_input_text() -> str:
    with open('input.txt', 'rb') as f:
        return f.read().decode('utf8')
    

def get_input_lines() -> list[str]:
    return get_input_text().splitlines()