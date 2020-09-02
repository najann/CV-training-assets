var model;
async function init() {
  model = await tf.loadLayersModel("http://localhost:80/");
  console.log("ready");
}

async function analyze() {
  const imgEl = document.getElementById("output");
  let input = tf.browser.fromPixels(imgEl);

  input = tf.tidy(() => {
    const a = input
      .resizeNearestNeighbor([224, 224])
      .toFloat()
      .expandDims();
    return a;
  });
  console.log(model);
  let result = await model.predict(input).array();
  result = result[0][0] < 0.5 ? "cat" : "dog";
  input.dispose();
  alert(result);
}

init();