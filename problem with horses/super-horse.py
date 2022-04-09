''' ---------------------------------------------------------------------------------------------------------------------------------------------------
    ------------------------------------------------The project was made by Dmitry Zolotukhin----------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------'''

matrix = [
    ["#", "#", "#", "#"],
    ["#", "#", "#", "#"],
    ["#", "#", "#", "#"],
    ["Y", "#", "#", "#"]
]
complete_matrix = []


# ------------------------------------------------ Knight moves -------------------------------------------------------------------------

def is_RU(x1, y1, is_dead):
    if ((x1 + 2) < len(matrix[y1])) and (y1 + 1) < len(matrix) and is_dead:
        matrix[y1 + 1][x1 + 2] = "X"
        return True
    if ((x1 + 2) < len(matrix[y1])) and (y1 + 1) < len(matrix) and is_dead == False:
        matrix[y1 + 1][x1 + 2] = "Y"
        return True


def is_UR(x1, y1, is_dead):
    if ((x1 + 1) < len(matrix[y1])) and (y1 + 2) < len(matrix) and is_dead:
        matrix[y1 + 2][x1 + 1] = "X"
        return True
    if ((x1 + 1) < len(matrix[y1])) and (y1 + 2) < len(matrix) and is_dead == False:
        matrix[y1 + 2][x1 + 1] = "Y"
        return True


def is_LD(x1, y1, is_dead):
    if ((x1 - 2) >= 0) and (y1 - 1) >= 0 and is_dead:
        matrix[y1 - 1][x1 - 2] = "X"
        return True
    if ((x1 - 2) >= 0) and (y1 - 1) >= 0 and is_dead == False:
        matrix[y1 - 1][x1 - 2] = "Y"
        return True


def is_DL(x1, y1, is_dead):
    if ((x1 - 1) >= 0) and (y1 - 2) >= 0 and is_dead:
        matrix[y1 - 2][x1 - 1] = "X"
        return True
    if ((x1 - 1) >= 0) and (y1 - 2) >= 0 and is_dead == False:
        matrix[y1 - 2][x1 - 1] = "Y"
        return True


def is_LU(x1, y1, is_dead):
    if ((x1 - 2) >= 0) and (y1 + 1) < len(matrix) and is_dead:
        matrix[y1 + 1][x1 - 2] = "X"
        return True
    if ((x1 - 2) >= 0) and (y1 + 1) < len(matrix) and is_dead == False:
        matrix[y1 + 1][x1 - 2] = "Y"
        return True


def is_UL(x1, y1, is_dead):
    if ((x1 - 1) >= 0) and (y1 + 2) < len(matrix) and is_dead:
        matrix[y1 + 2][x1 - 1] = "X"
        return True
    if ((x1 - 1) >= 0) and (y1 + 2) < len(matrix) and is_dead == False:
        matrix[y1 + 2][x1 - 1] = "Y"
        return True


def is_RD(x1, y1, is_dead):
    if ((x1 + 2) < len(matrix)) and (y1 - 1) >= 0 and is_dead:
        matrix[y1 - 1][x1 + 2] = "X"
        return True
    if ((x1 + 2) < len(matrix)) and (y1 - 1) >= 0 and is_dead == False:
        matrix[y1 - 1][x1 + 2] = "Y"
        return True


def is_DR(x1, y1, is_dead):
    if ((x1 + 1) < len(matrix)) and (y1 - 2) >= 0 and is_dead:
        matrix[y1 - 2][x1 + 1] = "X"
        return True
    if ((x1 + 1) < len(matrix)) and (y1 - 2) >= 0 and is_dead == False:
        matrix[y1 - 2][x1 + 1] = "Y"
        return True

#------------------------------------------------------------checking moves-------------------------------------------------------------

def check(x1, y1, is_dead):
    is_RU(x1, y1, is_dead)
    is_UR(x1, y1, is_dead)
    is_DL(x1, y1, is_dead)
    is_LU(x1, y1, is_dead)
    is_UL(x1, y1, is_dead)
    is_RD(x1, y1, is_dead)
    is_DR(x1, y1, is_dead)


def draw_matrix():
    complete_matrix = matrix * 2
    for b in complete_matrix:
        print(*(b * 2))


while True:
    if matrix[0].count("#") == 0 and matrix[1].count("#") == 0 and matrix[2].count("#") == 0 and matrix[3].count(
            "#") == 0:
        draw_matrix()
        break
    for y in range(4):
        for x in range(4):
            if matrix[y][x] == "Y":
                check(y, x, True)
            if matrix[y][x] == "X":
                check(y, x, False)
