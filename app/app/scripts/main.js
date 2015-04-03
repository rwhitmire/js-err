/*global $, Backbone, Marionette, http*/

(function() {
    'use strict';

    var App = new Marionette.Application();

    App.addRegions({
        mainRegion: '#main-region'
    });

    App.on('start', function() {
        Backbone.history.start();
    });


    $.ajaxSetup({
        beforeSend: function (xhr) {
            xhr.setRequestHeader('Authorization', 'Basic ' + $.cookie('token') || '');
        },
    });


    $(document).ready(function () {
        var promise = $.when(http.get('user'));

        promise.done(function(user){
            App.user = new App.Models.User(user);
            console.log('user.attributes', user);
        });

        promise.fail(function(response){
            if(response.status === 401) {
                window.location = '/login.html';
            }
        });

        App.start();
    });

    window.App = App;
})();