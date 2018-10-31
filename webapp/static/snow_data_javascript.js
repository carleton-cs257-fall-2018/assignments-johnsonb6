initialize();

function initialize() {
    homePageBaseDepthAverage("jackson_hole");
    homePageSnowfallAverage("jackson_hole");
    
    homePageBaseDepthAverage("telluride");
    homePageSnowfallAverage("telluride");

    homePageBaseDepthAverage("snowbird");
    homePageSnowfallAverage("snowbird");
    

    homePageBaseDepthAverage("whistler");
    homePageSnowfallAverage("whistler");


}

function getBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
    return baseURL;
}

function homePageBaseDepthAverage(resort_name) {
    var today = new Date();
    var dd = String(today.getDate());
    var mm = String(today.getMonth() + 1);
    var yyyy = String(today.getFullYear());
    if (dd.length < 2) {
        dd = '0' + dd;
    }
    if (mm.length < 2) {
        mm = '0' + mm;
    }
    
    var today_date = yyyy + mm + dd;

    var url = getBaseURL() + '/' + resort_name + '/base_depth_average/date/' + today_date;
    var documentId = resort_name + '_average_base_depth';

    fetch(url, {method: 'get'})

    .then((response) => response.json())    .then(function(response) {
        var element = document.getElementById(documentId);
        if (element){
            element.innerHTML = response;
        }
    })
    .catch(function(error) {
        console.log(error);
    });


}
function homePageSnowfallAverage(resort_name) {
   var url = getBaseURL() + '/' + resort_name + '/snowfall_average/date/20170101';
   
   var documentId = resort_name + '_average_snowfall';
   
   fetch(url, {method: 'get'})
   .then((response) => response.json())
   .then(function(response) {
       var element = document.getElementById(documentId);
       if (element){
           element.innerHTML = response;
       }
    })
    .catch(function(error) {
        console.log(error);
    });
}

function onForecastButtonClicked() {
    var url = getBaseURL() + '/jackson_hole/snowfall_for_period/start_date/20170101/end_date/20170104';
    
    
    
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
    var url = getBaseURL() + "/jackson_hole"  + '/snowfall_for_period/start_date/' + start_date + '/end_date/' + end_date;
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
