def article_overview(kind, period):
    data = get_from_file(kind, period)
    titles = []
    urls =[]
    # YOUR CODE HERE
    
    for art in data:
        titles.append({art['section']:art['title']})
        #urls.append(art["url"])
        for med in art["media"]:
            for m in med["media-metadata"]:
                if m["format"] == "Standard Thumbnail":
                    urls.append(m["url"])
        #print len(urls)
    return (titles, urls)

