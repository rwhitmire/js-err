App.module('Views.Errors', function(Errors) {
    'use strict';

    Errors.DetailsLayout = Marionette.LayoutView.extend({
        template: JST['errors/details-layout.hbs'],
        regions: {
            details: '#error-details',
        }
    });

});
