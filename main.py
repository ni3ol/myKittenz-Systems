import numpy

def process_line(line):
    items = line.split()
    operation = items.pop(0)
    values = [int(x) for x in items]
    if operation == 'MIN':
        result = min(values)
    if operation == 'MAX':
        result = max(values)
    if operation == 'SUM':
        result = 0
        for i in values:
            result += i
    if operation == 'P90':
        result = numpy.percentile(numpy.array(values), 90)
    return str(result) + '\n'

def main():
    input = open('input.txt','r')
    output = open('output.txt', 'w')
    for line in input:
        result = process_line(line)
        output.write(result)
    input.close()
    output.close()
    print('File output saved in output.txt')

if __name__ == '__main__':
    main()
