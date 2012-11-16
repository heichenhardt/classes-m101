import pymongo

def index():
    from pymongo import Connection
    connection = Connection('mongodb://localhost', safe=True)

    db = connection.test
    index = 0
    while (index<100000):
        id = db.counters.find_and_modify(
                            query = {'type': 'user'},
                            update = {'$inc': {'value': 1}},
                            upsert = True,
                            new = True)

        index = index + 1
        print id['value']



index()

