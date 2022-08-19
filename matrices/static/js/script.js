(function() {
    "use strict";

    function ScrollToBottom(element) {
        element.scrollTop = element.scrollHeight - element.offsetHeight;
    };

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
})();