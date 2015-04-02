/*global App, Marionette*/

App.module('Controllers', function(Controllers) {
    'use strict';

    Controllers.MainController = Marionette.Controller.extend({

        dashboard: function() {
            console.log('dashboard.');
        }

    });

});
