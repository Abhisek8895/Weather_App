console.log("Hello World")
document.addEventListener('DOMContentLoaded', function () {
    // Get all predefined city buttons
    var cityButtons = document.querySelectorAll('.suggestion');

    // Add click event listener to each button
    cityButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var cityName = this.getAttribute('data-city');
            console.log("I am ",cityName)
            // Update the value of the city input field
            console.log(document.getElementById('cityInput').value);
            document.getElementById('cityInput').value = cityName;
            console.log("This is",cityInput)
            // Submit the form
            document.getElementById('weatherForm').submit();
        });
    });
});
