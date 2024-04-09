import time

def add_time_to_file(file_name):
    with open(file_name, 'w') as f:
        f.write(time.ctime() + "\n")

add_time_to_file('example.txt')
