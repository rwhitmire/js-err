App.module('Views.Dashboard', function(Dashboard){
    'use strict';

    Dashboard.Layout = Marionette.LayoutView.extend({
        template: JST['dashboard/layout.hbs'],
        regions: {
            errors: '#errors'
        }
    });

});