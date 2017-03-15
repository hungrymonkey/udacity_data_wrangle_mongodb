def insert_autos(infile, db):
    data = process_file(infile)
    # Add your code here. Insert the data in one command.
    db.autos.insert(data)
