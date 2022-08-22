from matrices import app
from matrices import matrices_dict, matrices_str_dict, tmp_matrices, matrices_names
from matrices import database, utils
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
    return '/'


@app.route('/create_matrix/<string:matrix>', methods=['POST'])
def get_matrix_data_to_create(matrix):
    global matrices_dict, matrices_str_dict, tmp_matrices, matrices_names
    _logger.debug(eval(matrix))
    return '/'


@app.route('/help')
def help():
    return render_template('help.html')
