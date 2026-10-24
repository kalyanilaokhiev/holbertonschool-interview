#!/usr/bin/python3

import sys

if __name__ == "__main__":
    total_size = 0
    line_count = 0
    # status code and count
    status_code = {"200": 0,
                   "301": 0,
                   "400": 0,
                   "401": 0,
                   "403": 0,
                   "404": 0,
                   "405": 0,
                   "500": 0}

    # looking through the input format
    try:
        for line in sys.stdin:
            # split the line
            parts = line.split()

            # checking if the input has at least both parts
            if len(parts) >= 2:
                file_size = parts[-1]
                code = parts[-2]
                    
                try: 
                    # convert file size to int
                    file_size = int(file_size)
                    total_size += file_size # add to total_size
        
                    # check if the status code is valid in dict
                    if code in status_code:
                        status_code[code] += 1
        
                    # count for the 10 lines
                    line_count += 1
        
                # if not int or valid status, dont print anything
                except (ValueError, IndexError):
                    continue

                # check if reached 10 lines
                if line_count == 10:
                    print("File size: {}".format(total_size))

                    # printing status code in ascending order
                    for i in sorted(status_code.keys()):
                        if status_code[i] > 0:
                            print("{}: {}".format(i, status_code[i]))

                # resart count
                line_count = 0

    # Check if there is a keyboard interrupt
    except KeyboardInterrupt: 
        print("File size: {}".format(total_size))
        
        for i in sorted(status_code.keys()):
            if status_code[i] > 0:
                print("{}: {}".format(i, status_code[i]))

        # end the code with keyboard interrupt after printing
        raise