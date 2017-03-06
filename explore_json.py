def get_artist_id(query, name, ty='Group'):
   for i,k in enumerate(query['artists']):
      if 'type' in k:
         if k['name'] == name and k["type"]==ty:
            return (k["id"],i)

def get_foreign_alias(aliases,locale='es'):
    for k in aliases:
       if k['locale'] == locale:
          return k

def get_band( query, name='First Aid Kit'):
    out = []
    for k in query:
      if k['name'] == name:
         out.append(k)
    return out

def answers():
    #Question1

    results = query_by_name(ARTIST_URL, query_type["simple"], "FIRST AID KIT")
    bands = get_band(results['artists'])
    pretty_print(len(bands))
    #Question2
    results = query_by_name(ARTIST_URL, query_type["simple"], "QUEEN")
    (queen_id, i) =  get_artist_id(results,'Queen')
    print(results['artists'][i]['begin-area']['name'])
    #Question3
    results = query_by_name(ARTIST_URL, query_type["simple"], "BEATLES")
    (beatle_id, i) =  get_artist_id(results,'The Beatles')
    pretty_print(get_foreign_alias(results['artists'][i]['aliases'])['name'])
    #Question4
    results = query_by_name(ARTIST_URL, query_type["simple"], "NIRVANA")
    bands = get_band(results['artists'], 'Nirvana')
    for k in bands:
       print(k['disambiguation'])
    (Nirvana_id, i) =  get_artist_id(results,'Nirvana')
    #pretty_print(results['artists'][i]['disambiguation'])
    #Question5
    results = query_by_name(ARTIST_URL, query_type["simple"], "ONE DIRECTION")
    (OneD_id, i) =  get_artist_id(results,'One Direction')
    pretty_print(results['artists'][i]['life-span']['begin'])

