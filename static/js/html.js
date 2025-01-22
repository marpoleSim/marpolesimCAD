function capitalizeFirstLetter(val) {
    return String(val).charAt(0).toUpperCase() + String(val).slice(1);
}

export function showParameter(data){

    $('#parameterTitle').show();
    $('#parameterForm').show();
    $('#status').hide();

    var html1='<h4> (' + capitalizeFirstLetter(data.functionName) +')</h4>' ;
    document.getElementById('parameterTitle').innerHTML = html1;

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
