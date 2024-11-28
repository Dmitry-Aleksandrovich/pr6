import importlib
import sys
from vector import save_vectors_to_db

def main():
    # Ввод координат векторов
    vector1 = list(map(float, input("Введите координаты первого вектора (x y z): ").split()))
    vector2 = list(map(float, input("Введите координаты второго вектора (x y z): ").split()))

    # Динамическая загрузка функциональной части
    vector_ops = importlib.import_module('vector_operations')

    # Вычисления
    scalar_product = vector_ops.scalar_product(vector1, vector2)
    vector_product = vector_ops.vector_product(vector1, vector2)

    # Вывод результатов
    print(f"Скалярное произведение: {scalar_product}")
    print(f"Векторное произведение: {vector_product}")

    # Сохранение векторов в базу данных
    save_vectors_to_db(vector1, vector2)

    # Завершаем программу
    sys.exit("Программа завершена.")

if __name__ == '__main__':
    main()

