function capitalizeFirstLetter(val) {
    return String(val).charAt(0).toUpperCase() + String(val).slice(1);
}

export function showParameter(data){

    $('#parameterTitle').show();
    $('#parameterForm').show();
    $('#status').hide();

    let id;
    for( let i = 0; i < 9; i++) {
        if (i<data.numberOfArgs){
            id = (i+1).toString();
            document.getElementById('argname' + id).innerHTML = data.argNames[i] + ': ';
            document.getElementById('argvalue' + id).value = data.argValues[i];
            $('#arg' + id).show();
        } else {
            id = (i+1).toString();
            $('#arg' + id).hide();
        }
    } 
}

export function showOrderParameter(data){

    //$('#parameterTitle').show();
    //$('#parameterForm').show();
    //$('#status').hide();
    $('#argsubmit').show();

    document.getElementById('partname').value = data.partname;
    document.getElementById('orderId').value = data.orderId;

    let id;
    for( let i = 0; i < 9; i++) {
        if (i<data.numberOfArgs){
            id = (i+1).toString();
            document.getElementById('argname' + id).innerHTML = data.arg_names[i] + ': ';
            document.getElementById('argvalue' + id).value = data.arg_values[i].toString();
            $('#arg' + id).show();
        } else {
            id = (i+1).toString();
            $('#arg' + id).hide();
        }
    }
}
