


var rowNum = 0

function addFields(){    
    rowNum++
    var container = document.getElementById("container");
    var newMappingPair = createMapping();
    // var newMappingPair = document.createTextNode("Member " + (i+1))
    container.appendChild(newMappingPair);
    container.appendChild(document.createElement("br"));
}

function createMapping(){
    // bootstrap class
    var row = document.createElement("div")
    row.class = "form-row"
    
    // Cell
    var col1 = document.createElement("div")
    col1.class = "col-6" 
    var cell = document.createElement("input")
    cell.type = "text"
    cell.name = "cell" + rowNum
    cell.class = "form-control"
    col1.appendChild(cell)

    // Value
    var col2 = document.createElement("div")
    col2.class = "col-6" 
    var val = document.createElement("input")
    val.type = "text"
    val.name = "val" + rowNum
    val.class = "form-control"
    col2.appendChild(val)
    
    row.appendChild(col1)
    row.appendChild(col2)
}