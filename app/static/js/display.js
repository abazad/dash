function displayDoughnutGraph(messages) {
    $(function () {
        var users = new Array();
        var doughnutData = [];
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
            doughnutData.push(dataset);
        }

// Get context with jQuery - using jQuery's .get() method.
        var ctx = $('#doughnut').get(0).getContext("2d");

        var myDoughnutChart = new Chart(ctx).Doughnut(doughnutData);
    })
}

function displayLineGraph(dateGraph) {
    $(function () {
        var dates = new Array();

        for (key in dateGraph) {
            dates.push(key);
        }
        dates.sort();

        var lineData = {
            labels: dates,
            datasets: [
                {
                label: "Kevin Shi",
                fillColor: "rgba(220,220,220,0.2)",
                strokeColor: "rgba(220,220,220,1)",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: []
            },
                {
                    label: "You",
                    fillColor: "rgba(151,187,205,0.2)",
                    strokeColor: "rgba(151,187,205,1)",
                    pointColor: "rgba(151,187,205,1)",
                    pointStrokeColor: "#fff",
                    pointHighlightFill: "#fff",
                    pointHighlightStroke: "rgba(151,187,205,1)",
                    data: []
                }
            ]
        }

        for (var i = 0; i < dates.length; i++) {
            lineData.datasets[0].data.push(dateGraph[dates[i]]["Kevin Shi"]);
            lineData.datasets[1].data.push(dateGraph[dates[i]]["You"]);
        }

        var ctx2 = $('#linegraph').get(0).getContext("2d");
        var myLineChart = new Chart(ctx2).Line(lineData);
    })
}