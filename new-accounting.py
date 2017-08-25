def count_melon_sales(file_name):
    melon_sales = {
        'Musk': 0,
        'Hybrid': 0,
        'Winter': 0,
        'Watermelon': 0
    }

    with open(file_name) as melon_sales_data:
        for line in melon_sales_data:
            line = line.strip().split('|')
            if line[1] == 'Musk':
                melon_sales['Musk'] += int(line[2])
            elif line[1] == 'Hybrid':
                melon_sales['Hybrid'] += int(line[2])
            elif line[1] == 'Winter':
                melon_sales['Winter'] += int(line[2])
            elif line[1] == 'Watermelon':
                melon_sales['Watermelon'] += int(line[2])

    return melon_sales


def calculate_melon_revenue(melon_sales):
    melon_prices = {
        'Musk': 1.15,
        'Hybrid': 1.30,
        'Winter': 4.00,
        'Watermelon': 1.75
    }

    melon_revenue = {}
    total_revenue = 0

    for key in melon_sales:
        melon_revenue[key] = melon_prices[key] * melon_sales[key]

    for melon in melon_revenue:
        print 'We sold {} {} melons for ${:.2f} each for a total of ${:.2f}.'.format(melon_sales[melon], melon, melon_prices[melon], melon_revenue[melon])
        total_revenue += melon_revenue[melon]

    return total_revenue


def separate_sales_by_type(file_name):
    online_sales = 0
    phone_sales = 0

    with open(file_name) as sales_data:
        for line in sales_data:
            line = line.strip().split('|')
            if line[2] == 'ONLINE':
                online_sales += float(line[3])
            else:
                phone_sales += float(line[3])

    print 'Online sales generated ${:.2f} in revenue'.format(online_sales)
    print 'Salespeople generated ${:.2f} in revenue.'.format(phone_sales)


total = calculate_melon_revenue(count_melon_sales('orders-by-type.txt'))
print
print 'We sold ${:.2f} in total revenue.'.format(total)
print
separate_sales_by_type('orders-with-sales.txt')
