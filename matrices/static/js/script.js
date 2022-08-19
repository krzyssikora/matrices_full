var loaded = 0;

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

    document.getElementById('add-matrix').addEventListener('click', (e) => {
        e.preventDefault();

        function makeGrid(rows_number, columns_number) {
            document.getElementById('enter_matrix').style.display = 'block';
            var spot = document.getElementById('matrix-input');
            spot.innerHTML = '';
            spot.style.width = `${(20 + 6 + 6) * columns_number}px`;
            spot.style.gridTemplate = '1fr '.repeat(rows_number) + '/ ' + '1fr '.repeat(columns_number);
            var html = '';
            for (let r=0; r<rows_number; r++) {
                for (let c=0; c<columns_number; c++) {
                    html += `<input type="text" class="matrix-elt", id=m_${r}_${c}""> `
                };
            };
            spot.innerHTML = html;
        };

        makeGrid(3, 4);
    })
})();