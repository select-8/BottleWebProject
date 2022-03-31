% rebase('layout.tpl')
<p>Add a new case to the list:</p>

<form action="/new" method="POST">
  <div class="form-group">
    <label for="City">City</label>
    <input type="text" class="form-control" id="City" aria-describedby="cityHelp" placeholder="Enter city" name="newcity">
    <small id="cityHelp" class="form-text text-muted">Enter a new city.</small>
  </div>
  <div class="form-group">
    <label for="Count">Count</label>
    <input type="text" class="form-control" id="Count" aria-describedby="countHelp" placeholder="Enter Count" name="newcolour">
    <small id="countHelp" class="form-text text-muted">Enter a Count for your new city.</small>
  </div>
  <div class="form-group">
    <label for="Colour">Colour</label>
    <input type="text" class="form-control" id="Colour" aria-describedby="colourHelp" placeholder="Enter colour" name="newcolour">
    <small id="colourHelp" class="form-text text-muted">Enter a new colour for your city.</small>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
<br />
<div id="bottle-map" style="height:420px;width:420px;margin:0 auto;"></div>
<hr />