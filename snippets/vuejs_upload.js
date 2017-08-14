'use strict';



new Vue({
  el: '#app',
  data: {
    image: ''
  },
  methods: {
    onFileChange: function onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      this.createImage(files[0]);
    },
    createImage: function createImage(file) {
      var image = new Image();
      var reader = new FileReader();
      var vm = this;

      reader.onload = function (e) {
        vm.image = e.target.result;
      };
      reader.readAsDataURL(file);
    },

    removeImage: function removeImage(e) {
      this.image = '';
    },

    postdata: function() {
        console.log('postdata');
        $.ajax({
        type: "POST",
        url: "snippets/reverse_pca.py",
        data: { 'hello': "world" },
        dataType: "json",
        success: function(data) {
                    console.log('success');
                    console.log(data);
                }
        });
     }
  }
});

// Tip: Look at this for UI https://scotch.io/tutorials/how-to-handle-file-uploads-in-vue-2
