from engine.image import Image
from engine.environment import Environment

import random
def random_id():
	return ''.join(random.choice("0123456789abcdef") for x in range(32))