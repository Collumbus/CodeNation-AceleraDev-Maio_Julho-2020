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
    XXIIH = 1320                                                                    # 22 hours in minutes
    VIH = 360                                                                       # 6 hours in minutes
    billed_sources = {}                                                             # dic. to store calculated bills

    for record in records:
        start = datetime.fromtimestamp(record['start'])                             # call start
        s_min = ((start.hour * 60 + start.minute) * 60 + start.second) // 60        # call start in minutes
        end = datetime.fromtimestamp(record['end'])                                 # call end
        minutes = (end - start).seconds // 60                                       # call duration in minutes
        tax = 0.0                                                                   # cost calculator var

        for minute in range(minutes):                                               # check what tax the minute fits

            if VIH < (minute + s_min) < XXIIH:                                      # day tax
                tax += MINUTE_TAX

        tax += CONNECTION_TAX                                                       # adds the connection tax
        billed_sources[record['source']] = round(billed_sources.setdefault(record['source'], 0) + tax, 2)

    report = [{'source': record, 'total': billed_sources[record]} for record in billed_sources]
    return sorted(report, key=lambda x: x['total'], reverse=True)


if __name__ == "__main__":

    print(classify_by_phone_number(records))
