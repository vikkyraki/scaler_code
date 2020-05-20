import csv

def main():
    with open('input') as input:
        reader = csv.reader(input, delimiter=',')
        for item in reader:
            item[6] = '+' + item[4] + '-' + item[6]
            del item[4]
            x = ",".join(item)
            print(x)
        
    input.close()
    return 0

if __name__ == '__main__':
    main()

