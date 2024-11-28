import psycopg2  # импортируем psycopg2

def save_vectors_to_db(vector1, vector2):
    """
    Сохранение векторов в базу данных PostgreSQL.
    """
    try:
        # Подключение к базе данных
        conn = psycopg2.connect(
            host="localhost",
            database="vector_operations",
            user="user",
            password="password"
        )
        cur = conn.cursor()

        print("Соединение с базой данных установлено.")

        # Запрос на вставку данных
        query = """
        INSERT INTO Vectors (vector1_x, vector1_y, vector1_z, vector2_x, vector2_y, vector2_z)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (*vector1, *vector2))

        # Применение изменений и закрытие соединения
        conn.commit()
        print("Векторы успешно сохранены в базу данных.")
        cur.close()
        conn.close()

    except Exception as e:
        print(f"Ошибка при работе с базой данных: {e}")

