from matrices import app
from matrices import matrices_dict, matrices_str_dict, tmp_matrices
from matrices import database, utils
from matrices.config import _logger
from flask import render_template, request


@app.route('/')
def index():
    matrices_dict = database.import_from_database()
    _logger.debug(matrices_dict)
    matrices_list = utils.get_list_of_matrix_dict_latexed(matrices_dict)
    for m in matrices_list:
        print(m)
    return render_template('index.html')


@app.route('/help')
def help():
    return render_template('help.html')
