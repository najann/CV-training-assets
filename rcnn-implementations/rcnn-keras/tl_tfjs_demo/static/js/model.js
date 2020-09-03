async function init() {
  document.getElementById("analysis-result-loader").style.display = 'none';
  document.getElementById("model-loader").style.display = 'grid';
  document.getElementById("main").style.display = 'none';
  document.getElementById("backbutton").style.display = 'none';
  document.getElementById("submit").disabled = true;

  try {
    model = await tf.loadLayersModel("http://localhost:8081");
  } catch (error) {
    try {
      model = await tf.loadLayersModel("http://localhost:80");
    } catch (samerror) {
      try {
        model = await tf.loadLayersModel("http://173.193.68.8:30002/");
      } catch (err) {
        document.getElementById("model-loader").style.display = 'none';
        alert('For some unknown reason, the model could not be retrieved. Please try again in a different browser.')
      }
    }
  }

  document.getElementById("model-loader").style.display = 'none';
  document.getElementById("main").style.display = 'grid';
}

async function analyze(inp) {
  // document.getElementById("analysis-result-loader").style.display = 'grid';


  // document.getElementById("main").style.display = 'none';

  input = tf.tidy(() => {
    const a = inp
      .resizeNearestNeighbor([224, 224])
      .toFloat()
      .expandDims();
    return a;
  });
  let result = await model.predict(input).array();
  result = result[0][0] < 0.5 ? "cat" : "dog";
  input.dispose();

  document.getElementById("analysis-result-loader").style.display = 'none';
  document.getElementById("result").innerHTML = '<h4>This is most likely a ' + result + '</h4><canvas id="resultimage"></canvas>';
  tf.browser.toPixels(inp, document.getElementById('resultimage'));
  document.getElementById("backbutton").style.display = 'grid';

}

init();