App.module('Controllers', function(Controllers) {
    'use strict';

    Controllers.MainController = Marionette.Controller.extend({

        dashboard: function() {
            var xhr = http.get('errors');

            xhr.done(function(errors) {
                var layout = new App.Views.Dashboard.Layout();
                App.mainRegion.show(layout);
            });
        }

    });

});
