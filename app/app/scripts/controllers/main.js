App.module('Controllers', function(Controllers) {
    'use strict';

    Controllers.MainController = Marionette.Controller.extend({

        dashboard: function() {
            var xhr = http.get('errors');

            xhr.done(function(errors) {
                console.log(errors);
                var layout = new App.Views.Dashboard.Layout();

                var errorTableView = new App.Views.Errors.TableView({
                    collection: new App.Collections.Errors(errors),
                });
                
                App.mainRegion.show(layout);
                layout.showChildView('errors', errorTableView);
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
