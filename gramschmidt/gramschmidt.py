from numpy import linalg as la
import numpy as np
def gramSchmidt(vectors):
    new_vectors = []
    new_vectors.append(vectors[0]/la.norm(vectors[0]))
    for i in range(1, len(vectors)):
        p = 0
        for j in range(0, i):
            p = p + np.dot(vectors[i], new_vectors[j]) * new_vectors[j]
        r = vectors[i] - p
        new_vectors.append(r/la.norm(r))
    return new_vectors

vectors = [(1,1,0), (2,2,3)]
gramSchmidt(vectors)
