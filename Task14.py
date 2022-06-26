class Flover:
    name = None

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def info(self):
        print(f'{self.name} {self.color} i пахне')



peony = Flover('Піон', 'рожевий')
chamomile = Flover('Ромашка', 'біла')
peony.info()
chamomile.info()
