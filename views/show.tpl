% rebase('layout.tpl')
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
<br />
% include('button.tpl') 
<br />
<div id="bottle-map" style="height:500px;width:1000px;margin:0 auto;"></div>
<hr />