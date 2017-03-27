def process_file(filename, fields):

    process_fields = fields.keys()
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for i in range(3):
            l = reader.next()

        for line in reader:
            # YOUR CODE HERE
            ele = {}
            for k in FIELDS:
                if k == 'rdf-schema#label':
                    ele[FIELDS[k]] = line[k].replace("(spider)","").strip()
                elif k == 'name':
                    if line[k] == 'NULL' or not line[k].isalnum():
                        ele[FIELDS[k]] = ele[FIELDS['rdf-schema#label']]
                    else:
                        ele[FIELDS[k]] = line[k].strip()
                elif line[k] == 'NULL':
                    ele[FIELDS[k]] = None
                elif k ==  'synonym':
                    ele[FIELDS[k]] = line[k].strip("{} \r\t\n").split("|")
                else:
                    ele[FIELDS[k]] = line[k].strip()
            o = {}
            for k in ['label','uri', 'description', 'synonym', 'name']:
                o[k] = ele[k]
                des = {}
                for d in ['family','class','phylum','order','kingdom','genus']:
                    des[d] = ele[d]
                o['classification'] = des
            data.append(o)
    return data
