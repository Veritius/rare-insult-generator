import random, time

adjaa = [
	'uneducated',
	'uncultured',
	'decomposing',
	'insignificant',
	'uninteresting',
	'irregular',
	'undeserving',
	'undercooked',
	'lobotomised',
	'dehydrated',
	'incompetent',
	'pathetic',
	'dense',
	]

adjab = [
	'deformed'
	'three-cheese-high',
	'train-station-loving',
	'soggy-couch-cushion-loving',
	'breadcrumb-snorting',
	'sugar-huffing',
	'snail-powered',
	'cat-licking',
	'dog-kicking',
	'plunger-sucking',
	'microwave-slapping',
	'cabbage-headed',
	'spine-liquifying',
	'paper-brained',
	'NPC-kicking',
	'dim-witted',
	'potion-overdosing',
	'light-mode-using',
	'google-plus-using',
	'calcium-deficient',
	'chair-throwing',
	'lightbulb-breaking',
	'snowflake-slapping',
	]

nameaa = [
	'idiot',
	'waffle',
	'imbecile',
	'moron',
	'stick of unsalted butter',
	'troglodyte',
	'golem',
	'trapezoid',
	'parachute',
	'peasant',
	'millenial',
	'fool',
	'oaf',
	'nincompoop',
	'helicopter',
	'dunce',
	'simpleton',
	'park bench',
	'halfwit',
	'blender',
	'numbskull',
	'fedora',
	'hamster',
	'puppy',
	'table',
	'invertebrate',
	'coffee cup',
	'bag of wheat'
	'crustacean',
	'giraffe',
	'omelette',
	'scoundrel',
	]


while True:
	adjba = random.choice(adjaa)
	adjbb = random.choice(adjab)
	nameba = random.choice(nameaa)
	print(f'{adjba} {adjbb} {nameba}')
	time.sleep(1)
