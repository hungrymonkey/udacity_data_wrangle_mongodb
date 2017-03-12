def split_file(filename):
    """
    Split the input file into separate files, each containing a single patent.
    As a hint - each patent declaration starts with the same line that was
    causing the error found in the previous exercises.
    
    The new files should be saved with filename in the following format:
    "{}-{}".format(filename, n) where n is a counter, starting from 0.
    """
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
		wf.write(line)
        wf.close()
        rf.close()

