//--------------------------------------Slider for Prices filter
function getPriceVals() {
    // Get slider price values
    var parent = this.parentNode;
    var slides = parent.getElementsByTagName("input");
    var slide1 = parseFloat(slides[0].value);
    var slide2 = parseFloat(slides[1].value);
    // Neither slider will clip the other, so make sure we determine which is larger
    if (slide1 > slide2) { var tmp = slide2;
        slide2 = slide1;
        slide1 = tmp; }

    var displayElement = parent.getElementsByClassName("rangePriceValues")[0];
    displayElement.innerHTML = "€ " + slide1 + " - €" + slide2;
}

//--------------------------------------Slider for Year filter
function getYearVals() {
    // Get Year slider values
    var parent = this.parentNode;
    var slides = parent.getElementsByTagName("input");
    var slide1 = parseFloat(slides[0].value);
    var slide2 = parseFloat(slides[1].value);
    // Neither slider will clip the other, so make sure we determine which is larger
    if (slide1 > slide2) { var tmp = slide2;
        slide2 = slide1;
        slide1 = tmp; }

    var displayElement = parent.getElementsByClassName("rangeYearValues")[0];
    displayElement.innerHTML = "From " + slide1 + " To " + slide2;
}
 
//----------------------------------------------- Initialize Sliders   
window.onload = function() {
    // For Price
    var sliderSectionsPrice = document.getElementsByClassName("range-slider-price");
    for (var x = 0; x < sliderSectionsPrice.length; x++) {
        var slidersPrice = sliderSectionsPrice[x].getElementsByTagName("input");
        for (var y = 0; y < slidersPrice.length; y++) {
            if (slidersPrice[y].type === "range") {
                slidersPrice[y].oninput = getPriceVals;
                // Manually trigger event first time to display values
                slidersPrice[y].oninput();
            }
        }
    }
    // For Year
    var sliderSectionsYear = document.getElementsByClassName("range-slider-year");
    for (var x = 0; x < sliderSectionsYear.length; x++) {
        var slidersYear = sliderSectionsYear[x].getElementsByTagName("input");
        for (var y = 0; y < slidersYear.length; y++) {
            if (slidersYear[y].type === "range") {
                slidersYear[y].oninput = getYearVals;
                // Manually trigger event first time to display values
                slidersYear[y].oninput();
            }
        }
    }
}