import psycopg2

try:
    conn = psycopg2.connect(
        user='webdb',
        password='webdb',
        host='lx01',
        port='5432',
        database='webdb'
    )

    cursor = conn.cursor()
    cursor.execute('select version()')
    record = cursor.fetchone()

    print(record)
except Exception as e:
    print(f'error: {e}')
finally:
    'conn' in locals() and \
    conn and \
    conn.close()
