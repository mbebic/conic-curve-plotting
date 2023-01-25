"use strict";

var plottedarray;
var curveindex;
var nshown = 0;

document.addEventListener("DOMContentLoaded", set_up_ui());

function getcurvefake(id) {
    let x = Array.from(Array(100).keys());
    let y = Array.from({length:100}, () => Math.random());
    return {"x": x, "y": y, "name": id}
    // return 'test'

}

// called by Refresh Plots button.
function processtable() {
    let t = document.getElementById("conictable"); // table of curves populated from django database
    let box = document.getElementById("curveoutput"); // output box for development, hide when done
    let g = document.getElementById("graph"); // Division containing the plotly graph
    let runlocally = false;

    for (var i = 1; i < t.rows.length; i++) {
        let r = t.rows[i]; // retrieving table row
        let l = r.cells.length; // need length to access last element
        let s = r.cells[l-1].childNodes[0]; // by convention, last element is a checkbox
        let id = r.cells[0].innerHTML; // retrieving curve id
        if (s.checked) { 
            // box is checked, see if curve is already plotted 
            if (plottedarray[i] === 0) {
                // generate curves locally, or get from the server
                if (runlocally) {
                    // Create fake data locally and add it to graph 'g' at position 'nshown'
                    let curvedata = getcurvefake(id);
                    Plotly.addTraces(g, x="test label", [curvedata], nshown);
                }
                else {
                    // Call an asynchronous function that sends an id to the server
                    // obtains xy data, adds it to graph 'g' at position 'nshown' and 
                    // updates tracking variables
                    plotcurve(id, g, i);
                }
                
                // Post action to msg box, tracking variables are updated within plot_curve 
                box.innerHTML += 'Add curve ID '+id+' to Index '+curveindex[i]+'\n';
            } 
        }
        else {
            // box is unchecked, see if curve needs to be removed
            if (plottedarray[i] === 1) {
                // plotted, need to remove
                let g = document.getElementById("graph");
                let ix = curveindex[i];
                Plotly.deleteTraces(g, ix); // removed trace
                curveindex[i] = null; // updated the cooresponding index val
                // drop indices of remaining curves
                curveindex.forEach((x, j) => {if (x > ix) {curveindex[j] = x-1}});
                box.innerHTML += 'Remove curve ID '+id+' Index '+curveindex[i]+'\n';
                nshown += -1;
                plottedarray[i] = 0; // registering curve removal
            }
        }
    }
}

// Obtains the curve points by id and plots it to graph 'g' at position 'n'
function plotcurve(cid, g, i) {
    console.log("Making a fetch request for cid=" + cid);
    const myRequest = new Request(calcconic_url, { // calcconic_url assigned in html script block
            method: 'POST', 
            headers: {
                "X-CSRFToken": Cookies.get('csrftoken'),
                "Accept": "application/json",
                "Content-Type": "application/json",
                'X-Requested-With': 'XMLHttpRequest'
            },
            cache: 'no-cache',
            body: JSON.stringify({id: cid})
        });
    fetch(myRequest)
    .then(response => {
        if (response.status === 403){
            throw new Error('You are not authorized to use this resource.');
        }
        const contentType = response.headers.get('content-type');
        if (!contentType || !contentType.includes('application/json')) {
          throw new TypeError("Returned object is not a JSON");
        }
        return response.json();
     })
    .then(curvexy => {
        // output xy inot text box to see if resolving correctly
        // document.getElementById("curveoutput").innerHTML += JSON.stringify(curvexy)+'\n';
        // add curve to the existing plotly graph
        console.log("adding curve id "+cid+" at index "+nshown);
        Plotly.addTraces(g, [curvexy], nshown);
        plottedarray[i] = 1; // registering curve addition
        curveindex[i] = nshown; // memorizing curve index within the Plotly traces stack
        nshown += 1;
    })
    .catch(error => {
        // The curve cannot be plotted, publish the error message to the console and return
        console.error(error);
        // Note that the checkmark in the table will remain. This is an artifact of a demo 
        // nature of this app, not a real problem. User authorizations in a production app are handled 
        // *before* a call to fetch is even attempted; this level of error handling is here just to 
        // aid in troubleshooting during development.  
    });
}


function set_up_ui() {
    let t = document.getElementById("conictable");
    // fills array of conic tables length -1 to accomodate for the
    // row of the table headers
    plottedarray = Array(t.rows.length).fill(0);
    curveindex = Array(t.rows.length).fill(null);
    // Create an empty graph using Plotly 
    let g = document.getElementById("graph");
    let layout  = {
        // xaxis: {
        //     autorange: false,
        //     range: [-10,10]
        // },
        yaxis: {
            // autorange: false,
            scaleanchor: 'x', 
            scaleratio: 1
        }
    };
    Plotly.newPlot(g, [], layout);
}


function graphgridsetup() {
    let xmin = document.getElementById("xmin").value;
    let xmax = document.getElementById("xmax").value;
    let ymin = document.getElementById("ymin").value;
    let ymax = document.getElementById("ymax").value;
    let gtitle = document.getElementById("gtitle").value;

    let g = document.getElementById("graph");
    
    let update = {
        title: gtitle,

        'xaxis.range': [xmin,xmax],
        'yaxis.range': [ymin,ymax]
    }

    Plotly.relayout(g, update);
    // graph.layout.xaxis.range[0] = xmin;
    // graph.layout.xaxis.range[1] = xmax;
    // graph.layout.yaxis.range[0] = ymin;
    // graph.layout.yaxis.range[1] = ymax;

}