from rep.image import Image
from rep.environment import Environment
import os

import random
def random_id():
	return ''.join(random.choice("0123456789abcdef") for x in range(32))

TMP_DIR = os.path.join(os.environ["HOME"], ".rep")

SSH_PROXY = ["ssh", "-o", "StrictHostKeyChecking=no", "-p", "2022", "-A", "-t", "docker@localhost"]