
def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [{"$match": {"user.time_zone" : "Brasilia" ,"user.statuses_count" : {"$gte": 100}} },
            {"$project" : {"followers" : "$user.followers_count", "screen_name" : "$user.screen_name","tweets" : "$user.statuses_count"}},
            {"$sort" : {"followers" : -1}},
            {"$limit" : 1}]
    return pipeline
