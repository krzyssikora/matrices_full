from flask import Flask
# initialize global variables
matrices_dict = dict()
matrices_str_dict = dict()
tmp_matrices = dict()
matrices_names = list()
assign_answer = [False, False, ""]

from matrices import database
from matrices.config import _logger

app = Flask(__name__)

import matrices.views

# todo:
#  1. assigning answers in user input
#  2. refreshing storage after 1
#  3. different way of refreshing storage
#  4. passing data from python to JS without hidden elements