function displayGraph(messages) {
    $(function() {
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

        options = {
            segmentShowStroke : true
        }

        var ctx = $('#myChart').get(0).getContext("2d");
        var myLineChart = new Chart(ctx).Doughnut(data, options);
        var legend = myLineChart.generateLegend();
        $('#myChart').append(legend);
    })
}