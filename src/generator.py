def even_odd_generator(limit=None):
    count = 0
    while limit is None or count < limit:
        yield "Even" if count % 2 == 0 else "Odd"
        count += 1