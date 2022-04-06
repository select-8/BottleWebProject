function show() {
    let rowId = event.target.parentNode.parentNode.id;
    var data = document.getElementById(rowId).querySelectorAll(".row-data"); 
    var id = data[0].innerHTML;
    console.log('Id from JS:', id)
    $.post('/get_row_to_edit', id);
    window.location.replace(`/time_to_edit/${id}`);
};

function hide() {
    let rowId = event.target.parentNode.parentNode.id;
    var data = document.getElementById(rowId).querySelectorAll(".row-data"); 
    var id = data[0].innerHTML;
    $.post('/delete', id);
    window.location.reload();
}
