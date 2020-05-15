from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]


def classify_by_phone_number(records):
    CONNECTION_TAX = 0.36
    MINUTE_TAX = 0.09
    billed_sources = {}

    for record in records:
        start = datetime.fromtimestamp(record['start'])
        end = datetime.fromtimestamp(record['end'])

        # day charge rate
        if (start.hour >= 6 and end.hour < 22):
            tax = CONNECTION_TAX + (((end - start).seconds // 60) * MINUTE_TAX)

        # night charge rate
        elif (start.hour >= 22 and end.hour >= 6) or (start.hour < 6 and end.hour < 6):
            tax = CONNECTION_TAX

        # mix charge rate
        elif (start.hour >= 6 and start.hour < 22) and (end.hour >= 22 and end.hour < 6):
            limit_s = datetime.fromisoformat(datetime.strftime(start.date(), "%Y-%m-%d") + "T22:00:00")
            tax = CONNECTION_TAX + (((limit_s - start.hour).seconds // 60) * MINUTE_TAX)

        elif (start.hour >= 22 and start.hour < 6) and (end.hour >= 6 and end.hour < 22):
            limit_i = datetime.fromisoformat(datetime.strftime(start.date(), "%Y-%m-%d") + "T06:00:00")
            tax = CONNECTION_TAX + (((limit_i - end.hour).seconds // 60) * MINUTE_TAX)

        billed_sources[record['source']] = round(billed_sources.setdefault(record['source'], 0) + tax, 2)

    report = [{'source': record, 'total': billed_sources[record]} for record in billed_sources]
    return sorted(report, key=lambda x: x['total'], reverse=True)


if __name__ == "__main__":

    print(classify_by_phone_number(records))
