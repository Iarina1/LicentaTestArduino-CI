with open('first_output.txt') as f:
    if 'error' in f.read():
        print("true")
