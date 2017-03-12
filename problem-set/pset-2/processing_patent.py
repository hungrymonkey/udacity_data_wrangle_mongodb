    with open(filename, 'r') as rf:
        n = 0
        wf = open("{}-{}".format(filename, n), 'w')
        wf.write(rf.next())
        for line in rf:
            if line.find('<?xml version="1.0" encoding="UTF-8"?>') == -1:
                wf.write(line)
            else:
                wf.close()
                n = n+1
                wf = open("{}-{}".format(filename, n), 'w')
        wf.close()
        rf.close()
