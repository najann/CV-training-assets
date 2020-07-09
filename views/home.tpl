% rebase('base.tpl', title='YOLO Object Detector')

<div id="home_container">
  <h1>Welcome to the YOLO image analyzer</h1>
  <hr>
  <form method="post" enctype="multipart/form-data" action="/analyze">
    <label>Please upload the file you want to be processed. <br />
      <input onclick="enableStyle('analyze')" type="file" id="unpredicted" name="unpredicted" accept="image" />
    </label>
    <div id="submitwrapper">
      <button type="submit" id="analyze" class="disabled"> Find objects! </button>
    </div>
  </form>
</div>