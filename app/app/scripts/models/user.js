/*global App, Backbone, http*/

App.module('Models', function(Models) {
    'use strict';

    Models.User = Backbone.Model.extend({

        url: http.api + 'user',

        defaults: {

        },

    });

});
