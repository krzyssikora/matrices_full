from flask import Flask
matrices_dict = dict()
matrices_str_dict = dict()
from matrices import database
from matrices.config import _logger

app = Flask(__name__)
_logger.debug(matrices_dict)
matrices_dict = database.import_from_database()
_logger.debug(matrices_dict)

import matrices.views