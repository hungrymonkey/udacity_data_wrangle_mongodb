def dot_query():
    # Edit the line below with your query - try to use dot notation.
    # You can check out example_auto.txt for an example of the document
    # structure in the collection.
    query = {"dimensions.width":{"$gt":2.5}}
    return query
