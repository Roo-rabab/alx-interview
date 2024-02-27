#!/usr/bin/python3
'''Module for log parsing script.
Write a script that reads stdin line by line and computes metrics:
-Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
 <status code> <file size> (if the format is not this one,
 the line must be skipped)
-After every 10 lines and/or a keyboard interruption (CTRL + C),
 print these statistics from the beginning:
    ->Total file size: File size: <total size>
    ->where <total size> is the sum of all previous <file size>
      (see input format above)
    ->Number of lines by status code:
      -possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
      -if a status code doesn’t appear or is not an integer,
       don’t print anything for this status code
      -format: <status code>: <number>
      -status codes should be printed in ascending order
'''

import sys

if __name__ == "__main__":
    size = [0]
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    def check_match(line):
        '''Checks for regexp match in line.'''
        try:
            line = line[:-1]
            words = line.split(" ")
            size[0] += int(words[-1])
            code = int(words[-2])
            if code in codes:
                codes[code] += 1
        except:
            pass

    def print_stats():
        '''Prints accumulated statistics.'''
        print("File size: {}".format(size[0]))
        for k in sorted(codes.keys()):
            if codes[k]:
                print("{}: {}".format(k, codes[k]))
    i = 1
    try:
        for line in sys.stdin:
            check_match(line)
            if i % 10 == 0:
                print_stats()
            i += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
