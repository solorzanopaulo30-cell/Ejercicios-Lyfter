
sales = [
	{
		'date': '15/03/24',
		'customer_email': 'laura@gmail.com',
		'items': [
			{
				'name': 'Mochila',
				'upc': 'ITEM-101',
				'unit_price': 45.90,
			},
			{
				'name': 'Auriculares',
				'upc': 'ITEM-205',
				'unit_price': 89.99,
			},
			{
				'name': 'Termo',
				'upc': 'ITEM-310',
				'unit_price': 21.30,
			},
		],
	},
	{
		'date': '15/03/24',
		'customer_email': 'carlos@gmail.com',
		'items': [
			{
				'name': 'Mochila',
				'upc': 'ITEM-101',
				'unit_price': 45.90,
			},
			{
				'name': 'Mouse',
				'upc': 'ITEM-88',
				'unit_price': 15.75,
			},
		],
	},
	{
		'date': '14/03/24',
		'customer_email': 'sofia@gmail.com',
		'items': [
			{
				'name': 'Mouse',
				'upc': 'ITEM-88',
				'unit_price': 14.20,
			},
			{
				'name': 'Termo',
				'upc': 'ITEM-310',
				'unit_price': 19.90,
			},
		],
	},
]


result = {}

for sale in sales:
    for item in sale['items']:
        upc = item['upc']
        price = item['unit_price']

        if upc in result:
            result[upc] += price
        else:
            result[upc] = price

print(result)
        