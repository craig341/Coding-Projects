class HealthBar:
    symbol_remaining = '█'
    symbol_left = '_'
    symbol_barrier = '|'

    def __init__(self, entity, length=20):
        self.entity = entity
        self.length = length
        self.max_health = entity.max_health
        self.current_health = entity.health

    def update(self):
        self.current_health = self.entity.health


    def draw(self):
        remaining_bars = round(self.current_health / self.max_health * self.length)
        lost_bars = self.length - remaining_bars
        print(f'{self.entity.name} HEALTH: {self.entity.health}/{self.entity.max_health}')
        print(f'{self.symbol_barrier}'
              f'{remaining_bars * self.symbol_remaining}'
              f'{lost_bars * self.symbol_left}'
              f'{self.symbol_barrier}')

