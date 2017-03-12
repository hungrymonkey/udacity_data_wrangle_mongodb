def process_file(f):
    """
    This function extracts data from the file given as the function argument in
    a list of dictionaries. This is example of the data structure you should
    return:

    data = [{"courier": "FL",
             "airport": "ATL",
             "year": 2012,
             "month": 12,
             "flights": {"domestic": 100,
                         "international": 100}
            },
            {"courier": "..."}
    ]


    Note - year, month, and the flight data should be integers.
    You should skip the rows that contain the TOTAL data for a year.
    """
    data = []
    info = {}
    info["courier"], info["airport"] = f[:6].split("-")
    # Note: create a new dictionary for each entry in the output data list.
    # If you use the info dictionary defined here each element in the list 
    # will be a reference to the same info dictionary.
    with open("{}/{}".format(datadir, f), "r") as html:

        soup = BeautifulSoup(html)
        result = soup.find('table',class_='dataTDRight')
        for r in result.find_all('tr', class_='dataTDRight'):
            cols = r.find_all('td')
            i = info
            if cols[1].text != 'TOTAL':
                i["year"] = int(cols[0].text)
                i["month"] = int(cols[1].text)
                i["flights"] = {"domestic":  int(cols[2].text.replace(',', '')),
                                     "international":  int(cols[3].text.replace(',', ''))}
                data.append(i)
    return data
