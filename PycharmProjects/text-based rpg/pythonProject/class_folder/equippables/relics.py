from pythonProject.classes import Relic

none = Relic(name='None', rarity='default')

max_crit = Relic(name='Always Crit', rarity='developer', crit_chance=9999)
developer_pass = Relic(name='Developer Pass', rarity='developer', strength=1000)

relic_dict = {obj.name: obj for obj in globals().values() if isinstance(obj, Relic)}
