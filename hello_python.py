#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Henrik
#
# Created:     29.10.2012
# Copyright:   (c) Henrik 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print(readPropertyValue('build.properties', 'version'))

def readPropertyValue(properties, key):
    try:
        f = open(properties)
        dictionary = {}
        for line in f.readlines():
            keyValue = line.split('=')
            if len(keyValue) == 2:
                dictionary[keyValue[0]] = keyValue[1]

        if key in dictionary:
            return dictionary[key]
        else:
            return None
    except IOError:
        print 'Can\'t open file'

if __name__ == '__main__':
    main()