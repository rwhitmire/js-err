App.module('Views.Errors', function(Errors) {
    'use strict';

    Errors.RowView = Marionette.ItemView.extend({
        template: JST['errors/row.hbs'],
        tagName: 'tr'
    });


    Errors.TableView = Marionette.CompositeView.extend({
        template: JST['errors/table.hbs'],
        childView: Errors.RowView,
        childViewContainer: '#error-rows'
    });

});