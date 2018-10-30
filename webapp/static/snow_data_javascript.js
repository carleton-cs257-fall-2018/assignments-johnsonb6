initialize();

function initialize() {
    homePageBaseDepthAverage("jackson_hole")
    /*
    var element = document.getElementById("jackson_hole_average_base_depth");
    if (element) {
        element.innerHTML = "base_depth";
    }
    */
}

function getBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
    return baseURL;
}

function homePageBaseDepthAverage(resort_name) {
    var url = getBaseURL();
    // + '/' + resort_name + '/base_depth_average/date/20170101';

    var documentId = resort_name + '_average_base_depth';

    /*
    var element = document.getElementById(documentId);
    if (element) {
        element.innerHTML = "base_depth";
    }
    */


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
    //var url = getBaseURL();
    alert("clicked");
    var place_to_put_snowfall = document.getElementById("forecast_return");
    place_to_put_snowfall.innerHTML = "snowfall_list";
    if (place_to_put_snowfall) {
        place_to_put_snowfall.innerHTML = "snowfall_list";
    }
    /*
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(function(snowfall_list) {
        var place_to_put_snowfall = document.getElementById("forecast_return");
        if (place_to_put_snowfall){
            place_to_put_snowfall.innerHTML = snowfall_list;
        }
    })
    .catch(function(error) {
        console.log(error);
    });
    */

}
