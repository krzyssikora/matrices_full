var loaded = 0;
const matrices_names = [];

(function() {
    "use strict";


    // info that mathJax is loading
    var pop_up = document.getElementById('pop-up-universal');  
    pop_up.style.display = 'block';

    var modal_content = document.getElementById('modal_div');
    var i = 0

    function checkLoaded() {
        if(loaded === 0) {
            for (let j=0; j<5; j++) {
                let clone = document.createElement('span');
                clone.innerHTML = 'mathematics is loading... ';
                clone.id = `wait_${i}`;
                i++;
                clone.style.color = '#' + Math.floor(Math.random()*16777215).toString(16);
                clone.style.backgroundColor = 'rgba(255, 255, 255, 0.2)';
                clone.style.fontSize = (50 + Math.floor(Math.random()*35)).toString(16) + 'px';
                modal_content.appendChild(clone);
            };
            window.setTimeout(checkLoaded, 1); 
        } else {
            setTimeout(() => {
                modal_content.innerHTML = '';
                pop_up.style.display = 'none';
            }, 1000)
        };
    }
    checkLoaded();

    // function ScrollToBottom(element) {
    //     element.scrollTop = element.scrollHeight - element.offsetHeight;
    // };

    var algebra_box = document.getElementById('algebra');
    var algebra_header = document.getElementById('algebra-header');
    algebra_header.style.width = algebra_box.clientWidth;
    
    var storage_box = document.getElementById('storage');
    var node = document.getElementById('matrix_a1');

    for (let i=0; i<=10; i++) {
        var clone = node.cloneNode(true);
        clone.innerHTML = clone.innerHTML.replace('A_1', `A_{${i + 2}}`);
        clone.id = `matrix_a${i + 2}`
        storage_box.appendChild(clone);
    };

    var user_input_field = document.getElementById('user-input');
    user_input_field.addEventListener('change', function() {
        console.log(user_input_field.value)
    });





    function correctMatrixName(matrix_name) {
        if (matrices_names.includes(matrix_name)) {
            return [false, `Matrix named "${matrix_name}" already exists.`]
        };

        for (let word of ["DET", "CLS", "HELP", "CREATE"]) {
            if (matrix_name.includes(word)) {
                return [false, `A matrix name cannot contain "${word}", it is a restricted word.`]
            };
        };

        if (matrix_name === 'T') {
            return [false, 'A matrix name cannot be "T", it is a restricted word.']
        };

        var letter_used = false;
        var digit_used = false;
        // only letters and digits allowed, digits must follow letters
        for (let letter of matrix_name) {
            if (!letter_used && ("0".charCodeAt(0) <= letter.charCodeAt(0)) && (letter.charCodeAt(0) <= "9".charCodeAt(0))) {
                return [false, "Letters must go before digits."]
            };
            if (("A".charCodeAt(0) <= letter.charCodeAt(0)) && (letter.charCodeAt(0) <= "Z".charCodeAt(0)) && digit_used) {
                return [false, "Digits must not be placed before letters."]
            };
            if (("A".charCodeAt(0) <= letter.charCodeAt(0)) && (letter.charCodeAt(0) <= "Z".charCodeAt(0))) {
                letter_used = true
            } else if (("0".charCodeAt(0) <= letter.charCodeAt(0)) && (letter.charCodeAt(0) <= "9".charCodeAt(0))) {
                digit_used = true
            } else {
                return [false, "Only letters and digits are allowed."]
            };
        };
        return [true, ''];
    };

    function correctMatrixDimension(dimension_string) {
        var dimension = parseInt(dimension_string)
        var dimension_string_2 = dimension.toString()
        if (dimension_string.length == dimension_string_2.length) {
            if ((dimension > 0) && (dimension < 10)) {
                return [true, dimension]
            } else {
                return [false, 'dimension must be a whole number between 1 and 9']
            };
        } else {
            return [false, 'dimension must be a whole number between 1 and 9']
        };
    };


    // define divs for enetering new matrix
    var matrix_name_div = document.getElementById('matrix-name-div');
    var matrix_dimensions_div = document.getElementById('matrix-dimensions-div');
    var matrix_input_div = document.getElementById('matrix-input');
    var matrix_rest_div = document.getElementById('matrix-rest');

    function makeGrid(rows_number, columns_number) {
        matrix_input_div.style.display = 'grid';
        var spot = document.getElementById('matrix-input');
        spot.innerHTML = '';
        spot.style.width = `${(30 + 6 + 6) * columns_number}px`;
        spot.style.gridTemplate = '1fr '.repeat(rows_number) + '/ ' + '1fr '.repeat(columns_number);
        var html = '';
        for (let r=0; r<rows_number; r++) {
            for (let c=0; c<columns_number; c++) {
                html += `<input type="text" class="matrix-elt", id=m_${r}_${c}""> `
            };
        };
        spot.innerHTML = html;
    };

    document.getElementById('add-matrix').addEventListener('click', (e) => {
        e.preventDefault();
        document.getElementById('enter_matrix').style.display = 'block';
        matrix_name_div.innerHTML = '<label class="pop-up-form-label" for="matrix-name" id="matrix-name-label"><b>matrix name</b></label><input class="pop-up-form-input" type="text" name="matrix-name" id="matrix-name"><span class="input-error-info" id="matrix-error-info"></span>';
        matrix_name_div.style.display = 'block';
        matrix_dimensions_div.innerHTML = '<label class="pop-up-form-label" for="rows" id="rows-label"><b>number of rows</b></label><input class="pop-up-form-input" type="text" name="rows" id="rows"><br><label class="pop-up-form-label" for="columns" id="columns-label"><b>number of columns</b></label><input class="pop-up-form-input" type="text" name="columns" id="columns"><span class="input-error-info" id="dimensions-error-info"></span>';
        matrix_dimensions_div.style.display = 'none';
        matrix_input_div.style.display = 'none';
        matrix_rest_div.style.display = 'none';


        const matrix_name_field = document.getElementById('matrix-name');
        const rows_field = document.getElementById('rows');
        const columns_field = document.getElementById('columns');
        const fields = [matrix_name_field, rows_field, columns_field];

        // switch of ENTER
        for (let field of fields) {
            matrix_name_field.addEventListener('keypress', (e) => {
                var key = e.charCode || e.keyCode || 0;     
                if (key == 13) {
                e.preventDefault();
                }
            });
        };

        // check name
        matrix_name_field.addEventListener('change', (e) => {
            e.preventDefault();
            var matrix_name = matrix_name_field.value.toUpperCase();
            var name_checked = correctMatrixName(matrix_name);
            var name_correct = name_checked[0];
            var name_message = name_checked[1];
            var rows_number = 0;
            var columns_number = 0;

            function checkDimension(field, field_str) {
                var info_dim = document.getElementById('dimensions-error-info');
                info_dim.style.display = 'none';
                var dim_checked = correctMatrixDimension(field.value);
                var dim_correct = dim_checked[0];
                var dim_message = dim_checked[1];
                if (dim_correct) {
                    if (field_str == 'rows') {
                        rows_number = dim_message
                    } else if (field_str == 'columns') {
                        columns_number = dim_message
                    };
                    if (rows_number > 0 && columns_number > 0) {
                        matrix_dimensions_div.innerHTML = `${rows_number} rows, ${columns_number} columns`;
                        matrix_rest_div.style.display = 'block';
                        makeGrid(rows_number, columns_number);
                    };
                } else {
                    info_dim.style.display = 'block'
                    info_dim.innerHTML = dim_message;
                };
            };

            if (name_correct) {
                // show rows and columns
                matrix_dimensions_div.style.display = 'block';
                // hide matrix name
                matrix_name_div.innerHTML = `matrix name: ${matrix_name}`;
                // get dimensions
                rows_field.addEventListener('change', (e) => {
                    e.preventDefault();
                    checkDimension(rows_field, 'rows')
                });
                columns_field.addEventListener('change', (e) => {
                    e.preventDefault();
                    checkDimension(columns_field, 'columns')
                });
                            
            } else {
                var info = document.getElementById('matrix-error-info');
                info.style.display = 'block';
                info.innerHTML = name_message;
            };
        });

        // makeGrid(2,3)

    })
})();