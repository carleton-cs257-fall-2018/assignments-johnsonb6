initialize();

function initialize() {
    var element = document.getElementById("10_day_button");
    if (element) {
        element.onclick = onForecastButtonClicked;
    }
    var historic_snowfall = document.getElementById("submit_historic_snowfall");
    if (historic_snowfall) {
        historic_snowfall.onclick = onHistoricSnowfallButtonClicked;
    }
    var snowfall_for_year = document.getElementById("submit_snowfall_for_year");
    if (snowfall_for_year) {
        snowfall_for_year.onclick = onHighestSnowfallInYearButtonClicked;
    }
}

function getBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
    return baseURL;
}

function onForecastButtonClicked() {
    var today = new Date();
    var dd = String(today.getDate());
    var mm = String(today.getMonth() + 1);
    var yyyy = String(2017);
    if (dd.length < 2) {
        dd = '0' + dd;
    }
    if (mm.length < 2) {
        mm = '0' + mm;
    }

    var today_date = yyyy + mm + dd;
    var ten_days_from_today = new Date();
    ten_days_from_today.setDate(today.getDate() + 10)
    var end_day = String(ten_days_from_today.getDate());
    var end_month = String(ten_days_from_today.getMonth() + 1);
    var end_year = String(2017);
    if (end_day.length < 2) {
        end_day = '0' + end_day;
    }
    if (end_month.length < 2) {
        end_month = '0' + end_month;
    }
    var ten_days_from_today_date = end_year + end_month + end_day;
    
    var url = getBaseURL() + '/jackson_hole/snowfall_for_period/start_date/' + today_date + '/end_date/' + ten_days_from_today_date;

    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(function(response) {
        var place_to_put_snowfall = document.getElementById('forecast_return');
        if (response.length == 0) {
            if (place_to_put_snowfall){
                place_to_put_snowfall.innerHTML = "no snowfall :(";
            } 

        }
        else{
            if (place_to_put_snowfall){
                var txt = "";
                response.forEach(myFunction);
                function myFunction(v) {
                    txt = txt + v + "in." + ", ";
                }
                place_to_put_snowfall.innerHTML = "Snowfall for the next 10 days:" + txt;
            }
        }
    })
    .catch(function(error) {
        console.log(error);
    });

}
function onHistoricSnowfallButtonClicked() {
       var start_date = document.getElementById("start_year").value + document.getElementById("start_month").value + document.getElementById("start_day").value;
       var end_date = document.getElementById("end_year").value + document.getElementById("end_month").value + document.getElementById("end_day").value;
       var url = getBaseURL() + '/jackson_hole/snowfall_for_period/start_date/' + start_date + '/end_date/' + end_date;
       fetch(url, {method: 'get'})
       .then((response) => response.json())
       .then(function(response) {
           var place_to_return = document.getElementById("historic_snowfall_results");
           if (response.length == 0) {
             place_to_return.innerHTML = "no snowfall in this range";
           }
          else{
              var txt = "";
             response.forEach(myFunction);
             function myFunction(v) {
                 txt = txt + v + "in." + ", ";
             }
             place_to_return.innerHTML = "Historic Snowfall for Specified Date Range:" + txt;

         }

    })
    .catch(function(error) {
        console.log(error);
    });
}

function onHighestSnowfallInYearButtonClicked() {
    var year = document.getElementById('snowfall_for_year').value;
    var url = getBaseURL() + "/jackson_hole/snowfall_date/year/" + year;
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(function(response) {
        var place_for_return = document.getElementById("highest_snowfall_in_year_results");
        if (place_for_return) {
            place_for_return.innerHTML = "Highest snowfall in " + year + ": " + response + " in.";
        }
    })
    .catch(function(error) {
        console.log(error);
    });
}
