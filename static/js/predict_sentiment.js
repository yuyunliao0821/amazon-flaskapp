function predict_sentiment() {
  
  var inputText = document.getElementById("textbox").value;
  var selectedModel = document.getElementById('ml-model').value;
  var predictionContainer = document.getElementById("prediction");
  var predictionText = document.getElementById("prediction-text")

  predictionContainer.style.display = "flex";

  var server_data=[{
    'text':inputText,
    'mlmodel':selectedModel
  }]

  $.post({
    url:"/predict", 
    data:JSON.stringify(server_data), 
    contentType:'application/json'}).done(function (data){
  predictionText.innerHTML = data;
  });

  //  $.get("/predict?"+"text="+inputText+"&"+"mlmodel="+selectedModel).done(function (data) {
  //    predictionText.innerHTML = data;
  //  })

}