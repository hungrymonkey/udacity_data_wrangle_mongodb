def fix_area(area):

    # YOUR CODE HERE
    if area[0] == '{':
        r = area[1:-1].split('|')
        area = max( r, key=lambda x: len(x))
    try:
        return float(area)
    except:
        return None
    return area
