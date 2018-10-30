initialize();

function initialize() {
    homePageBaseDepthAverage("jackson_hole");
    homePageSnowfallAverage("jackson_hole");
    var element = document.getElementById("3_day_button");
    if (element) {
        element.onclick = onForecastButtonClicked;
    }    
}

function getBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
    return baseURL;
}

function homePageBaseDepthAverage(resort_name) {
    var url = getBaseURL() + '/' + resort_name + '/base_depth_average/date/20170101';

    var documentId = resort_name + '_average_base_depth';

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
