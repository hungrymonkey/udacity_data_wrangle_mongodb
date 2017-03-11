def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        #print soup
        r = soup.find('select',id='AirportList')
        for a in r.findChildren():
            if len( a['value'] ) == 3 and a['value'] != 'All':
                data.append(a['value'])
        #print r
    return data
