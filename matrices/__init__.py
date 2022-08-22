from flask import Flask
# initialize global variables
matrices_dict = dict()
matrices_str_dict = dict()
tmp_matrices = dict()
matrices_names = list()

from matrices import database
from matrices.config import _logger

app = Flask(__name__)

import matrices.views