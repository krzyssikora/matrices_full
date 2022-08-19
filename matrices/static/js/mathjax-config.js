window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']]
  },
  svg: {
    fontCache: 'global'
  },
  startup: {
    ready: () => {
      // var pop_up = document.getElementById('pop-up-universal');  
      // pop_up.style.display = 'block';

      // var modal_content = document.getElementById('modal_div');
      // var node = modal_content.firstElementChild;
      // for (let i=1; i<10000; i++) {
      //   var clone = node.cloneNode(true);
      //   clone.id = `${i}`;
      //   clone.style.color = '#' + Math.floor(Math.random()*16777215).toString(16);
      //   modal_content.appendChild(clone);
      // };

      MathJax.startup.defaultReady();
      MathJax.startup.promise.then(() => {
        var algebra_box = document.getElementById('algebra');
        algebra_box.scrollTop = algebra_box.scrollHeight - algebra_box.offsetHeight;

        var storage_box = document.getElementById('storage');
        storage_box.scrollTop = storage_box.scrollHeight - storage_box.offsetHeight;
        loaded = 1;
        // pop_up.style.display = 'none';
      });
    }
  }
};