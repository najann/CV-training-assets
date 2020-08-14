async function init() {
    model = await tf.loadLayersModel("http://127.0.0.1:8000/");

    const imgEl = document.getElementById("img");
    const offset = tf.scalar(127.5);
    let input = tf.browser.fromPixels(imgEl);

    input = tf.tidy(() => {
        const a = input
            .resizeNearestNeighbor([224, 224])
            .toFloat()
            .sub(offset)
            .div(offset)
            .expandDims();
        // .reshape([1, 224, 224, 3])
        // .toFloat()
        // .div(tf.scalar(127))
        // .sub(tf.scalar(1));
        return a;
    });

    let result = await model.predict(input).array();
    result = result[0][0] < 0.5 ? 0 : 1;
    input.dispose()
    console.log(result)
}

init();