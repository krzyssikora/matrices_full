from matrices import matrices_dict, matrices_str_dict
from matrices import database


def create_matrix():
    """Creates a matrix entered by a user.

    The user inputs the following information following a prompt:
    number of rows, number of columns and either entries entered manually or assigned randomly.

    The matrix is added to the global matrices_dict dictionary and to the database.
    """
    if len(matrices_dict) == 0:
        database.import_from_database()
    # asks for dimensions
    while True:
        r = input("Number of rows:    ")
        try:
            rows = int(r)
            break
        except Exception as e:
            print(e)
    while True:
        c = input("Number of columns: ")
        try:
            columns = int(c)
            break
        except Exception as e:
            print(e)
    # asks for the matrix name
    print("Matrix name (5 characters, only letters and digits, digits must follow letters).")
    print("A name cannot contain \"DET\", \"CLS\", \"HELP\", \"END\", \"QUIT\" and \"CREATE\" "
          "and be equal \"T\", as these are reserved words.")
    while True:
        name = input("Enter name: ").upper()
        correct, stderr = correct_matrix_name(name)
        if not correct:
            print(stderr)
        else:
            # asks for the method of creating the matrix:
            # either manually, or randomly
            while True:
                method = input("M - enter values manually\nR - assign pseudo-random values\n")
                if method in {"M", "m"}:
                    random_assignment = False
                    break
                if method in {"R", "r"}:
                    random_assignment = True
                    break
            matrices_dict.update({name: Matrix(rows, columns, random_assignment=random_assignment)})
            save_matrix(name)
            print("Matrix " + name + ":")
            print(matrices_dict.get(name))
            print("has been created.")
            break


def matrix_help_general_menu():
    """Displays general help information."""
    # prints out a table with general help hints
    print("+--------------------+")
    print("| General help info. |")
    print("+--------------------+")
    print("This app offers various operations on matrices with rational inputs,")
    print("Let M and N be the names of matrices.")
    print("The following are the available actions.")
    print("To get more details type in a help command.")
    print()
    max_len = [0, 0, 0]
    for i in range(len(options)):
        for j in range(3):
            if len(options[i][j]) > max_len[j]:
                max_len[j] = len(options[i][j])

    max_len[0] += 2
    print("+" + "-" * (max_len[0] + 4) + "+" + "-" * (max_len[1] + 2) + "+" + "-" * (max_len[2] + 2) + "+")
    for i, line in enumerate(options):
        str_action = line[0]
        str_command = line[1]
        str_help = line[2]
        str_ast = "*" if (i != 0 and str_action != "") else " "
        print("| " + str_ast + " " + str_action + " " * (max_len[0] - len(str_action)) + " | "
              + str_command + " " * (max_len[1] - len(str_command))
              + " | " + str_help + " " * (max_len[2] - len(str_help)) + " | ")
        if i == 0:
            print("+" + "-" * (max_len[0] + 4) + "+" + "-" * (max_len[1] + 2) + "+" + "-" * (max_len[2] + 2) + "+")
    print("+" + "-" * (max_len[0] + 4) + "+" + "-" * (max_len[1] + 2) + "+" + "-" * (max_len[2] + 2) + "+")


def matrix_help_command(help_command):
    """Displays help information for a single command.

    Args:
        help_command (str): A command that the user searches help about.

    Returns:
        empty string when the help info is displayed correctly,
        None otherwise.
    """
    help_commands = list()
    for elt in help_explanations:
        help_commands.append(elt[0])
    if help_command in help_commands:
        our_line = help_explanations[help_commands.index(help_command)]
        both_lists = [list(), list()]
        for i in [1, 2]:
            if isinstance(our_line[i], str):
                both_lists[i - 1] = [our_line[i]]
            elif isinstance(our_line[i], list):
                both_lists[i - 1] = our_line[i]
        list_command, list_action = both_lists[0], both_lists[1]
        max_lines = max(len(list_command), len(list_action))
        for _ in range(max_lines - len(list_command)):
            list_command.append("")
        for _ in range(max_lines - len(list_action)):
            list_action.append("")
        max_command, max_action = 0, 60
        for i in range(max_lines):
            if len(list_command[i]) > max_command:
                max_command = len(list_command[i])
        if max_command < len("commands"):
            max_command = len("commands")
        print("+" + "-" * (max_command + 2) + "+" + "-" * (max_action + 2) + "+")
        print("|" + " commands " + " " * (max_command - 8) + "|"
              + " action " + " " * (max_action - 6) + "|")
        print("+" + "-" * (max_command + 2) + "+" + "-" * (max_action + 2) + "+")
        for i in range(max_lines):
            print("| " + list_command[i] + " " * (max_command - len(list_command[i])) + " | ", end="")
            if len(list_action[i]) < max_action:
                print(list_action[i] + " " * (max_action - len(list_action[i])) + " |")
            else:
                print_list = list_action[i][:list_action[i][:max_action].rfind(" ")]
                print(print_list + " " * (max_action - len(print_list)) + " |")
                actions = list_action[i][len(print_list) + 1:].split()
                while True:
                    print_list = ""
                    while True:
                        if len(print_list) + len(actions[0]) > max_action:
                            break
                        print_list += actions.pop(0) + " "
                        if len(actions) == 0:
                            break
                    print("|" + " " * (max_command + 2) + "| "
                          + print_list + " " * (max_action - len(print_list)) + " |")
                    if len(actions) == 0:
                        break
        print("+" + "-" * (max_command + 2) + "+" + "-" * (max_action + 2) + "+")
        return ""
    else:
        return None
