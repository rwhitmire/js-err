/*global App, Marionette*/

App.module('Routers', function(Routers) {
    'use strict';

    Routers.Main = Marionette.AppRouter.extend({

        controller: new App.Controllers.MainController(),

        appRoutes: {
            'dashboard': 'dashboard'
        }

    });

    var router = new App.Routers.Main();    

});