/*global $, Backbone, Marionette*/

(function() {
    'use strict';

    var App = new Marionette.Application();

    App.on('start', function() {
        Backbone.history.start();
    });

    $(document).ready(function () {
        App.start();
    });

    window.App = App;
})();