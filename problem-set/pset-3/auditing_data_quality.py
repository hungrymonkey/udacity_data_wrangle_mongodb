def is_float(f):
    try:
        float(f)
        return True
    except ValueError:
        return False
        
def is_int(f):
    try:
        int(f)
        return True
    except ValueError:
        return False
        
def audit_file(filename, fields):
    fieldtypes = {}

    # YOUR CODE HERE
    for f in FIELDS:
        fieldtypes[f] = set()
    with open(CITIES,'r') as fi:
        reader = csv.DictReader(fi)
        header = reader.fieldnames
        for row in reader:
            if 'dbpedia' in row['URI']:
                for f in FIELDS:
                    if  row[f] == "NULL" or row[f] == "":
                        fieldtypes[f].add(type(None))
                    elif row[f][0] == "{":
                        fieldtypes[f].add(type([]))
                    elif is_int(row[f]):
                        fieldtypes[f].add(type(2341))
                    elif is_float(row[f]):
                        fieldtypes[f].add(type(910231.1))
                    else:
                        fieldtypes[f].add(type(''))

    return fieldtypes
