% rebase('layout.tpl')
<div class="container">
  <div class="row">
    <div class="col-md-4">
      <h3>Edit an entry:</h3>
      <br />
      <form action="/update" method="POST">
        <div class="form-group" style="display: none;">
          <input type="text" class="form-control" id="id" name="id" value={{data_in_a_list[0]}}>
        </div>
        <div class="form-group">
          <label for="City">City</label>
          <input type="text" disabled="disabled" class="form-control" id="City" name="newcity" value={{data_in_a_list[1]}}>
        </div>
        <div class="form-group">
          <label for="Count">Edit Count</label>
          <input type="text" class="form-control" id="Count" name="editedcount" value={{data_in_a_list[4]}}>
        </div>
        <div class="form-group">
          <label for="Colour">Edit Colour</label>
          <input type="text" class="form-control" id="Colour" name="editedcolour" value={{data_in_a_list[5]}}>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>
    <div class="col-md-8">
      <div id="bottle-map"></div>
    </div>
  </div>
</div>