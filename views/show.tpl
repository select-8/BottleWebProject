% rebase('layout.tpl')
<table class="table table-striped">
<thead>
  <tr>
  %for h in columns:
    <th scope="col">{{h[1]}}</th>
  %end
%for row in table_data:
<tbody>

  <tr>
  % for col in row:
  <td class="c2">{{col[1]}}</td>
  % end
  <td><button type="button" class="btn btn-info">Edit</button></td>
  <td><button type="button" class="btn btn-danger">Delete</button></td>
  </tr>
</tbody>
%end
</table>
</br>
% include('button.tpl') 