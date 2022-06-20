function curveselect() {
    var selection = document.getElementById("curveselection");
    if (selection.value == 0) {
        document.getElementById("circleinput").hidden=true;
        document.getElementById("ellipseinput").hidden=true;
        console.log("nothing selected yet")
    }
    else if (selection.value == 1) {
        document.getElementById("circleinput").hidden=false;
        document.getElementById("ellipseinput").hidden=true;
        console.log("circle was chosen")
    }
    else if (selection.value == 2) {
        document.getElementById("circleinput").hidden=true;
        document.getElementById("ellipseinput").hidden=false;
        console.log("ellipse was chosen")
    }

}

function remove_validation_css() {
    document.getElementById("uiform").classList.remove("was-validated");
    document.getElementById("circleform").classList.remove("was-validated");
    document.getElementById("ellipseform").classList.remove("was-validated");
}

function apply_validation_css() {
    let csel = document.getElementById("curveselection");
    console.log("applying validation css" +csel.value)
    uiform.classList.add("was-validated");
    if (csel.value === '1') {
        let cform = document.getElementById("circleform");
        cform.classList.add("was-validated");
    }
    else if (csel.value === '2') {
        let eform = document.getElementById("ellipseform");
        eform.classList.add("was-validated");
    }
}

function process_ui() {
    console.log("entered process ui")
    let uiform = document.getElementById("uiform");
    let ui_valid = validateuiform();
    if (ui_valid) {
        pop_djform();
        console.log("sending into pop_djform")
    }
    else {
        // create message for notifiying correct entries were made
    }
}

function validateuiform() {
    let ctype = document.getElementById("curveselection");
    let uiform = document.getElementById("uiform");
    let uivalid = true;
    console.log("ctype val: "+ctype.value)
    if (ctype.value === '0') {
        ctype.setCustomValidity("Must select a curve");
    }
    else if (ctype.value === '1') {
        ctype.setCustomValidity("");
        temp = document.getElementById("circleform").checkValidity();
        uivalid = uivalid && temp;
    }
    else if (ctype.value === '2') {
        ctype.setCustomValidity("");
        temp = document.getElementById("ellipseform").checkValidity();
        uivalid = uivalid && temp;
    }
    temp = ctype.checkValidity();
    uivalid = uivalid && temp;
    apply_validation_css();
    return uivalid;
}


function pop_djform() {
    let djform = document.getElementById("djform");
    let conicselect = document.getElementById("curveselection");

    if (conicselect.value === '1') {
        let uiform = document.getElementById("circleform");
        let xc = parseFloat(uiform["cir-xc"].value);
        let yc = parseFloat(uiform["cir-yc"].value);
        let r = parseFloat(uiform["cir-r"].value);

        djform["a"].value = 1;
        djform["b"].value = 0;
        djform["c"].value = 1;
        djform["d"].value = -2*xc;
        djform["e"].value = -2*yc;
        djform["f"].value = xc**2+yc**2-r**2;
        console.log(djform["a"].value)
        
    }

    else if (conicselect.value === '2') {
        let uiform = document.getElementById("ellipseform");
        let xc = parseFloat(uiform["eli-xc"].value);
        let yc = parseFloat(uiform["eli-yc"].value);
        let eli_a = parseFloat(uiform["eli-a"].value);
        let eli_b = parseFloat(uiform["eli-b"].value);
        let eli_rot = parseFloat(uiform["eli-rot"].value);

        djform["a"].value = 1/(eli_a**2);
        djform["b"].value = 0;
        djform["c"].value = 1/(eli_b**2);
        djform["d"].value = -2*xc/(eli_a**2);
        djform["e"].value = -2*yc/(eli_b**2);
        djform["f"].value = (xc**2/eli_a**2)+(yc**2/eli_b**2)-1;
    }
    else {
        console.log("nothing was done")
    }

    //djform.submit();
}

function set_up_ui() {
    let uiform = document.getElementById("uiform");
    uiform["csel"].addEventListener("change", remove_validation_css);
    // Array.from(uiform.elements).forEach(element => {
    //     element.addEventListener("change", remove_validation_css)
    //   });
}

document.addEventListener("DOMContentLoaded", set_up_ui());