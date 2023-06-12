odoo.define('proyecto3.contador', function (require) {
    'use strict';

    var core = require('web.core');
    var qweb = core.qweb;

    var Contador = core.Widget.extend({
        events: {
            'click .sumar': '_sumar',
            'click .restar': '_restar',
        },
        init: function (parent) {
            this._super.apply(this, arguments);
            this.cantidad = 0;
        },
        _sumar: function () {
            this.cantidad++;
            this.$('.cantidad').val(this.cantidad);
        },
        _restar: function () {
            if (this.cantidad > 0) {
                this.cantidad--;
                this.$('.cantidad').val(this.cantidad);
            }
        },
        start: function () {
            this.$el.html(qweb.render('proyecto3.contador_template'));
        },
    });

    core.action_registry.add('proyecto3.contador', Contador);

    return Contador;
});