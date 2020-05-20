
def main():
    # Incase you have to take input, please take it from file named 'input' (without quotes) [e.g. cat input]
    # Print your final output to console. Do not redirect to another file.
    # E.g. Suppose the question is to print the content of a file.
    #	Your solution should be 'os.system("cat input")'(without single quotes) instead of 'os.system("cat input > output")'. That's it!
    # Your code starts from here...
    
    d = {}
    fh= open('input', 'r')
    lines = fh.readlines()
    for line in lines:
        strings = line.split()
        for string in strings:
            val = d.get(string, 0)
            d[string] = val + 1
        
    
    d = sorted(d.items() , key=lambda t : t[1] , reverse=True)

    
    for k,v in d:
        print(k,v)
    return 0

if __name__ == '__main__':
    main()

