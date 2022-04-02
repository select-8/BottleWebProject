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
<td>
<form action="/get_row_to_edit" method="post">
<button type="submit" onclick="show()" class="btn btn-info">Edit</button></td>
</form>
<td><button type="button" class="btn btn-danger">Delete</button></td>
</tr>
% end
</table>
<br />
% include('button.tpl') 