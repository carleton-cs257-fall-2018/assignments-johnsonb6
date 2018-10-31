st login: Tue Oct 30 13:34:12 on ttys003
eduroam-160-44:webapp brennanjohnson$ ssh johnsonb6@perlman.mathcs.carleton.edu
johnsonb6@perlman.mathcs.carleton.edu's password: 
Last login: Tue Oct 30 18:46:28 2018 from eduroam-160-44.dyn.carleton.edu

This is perlman.mathcs.carleton.edu running CentOS 7.

johnsonb6@perlman ~ $ cd /var/www/html/cs257/johnsonb6
johnsonb6@perlman /var/www/html/cs257/johnsonb6 $ cd assignments-johnsonb6/
johnsonb6@perlman /var/www/html/cs257/johnsonb6/assignments-johnsonb6 $ cd webapp
johnsonb6@perlman /var/www/html/cs257/johnsonb6/assignments-johnsonb6/webapp $ ls
api.py                  endpoints.py            run_website.py      static               templates               Whistler_Final.csv
csv_converter_final.py  Jackson_Hole.csv        Snowbird.csv        Telluride.csv        TestAPIQueries.py
dump.sql                Jackson_Hole_Final.csv  Snowbird_Final.csv  Telluride_Final.csv  Whistler_Blackcomb.csv
johnsonb6@perlman /var/www/html/cs257/johnsonb6/assignments-johnsonb6/webapp $ vi api.py
johnsonb6@perlman /var/www/html/cs257/johnsonb6/assignments-johnsonb6/webapp $ ls static/
jackson_hole_javascript.js  snow_data_css.css        telluride_javascript.js
snowbird_javascript.js      snow_data_javascript.js  whistler_javascript.js
johnsonb6@perlman /var/www/html/cs257/johnsonb6/assignments-johnsonb6/webapp $ vi static/snow_data_javascript.js 










johnsonb6@perlman /var/www/html/cs257/johnsonb6/assignments-johnsonb6/webapp $ vi static/jackson_hole_page.html
johnsonb6@perlman /var/www/html/cs257/johnsonb6/assignments-johnsonb6/webapp $ vi templates/jackson_hole_page.html
johnsonb6@perlman /var/www/html/cs257/johnsonb6/assignments-johnsonb6/webapp $ vi static/jackson_hole_javascript.js








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

    var url = getBaseURL() + '/telluride/snowfall_for_period/start_date/' + today_date + '/end_date/' + ten_days_from_today_date;

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
       var url = getBaseURL() + '/telluride/snowfall_for_period/start_date/' + start_date + '/end_date/' + end_date;
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
