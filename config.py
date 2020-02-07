import yaml

def get_api_key(vendor=None):

	try:
		with open('test_api_keys.yml') as file:
		    config = yaml.load(file, Loader=yaml.BaseLoader)

		if vendor in config.keys():
			api_key = config[vendor]
		else:
			api_key = 'your_api_key'
	except FileNotFoundError:
		api_key = 'your_api_key'

	return api_key
