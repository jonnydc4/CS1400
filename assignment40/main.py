'''
Project Name:P4 Stock Exchange Data
Author: Jonathon Carr
Due Date:10/31/2020
Course: CS1400-007

I learned how to make a nested dictionary and also how to print more effectively using a loop.
'''
def print_and_write(filePointer, string_to_write):
    print(string_to_write)
    filePointer.write(f'{string_to_write}\n')

def stock_summary(filenameToRead, filenameToWrite):

    try:
        input_file = open(filenameToRead, 'r')
    except:
        print("File does not exist")
        exit(1)
    lineCounter = 0
    max_price = 0
    min_price = 1000000
    all_stocks = {}
    for line in input_file:
        lineCounter += 1
        (stock, date, strPrice) = line.split(',')
        if lineCounter > 1:
            if not stock in all_stocks:
                all_stocks[stock] = {
                    "max_price": 0,
                    "min_price": 99999999,
                    "sum": 0,
                    "count": 0
                }
            price = float(strPrice)

            # compute overall max price
            if price > max_price:
                max_price = price
                max_stock = {
                    "stock": stock,
                    "date": date,
                    "price": price
                }

            # compute overall min price
            if price < min_price:
                min_price = price
                min_stock = {
                    "stock": stock,
                    "date": date,
                    "price": price
                }

            # compute max and min for this one stock
            if all_stocks[stock]["max_price"] < price:
                all_stocks[stock]["max_price"] = price
                all_stocks[stock]["max_price_date"] = date

            if all_stocks[stock]["min_price"] > price:
                all_stocks[stock]["min_price"] = price
                all_stocks[stock]["min_price_date"] = date

            all_stocks[stock]["count"] += 1
            all_stocks[stock]["sum"] += price


    # close input file
    input_file.close()

    # print all the results and write to a file
    write_file = open(filenameToWrite, 'w')
    for stock_name in all_stocks:
        print_and_write(write_file, stock_name)
        print_and_write(write_file, '----')
        print_and_write(write_file, f'Max: {all_stocks[stock_name]["max_price"]} {all_stocks[stock_name]["max_price_date"]}')
        print_and_write(write_file, f'Min: {all_stocks[stock_name]["min_price"]} {all_stocks[stock_name]["min_price_date"]}')
        print_and_write(write_file, f'Ave: {all_stocks[stock_name]["sum"] / all_stocks[stock_name]["count"]}')
        print_and_write(write_file, '')
    print_and_write(write_file, f'Highest: {max_stock["stock"]} {max_stock["price"]} {max_stock["date"]}')
    print_and_write(write_file, f'Lowest: {min_stock["stock"]} {min_stock["price"]} {min_stock["date"]}')
    write_file.close()

stock_summary('stocks_data.csv', 'stock_summary.txt')