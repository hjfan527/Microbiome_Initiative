var waypoint = new Waypoint({
    element: document.getElementById('pathostat_tool'),
    handler: function (direction) {
        $('#pathostat_tool').addClass('animated slideInRight');
    }
});