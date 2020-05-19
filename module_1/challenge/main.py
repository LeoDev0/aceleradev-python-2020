from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666',
     'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097',
     'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097',
     'end': 1564630198, 'start': 1564629838},
    {'source': '41-833333333', 'destination': '41-885633788',
     'end': 1564707276, 'start': 1564704317},
    {'source': '48-999999999', 'destination': '41-885633788',
     'end': 1564697158, 'start': 1564696258},
    {'source': '41-886383097', 'destination': '48-996384099',
     'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697',
     'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099',
     'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697',
     'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097',
     'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788',
     'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788',
     'end': 1564627800, 'start': 1564626000}
]

PERMANENT_FEE = 0.36
MINUTE_FEE = 0.09


def classify_by_phone_number(records):
    final_bill = []
    for record in records:
        call_initial_hour = int(datetime.fromtimestamp(record['start'])
                                        .strftime('%H'))
        total_minutes = (record['end'] - record['start']) // 60
        total_bill = PERMANENT_FEE
        if 6 <= call_initial_hour <= 22:
            total_bill += (total_minutes * MINUTE_FEE)

        repeated_source = False
        for bill in final_bill:
            if record['source'] == bill['source']:
                repeated_source = True
                bill['total'] += total_bill
                break

        if not repeated_source:
            final_bill.append({'source': record['source'],
                               'total': round(total_bill, 2)})

    # Ordering the list by total value and storing inside the same variable
    # to overwrite the previous list and save memory.
    final_bill = sorted(final_bill, key=lambda bill: bill['total'], reverse=True)
    return final_bill
