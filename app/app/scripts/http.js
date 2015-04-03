(function(){
    'use strict';

    window.http = {

        api: 'http://localhost:5000/',

        get: function(url) {
            url = this.api + url;

            return $.ajax({
                url: url,
                type: 'GET',
                dataType: 'json',
                contentType: 'application/json',
            });
        },

        post: function(url, data) {
            url = this.api + url;

            if(typeof data === 'object'){
                data = JSON.stringify(data);
            }

            return $.ajax({
                url: url,
                type: 'POST',
                data: data,
                dataType: 'json',
                contentType: 'application/json',
            });
        }
    };

})();