def scalar_product(vector1, vector2):
    """
    Функция для вычисления скалярного произведения двух векторов.
    """
    return sum(v1 * v2 for v1, v2 in zip(vector1, vector2))

def vector_product(vector1, vector2):
    """
    Функция для вычисления векторного произведения двух векторов.
    Возвращает кортеж с координатами векторного произведения.
    """
    x1, y1, z1 = vector1
    x2, y2, z2 = vector2
    result_x = y1 * z2 - z1 * y2
    result_y = z1 * x2 - x1 * z2
    result_z = x1 * y2 - y1 * x2
    return (result_x, result_y, result_z)

