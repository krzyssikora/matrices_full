import sqlite3
from matrices.algebra import Matrix


def import_from_database():
    """Imports matrices from database to the global dictionary matrices_dict."""
    global matrices_dict
    conn = sqlite3.connect('matrices_rational.sqlite')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS matrices
    (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name STRING, rows INTEGER, columns INTEGER, denominator INTEGER)
    ''')
    cur.execute("SELECT id, name, rows, columns, denominator FROM matrices")
    all_rows = cur.fetchall()
    ids = list()
    for matrix_data in all_rows:
        if matrix_data[1] in matrices_dict:
            continue
        else:
            matrices_dict.update({matrix_data[1]: Matrix(matrix_data[2], matrix_data[3])})
            matrices_dict.get(matrix_data[1]).denominator = matrix_data[4]
            ids.append([matrix_data[0], matrix_data[1]])
    for id_name in ids:
        matrix = matrices_dict.get(id_name[1])
        cur.execute("SELECT row, column, element FROM numerators WHERE matrix_id = ?", (id_name[0],))
        all_rows = cur.fetchall()
        for line in all_rows:
            matrix.mat[line[0]][line[1]] = line[2]
    conn.commit()
    cur.close()


def delete_matrix(m_name, fully=True):
    """Deletes the matrix from the database and, optionally, from the global matrices_dict dictionary.

    Args:
        m_name (str): A name, as in matrices_dict, not an actual object.
        fully (bool) - whether to delete from the matrices_dict, too
        fully = False is used in case of overwriting, i.e. creating a new matrix and storing it on an existing one.
        In such a case the matrix previously labeled with this name should be removed from the database,
        but in the dictionary an update is sufficient.
    """
    global matrices_dict
    conn = sqlite3.connect('matrices_rational.sqlite')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS matrices
    (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name STRING, rows INTEGER, columns INTEGER, denominator INTEGER)
    ''')
    cur.execute('''CREATE TABLE IF NOT EXISTS numerators
    (matrix_id INTEGER, row INTEGER, column INTEGER, element INTEGER)''')
    cur.execute('SELECT id FROM matrices WHERE name = ?', (m_name,))
    row = cur.fetchone()
    m_id = row[0]
    cur.execute('DELETE FROM matrices WHERE id = ?', (m_id,))
    cur.execute('DELETE FROM numerators WHERE matrix_id = ?', (m_id,))
    conn.commit()
    cur.close()
    if fully:
        del matrices_dict[m_name]
        print(f"The matrix {m_name} has been deleted from the database.")


def save_matrix(m_name):
    """Saves the matrix in the database.

        Args:
            m_name (str): A name, as in matrices_dict, not an actual object.

        Returns None if the matrix was not added to the global matrices_dic dictionary.
    """
    global matrices_dict
    conn = sqlite3.connect('matrices_rational.sqlite')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS matrices
    (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name STRING, rows INTEGER, columns INTEGER, denominator INTEGER)
    ''')
    cur.execute('''CREATE TABLE IF NOT EXISTS numerators
    (matrix_id INTEGER, row INTEGER, column INTEGER, element INTEGER)''')

    matrix = matrices_dict.get(m_name, None)
    if matrix is None:
        return None
    cur.execute('SELECT id FROM matrices WHERE name = ?', (m_name,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO matrices
        (name, rows, columns, denominator)
        VALUES (?, ?, ?, ?)''', (m_name, matrix.rows, matrix.columns, matrix.denominator))
        cur.execute('SELECT id FROM matrices WHERE name = ?', (m_name,))
        m_id = cur.fetchone()[0]
        for row in range(matrix.rows):
            for column in range(matrix.columns):
                cur.execute('INSERT INTO numerators (matrix_id, row, column, element) VALUES (?, ?, ?, ?)',
                            (m_id, row, column, matrix.mat[row][column]))
    conn.commit()
    cur.close()
