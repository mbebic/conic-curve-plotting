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
}

function apply_validation_css() {
    document.getElementById("uiform").classList.add("was-validated");
}

function process_ui() {
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

    if (ctype.value === '0') {
        ctype.setCustomValidity("Must select a curve");
        // input span notifying user to select a curve
        uiform.classList.add("was-validated"); // paints the form with validation css
        return false;
    }

    else {
        ctype.setCustomValidity("");
        uiform.classList.add("was-validated"); // paints the form with validation css
        return uiform.checkValidity();

    }
}

function pop_djform() {
    let djform = document.getElementById("djform");
    conicselect = document.getElementById("curveselection");

    if (conicselect.value === '1') {
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
        djform["f"].value = (xc**2/eli_a**2)+(yc**2/eli_b**2)-r**2;
        console.log(djform["a"].value)
    }
    else {
        console.log("nothing was done")
    }

    djform.submit();
}

function set_up_ui() {
    let uiform = document.getElementById("uiform");
    uiform["csel"].addEventListener("change", remove_validation_css);
    // Array.from(uiform.elements).forEach(element => {
    //     element.addEventListener("change", remove_validation_css)
    //   });
}

document.addEventListener("DOMContentLoaded", set_up_ui());
