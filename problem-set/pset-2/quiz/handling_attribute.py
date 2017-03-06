def get_authors(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
                "fnm": None,
                "snm": None,
                "email": None,
                "insr": []
        }

        # YOUR CODE HERE
        data['snm'] = author.find('snm').text
        data['fnm'] = author.find('fnm').text
        data['email'] = author.find('email').text
        data['insr'] = [ it for o in author.findall('insr') for (id,it) in o.items()]

        authors.append(data)

    return authors

