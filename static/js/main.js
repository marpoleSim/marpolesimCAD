import { init, display, zoomAll, } from '/static/js/vtkFunc.js';
import { showParameter, } from '/static/js/html.js';

$(function () {

   $(document).ready(function(){

      // enabling and disabling buttons
      //$('#argsubmit').attr('disabled','disabled');
      $('#submitOrder').attr('disabled','disabled');

      // initialize window
      init();
      });

   // respond to geometry modification
   $('#parameterForm').on('submit', function (event) {
      event.preventDefault();

      // display status
      document.getElementById('status').innerHTML = '<p>status: proceeding ... </p>';
      $('#status').show();

      $.ajax({
         url: 'modelling',
         type: 'POST',
         data: $(this).serialize(),
         dataType: 'json',
         success: function (response) {
             // display proceeding status
             if (response.flag) {

                var partname = response.partName;

                let submitOrderButton;
                if(document.getElementById('submitOrder').disabled){
                   submitOrderButton = true;
                } else {
                   submitOrderButton = false;
                }

                var data = {'partname': partname, 'submitOrderButton': submitOrderButton, }

                display(data);

                $('#submitOrder').removeAttr('disabled');

                document.getElementById('status').innerHTML = '<p>status: complete </p>';

             } else {

                document.getElementById('status').innerHTML = '<p>status: failed to make part, adjust parameter(s). </p>';

             }
         }
      });
   });

   // respond to resetting visualization
   $('#zoomAllForm').on('submit', function (event) {
      event.preventDefault();

      zoomAll();
   });

   // respond to selecting part 
   $('#selectPartForm').on('submit', function (event) {
      event.preventDefault();

      // enabling and disabling buttons
      $('#select').attr('disabled','disabled');
      $('#savePart').attr('disabled','disabled');
      $('#argsubmit').removeAttr('disabled');

      $.ajax({
         url: 'geomParameter',
         type: 'POST',
         data: $(this).serialize(),
         dataType: 'json',
         success: function (response) {

            // display parameter input panel
            showParameter(response)
         }
      });
   });

   // respond to part selection change
   $("#selectPart").change(function () {
      event.preventDefault();

      // enabling and disabling buttons
      $('#select').removeAttr('disabled');
      $('#argsubmit').attr('disabled','disabled');
      $('#savePart').attr('disabled','disabled');

      // hide parameter title and inputs
      $('#parameterTitle').hide();
      $('#status').hide();
      let id;
      for( let i = 0; i < 9; i++) {
              id = (i+1).toString();
              $('#arg' + id).hide();
      }
   });

   // respond to geometry modification
   /*
   $('#submitOrderForm').on('submit', function (event) {
      event.preventDefault();

      $.each ( $('#parameterForm input').serializeArray(), function ( i, obj ) {
          $('<input type="hidden">').prop( obj ).appendTo( $('#submitOrderForm') );
      } );

      $.ajax({
         url: 'submit_order',
         type: 'POST',
         data: $(this).serialize(),
         dataType: 'json',
         success: function (response) {
             window.location.replace('order_receipt', response);
         }
      });
   });
   */
   $('#submitOrderForm').on('submit', function (event) {
      event.preventDefault();
      document.getElementById("partnameB").value = document.getElementById("partname").value;

      let arg_value_1;
      let arg_value_2;
      for( let i = 1; i < 10; i++) {
          arg_value_1 = 'argvalue' + (i).toString();
          arg_value_2 = 'argvalueB' + (i).toString();
          document.getElementById(arg_value_2).value = document.getElementById(arg_value_1).value;
      }
      
      document.getElementById("submitOrderForm").submit();
   });

});
