def get_authors(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
                "fnm": None,
                "snm": None,
                "email": None
        }

        # YOUR CODE HERE
        data['snm'] = author.find('snm').text
        data['fnm'] = author.find('fnm').text
        data['email'] = author.find('email').text
        authors.append(data)

    return authors
