import math


def distance(profil1, profil2):
    """
    Cosine distance
    """
    if len(profil1) == len(profil2):

        pscalaire = 0.0
        normp1 = 0.0
        normp2 = 0.0
        for i in range(len(profil1)):
            pscalaire += profil1 * profil2
            normp1 += profil1 ** 2
            normp2 += profil2 ** 2
            normp1 += math.sqrt(normp1)
            normp2 += math.sqrt(normp2)

        return math.sqrt(pscalaire / (normp1 * normp2))
    else:
        raise ValueError('Cosine similarity need vectors of the same size.')
