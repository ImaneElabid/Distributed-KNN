def similarity(p1, p2, similarity_type=1):
    if similarity_type == 1:
        from .euclidean import distance
        return distance(p1, p2)
    elif similarity_type == 2:
        from .cosine import distance
        return distance(p1, p2)
    else:
        raise ValueError("This similarity is not defined.")
