#Requirements
#Task 1: read the data from the spreadsheet

import csv

with open('sales.csv', 'r') as sales_csv:
    contents = sales_csv.read()

    print(contents)

#Task 2: Collect all of the sales from each month into a single list

    def read_data():
        data = []

        with open('sales.csv', 'r') as sales_csv:
            spreadsheet = csv.DictReader(sales_csv)

            for row in spreadsheet:
                data.append(row)

            return data

    def run():
        data = read_data()

        sales = []
        values = []

        for row in data:
            sale = int(row['sales'])
            sales.append(sale)

            values.append({'month': row['month'], 'value': sale})

        print("Sales: ", sales)

#Task 3: Output the total sales across all months

        total = sum(sales)
        print('Total sales across all months: ', total)



#Extensions
#Task 4: Output summary of results to a spreadsheet

        with open('output.csv', 'w+') as output_csv:
            writer = csv.writer(output_csv)

            writer.writerow(['Total sales across all months', total])

#Task 5: calculate average, months with highest and lowest sales

        average = int(total/len(sales))
        print('Average: ', average)

        highest_sale = max(values, key=lambda k: k['value'])
        print('Highest sale: ', str(highest_sale))

        lowest_sale = min(values, key=lambda k: k['value'])
        print('Lowest sale: ', str(lowest_sale))

#Task 6: Calculate monthly changes as a percentage
        import pandas as pd

        series = pd.Series(sales)
        result = series.pct_change()
        print('Percent change: ', result)


run()


#Task 7: Graphing

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('/Users/Frem/PycharmProjects/pythonProject/venv/sales.csv')
df = pd.DataFrame(data)

X = list(df.iloc[:, 1])
Y = list(df.iloc[:, 2])

X1 = list(df.iloc[:, 1])
Y2 = list(df.iloc[:, 3])

plt.plot(X, Y, color='g', label='Sales')
plt.xlabel("Month")
plt.ylabel("Currency")

plt.plot(X1, Y2, color='r', label='Expenditure')
plt.xlabel("Month")
plt.ylabel("Currency")

plt.legend()
plt.grid()
plt.show()


