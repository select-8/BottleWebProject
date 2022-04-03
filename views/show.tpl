% rebase('layout.tpl')
<div class="container">
  <div class="row">
    <div class="col-md-12">
      <table class="table table-bordered">
        <thead>
          <tr>
          %for h in columns:
          <th scope="col">{{h[1]}}</th>
          %end
        </thead>
        % for td in table_data:
        <tr id={{td['ID']}}>
          % for key, value in td.items():
          % if key != 'IsVisible':
        <td class="row-data">{{value}}</td>
          % end
          % end
        <td>
          <button action='/get_row_to_edit' type="submit" onclick="show()" class="btn btn-info">Edit</button>
        </td>
        <td>
          <button type="submit" onclick="hide()" class="btn btn-danger">Delete</button>
        </td>
        </tr>
          % end
      </table>
    </div>
  </div>
  <div class="row">
    <div class="col-md-12 bg-light text-right">
      % include('button.tpl') 
    </div>
  </div>
  <br />
  <div class="row">
    <div class="col-md-12">
      <div id="bottle-map" style="height:600px;width:100%;margin:0 auto;"></div>
    </div> 
  </div>
</div> 
