function showCrop() {
    let season = document.getElementById("season").value.toLowerCase();
    let result = document.getElementById("result");

    if (season === "summer") {
        result.innerHTML = "🌽 Suitable Crops: Maize, Cotton";
    } 
    else if (season === "winter") {
        result.innerHTML = "🌾 Suitable Crops: Wheat, Barley";
    } 
    else if (season === "rainy") {
        result.innerHTML = "🌱 Suitable Crops: Rice, Sugarcane";
    } 
    else {
        result.innerHTML = "❌ Please enter valid season (summer/winter/rainy)";
    }
}