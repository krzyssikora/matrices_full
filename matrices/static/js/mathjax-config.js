window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']]
  },
  svg: {
    fontCache: 'global'
  },
  startup: {
    ready: () => {
      MathJax.startup.defaultReady();
      MathJax.startup.promise.then(() => {
        var algebra_box = document.getElementById('algebra');
        algebra_box.scrollTop = algebra_box.scrollHeight - algebra_box.offsetHeight;

        var storage_box = document.getElementById('storage');
        storage_box.scrollTop = storage_box.scrollHeight - storage_box.offsetHeight;
        loaded = 1;
      });
    }
  }
};