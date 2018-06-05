class MoneyDataParser:
    def __init__(self, filename):
        self.diary = {}
        self.filename = filename

    def parse_data(self):
        with open(self.filename) as data_file:
            last_seen = ''
            for row in data_file.readlines():
                if '===' in row:
                    last_seen = row[:-1]
                    self.diary[last_seen] = []
                else:
                    self.diary[last_seen].append(row[:-1])
        return self.diary

