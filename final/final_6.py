#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Henrik
#
# Created:     16/12/2012
# Copyright:   (c) Henrik 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pymongo

def main():
    connection = pymongo.MongoClient(
            host=["mongodb://localhost:27017"],
            w="1", j=False)

    db = connection.photo

    albums = db.albums.aggregate([{'$project': {'image': '$images'}}, {'$unwind': '$image'}, {'$group': {'_id': 'null', 'images': {'$addToSet': '$image'}}}])
    referenced_images_result = albums['result'][0]
    ref_images = referenced_images_result['images']

    print "Images referenced: ", len(ref_images)

    images =  db.images.aggregate([{'$group': {'_id': 'null', 'images': {'$addToSet': '$_id'}}}])
    all_images_result = images['result'][0]
    all_images = all_images_result['images']

    print "All Images: ", len(all_images)


    remove_images = set(all_images) - set(ref_images)

    for image in remove_images:
        print "Remove ",image
        db.images.remove({'_id': image})

    print db.images.count()

if __name__ == '__main__':
    main()
