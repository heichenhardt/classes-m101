#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Henrik
#
# Created:     31.10.2012
# Copyright:   (c) Henrik 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pymongo
import os

def main():

    connection = pymongo.Connection('mongodb://localhost', safe=True)
    db = connection.students
    cursor = db.grades.find({'type': 'homework'}).sort(
                [['student_id', pymongo.ASCENDING], ['score', pymongo.ASCENDING]])
    student_id = -1
    for element in cursor:
        if student_id != element['student_id']:
            student_id = element['student_id']
            db.grades.remove({'_id': element['_id']})
            #print ('R ' + student_id + ' grade: '+ element['score'])

if __name__ == '__main__':
    main()
