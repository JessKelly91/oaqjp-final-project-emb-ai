let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200){
                let response = JSON.parse(xhttp.responseText);
                let formattedResponse = `For the given statement, the system response is 'anger': ${response.anger}, 'disgust': ${response.disgust}, 'fear': ${response.fear}, 'joy': ${response.joy}, and 'sadness': ${response.sadness}. The dominant emotion is ${response.dominant_emotion}.`;
                document.getElementById("system_response").innerHTML = formattedResponse;
            }
            else if (this.status == 400){
                document.getElementById("system_response").innerHTML = xhttp.responseText;
            }
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xhttp.send();
}
