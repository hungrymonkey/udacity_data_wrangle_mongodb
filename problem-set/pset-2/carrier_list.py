def extract_carriers(page):
    data = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        r = soup.find('select', class_='slcBox', id='CarrierList')
        for t in r.findChildren():
            if len( t['value'] ) == 2:
                data.append(t['value'])
    return data
