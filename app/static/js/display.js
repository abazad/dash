function displayGraph(messages) {
    $(function () {
        var users = new Array();
        var data = [];
        var colors = [];
        colors.push("#F7464A");
        colors.push("#46BFBD");

        for (key in messages) {
            users.push(key);
        }

        for (var i = 0; i < users.length; i++) {
            dataset = {};
            dataset['color'] = colors[i];
            dataset['label'] = users[i];
            dataset['value'] = messages[users[i]];
            data.push(dataset);
        }

// Get context with jQuery - using jQuery's .get() method.
        var ctx = $('#myChart').get(0).getContext("2d");
// This will get the first returned node in the jQuery collection.
        var myNewChart = new Chart(ctx);

        var myLineChart = new Chart(ctx).Doughnut(data);
    })
}