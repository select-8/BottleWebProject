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
    <td class="row-data">{{value}}</td>
% end
<td><button type="submit" onclick="show()" class="btn btn-info" name="alterdata">Edit</button></td>
<td><button type="button" class="btn btn-danger">Delete</button></td>
</tr>
% end
</table>
<br />
% include('button.tpl') 