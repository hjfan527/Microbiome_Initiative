Vue.http.options.emulateJSON = true; // send as 

new Vue({
    el: '#vueApp', // id of the object
    data: {
        debug: true,
        domain: '',
        ajaxRequest: false,
        postResults: []
    },
    methods: {
      checkWebsite: function() {
        this.ajaxRequest = true;
        this.$http.post("link to script", {
              domain: this.domain
            }, function (data, status, request) {
                this.postResults = data; // the data that needs to be sent
                this.ajaxRequest = false;
            });
      }}
});

new Vue({
    el: '#vueApp',
    data: {},
    methods: {
        postdata: function() {
            $.ajax({
            type: "POST",
            url: "/reverse_pca.py",
            data: { param: input },
            success: callbackFunc
            });
        }
    }
});
