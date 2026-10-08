import math
import random
import platform


random_number = random.randint(1, 100)

square_root = math.sqrt(random_number)

floored_square_root = math.floor(square_root)

operating_system = platform.system()

python_version = platform.python_version()


print("Random Number: " + str(random_number))
print("Square Root (floored): " + str(floored_square_root))
print("Operating System: " + operating_system)
print("Python Version: " + python_version)