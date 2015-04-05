App.module('Views.Errors', function(Errors) {
    'use strict';

    Errors.Details = Marionette.ItemView.extend({
        template: JST['errors/details.hbs'],
    });

});