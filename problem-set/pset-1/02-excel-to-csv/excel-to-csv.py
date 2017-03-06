def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    tempd = []
    for row in range(sheet.nrows):
        values = []
        for col in range(sheet.ncols):
            values.append(sheet.cell(row,col).value)
        tempd.append(values)
    # YOUR CODE HERE
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)
    #print tempd[1:][:]
    header = ['Station','Year','Month','Day','Hour','Max Load']
    data = []
    data.append(header)
    for col in range(1,len(tempd[0])-1):
        max_s = max([ (row[0],row[col]) for row in tempd[1:][:]],key=lambda x: x[1])
        time, load = max_s
        (year, month, day, hour, minute, second) = xlrd.xldate_as_tuple(time,0)
        data.append([tempd[0][col],year,month,day,hour,load])
    return data

def save_file(data, filename):
    # YOUR CODE HERE
    f = open(filename, 'w')

    for row in data:
        o = [str(i) for i in row]
        f.write("|".join(o)+"\n")

