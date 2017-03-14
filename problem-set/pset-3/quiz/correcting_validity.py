def process_file(input_file, output_good, output_bad):
    
    year_range = [1886,2014]
    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames

        #COMPLETE THIS FUNCTION
        gf = open(output_good, "w")
        bf = open(output_bad, "w")
        g = csv.DictWriter(gf, delimiter=",", fieldnames= header)
        b = csv.DictWriter(bf, delimiter=",", fieldnames= header)
        g.writeheader()
        b.writeheader()
        for row in reader:
            if 'dbpedia.org' in row['URI']:
                if row['productionStartYear'][:4].isdigit():
                    row['productionStartYear'] = row['productionStartYear'][:4]
                    if year_range[1] - year_range[0] >= (int(row['productionStartYear']) - year_range[0]) & 0xffffffffffffffff:
                        g.writerow(row)
                    else:
                        b.writerow(row)
                else:
                    b.writerow(row)
        gf.close()
        bf.close()

