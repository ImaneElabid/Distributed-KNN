import math


def distance(profil1, profil2):
    """
    Euclidean distance
    """
    if len(profil1) == len(profil2):
        total = 0.0
        tmp = 0.0
        for i in range(len(profil1)):
            tmp = (profil1[i] - profil2[i]) ** 2
            total = total + tmp
        return math.sqrt(total)
    else:
        raise ValueError('Euclidean similarity need vectors of the same size.')
