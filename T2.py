def imprime(mat):
    for x in mat:
        print(x)
    print()

def valido(lab, res, f, c):
    if f >= len(lab):
        return False
    if f < 0:
        return False
    if c >= len(lab[0]):
        return False
    if c < 0:
        return False
    if res[f][c] == 1:
        return False
    if lab[f][c] == 0:
        return False
    return True

def laberB(lab, res, f, c, puntos):
    
    if f == 0 and c == 0:
        if valido(lab, res, f, c):
            res[f][c] = 1
            if puntos >= 23:
                print("Se llegó a la meta con", puntos, "puntos")
                imprime(res)
                return True
            else:
                res[f][c] = 0
                return False
        else:
            return False
    else:
        if valido(lab, res, f, c):
            if lab[f][c] == 3 or lab[f][c] == 4:
                puntos += lab[f][c]
                
            res[f][c] = 1
            print("puntos: ", puntos)
            imprime(res)

            if laberB(lab, res, f-1, c, puntos):
                return True
            elif laberB(lab, res, f, c+1, puntos):
                return True
            elif laberB(lab, res, f+1, c, puntos):
                return True
            elif laberB(lab, res, f, c-1, puntos):
                return True
            else:
                res[f][c] = 0
                return False
        else:
            return False

lab = [
    [1, 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    [1, 1, 3, 1, 0, 1, 1, 1, 1]
]

res = [[0 for _ in range(9)] for _ in range(9)]


if laberB(lab, res, 8, 0, 0):
    print("\n¡Salimos!")
else:
    print("\nQuedamos atrapados")