initialize();

function initialize() {
    var element = document.getElementById("3_day_button");
    if (element) {
        element.onclick = onForecastButtonClicked;
    }
    var historic_snowfall = document.getElementById("submit_historic_snowfall");
    if (historic_snowfall) {
        historic_snowfall.onclick = onHistoricSnowfallButtonClicked;
    }
}

function getBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
    return baseURL;
}

function onForecastButtonClicked() {
     var url = getBaseURL() + '/telluride/snowfall_for_period/start_date/20170101/end_date/20170104';

     fetch(url, {method: 'get'})
     .then((response) => response.json())
     .then(function(response) {
         var place_to_put_snowfall = document.getElementById('forecast_return');
         if (place_to_put_snowfall){
             place_to_put_snowfall.innerHTML = response;
         }
     })
     .catch(function(error) {
         console.log(error);
       });

}
function onHistoricSnowfallButtonClicked() {
       var start_date = document.getElementById("start_year").value + document.getElementById("start_month").value + document.getElementById("start_day").value;
       var end_date = document.getElementById("end_year").value + document.getElementById("end_month").value + document.getElementById("end_day").value;
       var url = getBaseURL() + '/telluride/snowfall_for_period/start_date/' + start_date + '/end_date/' + end_date;
       fetch(url, {method: 'get'})
       .then((response) => response.json())
       .then(function(response) {
           var place_to_return = document.getElementById("historic_snowfall_results");
           if (place_to_return) {
             place_to_return.innerHTML = response;
        }
    })
    .catch(function(error) {
        console.log(error);
    });
}
