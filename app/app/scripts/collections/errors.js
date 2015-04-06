App.module('Collections', function(Collections) {
    'use strict';

    Collections.Errors = Backbone.Collection.extend({
        model: App.Models.Error
    });

});