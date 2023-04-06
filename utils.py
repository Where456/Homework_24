import re


def filters(file: list[str], cmd: str, value: str) -> list[str]:
    if cmd == 'filter':
        return list(filter(lambda d: value in d, file))
    if cmd == 'map':
        return list(map(lambda d: d.split()[int(value)], file))
    if cmd == 'unique':
        return list(set(file))
    if cmd == 'sort':
        reverse = value == 'asc'
        return sorted(file, reverse=reverse)
    if cmd == 'limit':
        return [i for i in file[:int(value)]]
    if cmd == 'regex':
        prog = re.compile(value)
        return list(filter(lambda d: prog.search(d), file))
    return []
