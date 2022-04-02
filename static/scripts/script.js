function show() {
    let rowId = event.target.parentNode.parentNode.id;
    //this gives id of tr whose button was clicked
    var data = document.getElementById(rowId).querySelectorAll(".row-data"); 
    /*returns array of all elements with "row-data" class within the row with given id*/
    //console.log(data)
    var id = data[0].innerHTML;
    let url = '/get_row_to_edit'
    let xhr = new XMLHttpRequest();
    xhr.open('POST', url, true);
    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(id);
}