function curveselect() {
    var selection = document.getElementById("curveselection");
    if (selection.value == 0) {
        document.getElementById("circleinput").hidden=true;
        document.getElementById("ellipseinput").hidden=true;
        console.log("nothing selected yet")
    }
    else if (selection.value == 1) {
        document.getElementById("circleinput").hidden=false;       document.getElementById("ellipseinput").hidden=true;
        console.log("circle was chosen")
    }
    else if (selection.value == 2) {
        document.getElementById("circleinput").hidden=true;
        document.getElementById("ellipseinput").hidden=false;
        console.log("ellipse was chosen")
    }

}
