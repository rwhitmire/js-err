(function(){
    'use strict';

    window.http = {
        get: function(url) {
            url = 'http://localhost:5000/' + url;

            return $.ajax({
                url: url,
                type: 'GET',
                dataType: 'json',
                contentType: 'application/json',
            });
        },

        post: function(url, data) {
            url = 'http://localhost:5000/' + url;

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