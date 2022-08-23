from matrices import app
from matrices import matrices_dict, matrices_str_dict, tmp_matrices, matrices_names
from matrices import database, utils, algebra
from matrices.config import _logger
from flask import render_template, request

@app.route('/')
def index():
    global matrices_dict, matrices_str_dict, tmp_matrices, matrices_names
    matrices_dict = database.import_from_database()
    matrices_list = utils.get_list_of_matrix_dict_latexed(matrices_dict)
    matrices_names = [elt.split('=')[0].lstrip('\\(') for elt in matrices_list]
    return render_template('index.html',
                           matrices_names=matrices_names,
                           matrices_list=matrices_list)


@app.route('/delete_matrix/<int:idx>', methods=['POST'])
def get_matrix_to_delete(idx):
    global matrices_dict, matrices_str_dict, tmp_matrices, matrices_names
    matrix_name_to_delete = matrices_names[idx]
    database.delete_matrix(matrix_name_to_delete)
    matrices_list = utils.get_list_of_matrix_dict_latexed(matrices_dict)
    matrices_names = [elt.split('=')[0].lstrip('\\(') for elt in matrices_list]
    return render_template('index.html',
                           matrices_names=matrices_names,
                           matrices_list=matrices_list)
    # return '/'


@app.route('/create_matrix/<string:matrix>', methods=['POST'])
def get_matrix_data_to_create(matrix):
    global matrices_dict, matrices_str_dict, tmp_matrices, matrices_names
    matrix = matrix.replace('minussign', '-')
    matrix = matrix.replace('slashsign', '/')
    matrix = eval(matrix)
    values = algebra.get_fractions_from_list_of_strings(matrix['values'])
    name, rows, columns = matrix['name'], matrix['rows'], matrix['columns']
    if values and name and rows and columns:
        name, rows, columns = name.upper(), int(rows), int(columns)
        new_matrix = algebra.Matrix(rows, columns, values)
        matrices_dict[name] = new_matrix
        database.save_matrix(name)
    matrices_list = utils.get_list_of_matrix_dict_latexed(matrices_dict)
    matrices_names = [elt.split('=')[0].lstrip('\\(') for elt in matrices_list]
    return render_template('index.html',
                           matrices_names=matrices_names,
                           matrices_list=matrices_list)
    # return '/'


@app.route('/help')
def help():
    return render_template('help.html')
