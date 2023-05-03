import importlib

def read_strings():
    with open("app.py", "r") as file:
        content = file.readlines()
    for line in content:
        if "string_list = [" in line:
            list_content = line.replace("string_list = [", "").replace("]", "").strip()
            if list_content:
                return [s.strip() for s in list_content.split(',')]
            else:
                return []
    return []

def write_strings(strings):
    with open("app.py", "r") as file:
        content = file.readlines()
    for idx, line in enumerate(content):
        if "string_list = [" in line:
            content[idx] = f'string_list = [{", ".join(f"{s!r}" for s in strings)}]\n'
            break
    with open("app.py", "w") as file:
        file.writelines(content)

    # Reload the app.py module
    import app
    importlib.reload(app)
