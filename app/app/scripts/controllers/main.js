App.module('Controllers', function(Controllers) {
    'use strict';

    Controllers.MainController = Marionette.Controller.extend({

        dashboard: function() {
            var xhr = http.get('errors');

            xhr.done(function(errors) {
                var layout = new App.Views.Dashboard.Layout();
                App.mainRegion.show(layout);
            });
        },

        error: function(id) {

            var xhr = http.get('errors/' + id);

            xhr.done(function(error) {

                console.log('error', error);

                var layout = new App.Views.Errors.DetailsLayout();
                App.mainRegion.show(layout);

                var errorModel = new App.Models.Error(error);

                var detailsView = new App.Views.Errors.Details({
                    model: errorModel,
                });

                layout.showChildView('details', detailsView);
            });


          
        }

    });

});
