% rebase('layout.tpl')
<div class="container">
  <div class="row">
    <div class="col-md-4">
      <h3>Add a new place to the list:</h3>
      <br />
      <form action="/new" method="POST">
        <div class="form-group">
          <label for="City">City</label>
          <input type="text" class="form-control" id="City" placeholder="Enter city" name="newCity">
        </div>
        <div class="form-group">
          <label for="City">Longitude</label>
          <input type="text" class="form-control" id="Lang" placeholder="Click on the map (ish)" name="newLong">
        </div>
        <div class="form-group">
          <label for="City">Latitude</label>
          <input type="text" class="form-control" id="Lat" placeholder="Click on the map (ish)" name="newLat">
        </div>
        <div class="form-group">
          <label for="Count">Count</label>
          <input type="text" class="form-control" id="Count" placeholder="Enter Count" name="newCount">
        </div>
        <div class="form-group">
          <label for="Colour">Colour</label>
          <input type="text" class="form-control" id="Colour" placeholder="Enter colour" name="newColour">
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>
    <div class="col-md-8">
      <div id="bottle-map"></div>
    </div>
  </row>
</div>