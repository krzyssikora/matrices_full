options = [["action", "command/-s", "help command"],
           ["clear screen", "cls", "help cls"],
           ["multiply by a scalar", "2 * M, 1/2 * M, 1.2 * M, N = 5/2 * M", "help *"],
           ["add matrices", "M + N", "help +"],
           ["subtract matrices", "M - N", "help -"],
           ["multiply matrices", "M * N", "help *"],
           ["determinant of a matrix", "det(M)", "help det"],
           ["inverse of a matrix", "M^(-1)", "help inv"],
           ["transpose of a matrix", "M^T", "help T"],
           ["augment a matrix with another", "aug(M, N)", "help aug"],
           ["sub-matrix", "sub(M, rows, columns) - from top left or", "help sub"],
           ["", "sub(M, r0, r1, c0, c1)", ""],
           ["", " - rows from r0 to r1 inclusive", ""],
           ["", " - columns from c0 to c1 inclusive", ""],
           ["row echelon form", "ref(M)", "help ref"],
           ["reduced row echelon form", "rref(M)", "help rref"],
           ["assign result to a matrix", "M = ...", "help ="],
           ["", "(both to a new or existing matrix)", ""],
           ["create a new matrix", "create", "help create"],
           ["delete a matrix from memory and database", "del M, del(M)", "help del"],
           ["       or a few matrices at once", "del(M, N)", ""],
           ["change a matrix into a form that", "wolframalpha(M)", "help wolframalpha"],
           ["       can be used in wolframalpha.com", "", ""],
           ["", "", ""],
           ["", "(brackets may be used)", ""],
           ["", "(but only the round ones)", ""],
           ["", "", ""],
           ["end application", "end, quit, exit, out", "help end"]
           ]

help_explanations = [["CLS", "cls",
                      '''Clears the screen and prints again the names and dimensions 
                      of all matrices stored in the database.'''],
                     ["*", ["a * b", "a * M, M * a", "M * N"],
                      ['''Multiplies two numbers that are integers (e.g. 12) 
                      or fractions (e.g. 97/11) or decimals (e.g. 0.25)''',
                       '''OR multiplies a matrix M by a number a''',
                       '''OR multiplies matrix M by matrix N, where the number of columns 
                       in M is the same as the number of rows in N''']],
                     ["+", "M + N", '''Adds matrices if their dimensions (both rows and columns) are the same.'''],
                     ["-", "M - N", '''Subtracts matrices if their dimensions (both rows and columns) are the same.'''],
                     ["DET", "det(M)", '''Evaluates the determinant of a square matrix, i.e. a matrix
                     whose number of rows is equal to the number of columns.'''],
                     ["INV", "M^(-1)", '''Finds the inverse of an invertible square matrix, i.e.
                     a matrix whose number of rows is equal to the number of columns and
                     the determinant is non-zero.'''],
                     ["T", "M^T", '''Finds the transpose of a matrix, i.e. switches rows to columns.'''],
                     ["AUG", "aug(M, N)", '''Augments a matrix M with N, if their numbers of rows are equal.'''],
                     ["SUB", ["sub(M, r, c)", "sub(M, r0, r1, c0, c1)"],
                      ['''Finds a sub-matrix of a given matrix with rows from 1 to r and columns
                      from 1 to c (inclusive).''',
                       '''OR finds a sub-matrix of a given matrix with rows from r0 to r1
                       and columns from c0 to c1 (inclusive).''']],
                     ["REF", "ref(M)", '''Evaluates the row echelon form of a matrix, i.e. a form with 1's in 
                     the leading diagonal and 0's below the diagonal.'''],
                     ["RREF", "rref(M)", '''Evaluates the reduced row echelon form of a matrix, i.e. a form with
                     1's in the leading diagonal and 0's both below and above the diagonal.'''],
                     ["=", "M = ...", '''Can be used to assign result of the dotted expression to a matrix M. M can be
                     both a new or an existing matrix.'''],
                     ["CREATE", ["create", "create(r, c)"],
                      ["Starts the process of creating a nem matrix with either manual or pseudo-random inputs.",
                       "Creates a new matrix with pseudo-random inputs, with r rows and c columns."]],
                     ["DEL", ["del M, del(M)", "del(M, N)"],
                      ['''Deletes a matrix from the memory and from the database.''',
                       '''Deletes a few matrices from the database. Their names should be separated
                       by commas and they should be identical to those listed.''']],
                     ["QUIT", "quit, exit, out", '''Quits to the main menu.'''],
                     ["END", "end", '''Ends the application.'''],
                     ["WOLFRAMALPHA", "wolframalpha(M)",
                      "Changes the matrix M into a form that can be copied and pasted into wolframalpha.com. "
                      "An input M can be also an expression that results in a matrix."],
                     ["QUIT", "quit", '''Ends the application.'''],
                     ["EXIT", "exit", '''Ends the application.'''],
                     ["out", "out", '''Ends the application.''']
                     ]
