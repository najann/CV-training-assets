% rebase('base.tpl', title='YOLO Object Detector')

<div id="home_container">
  <h1>Welcome to the YOLO image analyzer</h1>
  <hr>
  <form method="post" enctype="multipart/form-data" action="/analyze">
    <label>Please upload the file you want to be processed. <br />
      <input onclick="enableStyle('analyze')" type="file" id="unpredicted" name="unpredicted" accept="image" />
    </label>
    <br>
    <label> Define a confidence score:
      <select name="confidence" id="confidence">
        <option value="0.1">0.1</option>
        <option value="0.2">0.2</option>
        <option value="0.3">0.3</option>
        <option value="0.4">0.4</option>
        <option value="0.5" selected>0.5</option>
        <option value="0.6">0.6</option>
        <option value="0.7">0.7</option>
        <option value="0.8">0.8</option>
        <option value="0.9">0.9</option>
      </select>
    </label>
    <br>
    <label> Define a threshold:
      <select name="threshold" id="threshold">
        <option value="0.1">0.1</option>
        <option value="0.2">0.2</option>
        <option value="0.3" selected>0.3</option>
        <option value="0.4">0.4</option>
        <option value="0.5">0.5</option>
        <option value="0.6">0.6</option>
        <option value="0.7">0.7</option>
        <option value="0.8">0.8</option>
        <option value="0.9">0.9</option>
      </select>
    </label>
    <div id="submitwrapper">
      <button type="submit" id="analyze" class="disabled"> Find objects! </button>
    </div>
  </form>
</div>