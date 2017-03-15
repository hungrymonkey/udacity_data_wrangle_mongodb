def fix_name(name):

    # YOUR CODE HERE
    if name == "NULL":
        return []
    elif name[0] == '{':
        return name[1:-1].split('|')
    return [name]

