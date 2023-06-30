import random
import string


class RandomUtils:

    @staticmethod
    def get_random_text(length):
        letters = string.ascii_lowercase
        text = ''.join(random.choice(letters) for i in range(length))
        return text