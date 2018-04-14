import random


class StatisticMaker:
    def __init__(self, filename):
        self.filename = filename

        self.json = {
            "day": {
                "under18":      [],
                "middleAge":    [],
                "culmination":  [],
                "elder":        [],
                "total":        []
            }
        }

        self.months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def fill(self):
        for month in range(12):
            for day in range(self.months[month]):
                under18Day = []
                middleAgeDay = []
                culminationDay = []
                elderDay = []
                totalDay = []

                for hour in range(24):
                    under18 = random.randint(1, 50)
                    middleAge = random.randint(1, 50)
                    culmination = random.randint(1, 50)
                    elder = random.randint(1, 50)
                    total = under18 + middleAge + culmination + elder

                    under18Day.append(under18)
                    middleAgeDay.append(middleAge)
                    culminationDay.append(culmination)
                    elderDay.append(elder)
                    totalDay.append(total)

                # тут мы закончили добавлять только один день - 24 часа

                self.json['day']['under18'].append(under18Day)
                self.json['day']['middleAge'].append(middleAgeDay)
                self.json['day']['culmination'].append(culminationDay)
                self.json['day']['elder'].append(elderDay)
                self.json['day']['total'].append(totalDay)

    def dump(self):
        import json

        with open(self.filename, 'w') as file:
            json.dump(self.json, file)


male = StatisticMaker('male.json')
male.fill()
male.dump()

female = StatisticMaker('female.json')
female.fill()
female.dump()
