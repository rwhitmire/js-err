/*global $, Backbone, Marionette, http*/

(function() {
    'use strict';

    var App = new Marionette.Application();

    App.on('start', function() {
        Backbone.history.start();
    });


    $.ajaxSetup({
        beforeSend: function (xhr) {
            var token = $.cookie('token');
            if (!token) {
                return;
            }

            xhr.setRequestHeader('Authorization', 'Basic ' + token);
        },
    });



    $(document).ready(function () {
        var xhr = http.get('user');

        xhr.done(function(response){
            console.log(response);
        });

        xhr.fail(function(response){
            if(response.status === 401) {
                window.location = '/login.html';
            }
        });

        App.start();
    });

    window.App = App;
})();