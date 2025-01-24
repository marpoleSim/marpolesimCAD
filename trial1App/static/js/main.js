import { init, display, zoomAll, } from '/static/js/vtkFunc.js';
import { showParameter, } from '/static/js/html.js';

$(function () {

   $(document).ready(function(){

      // enabling and disabling buttons
      $('#argsubmit').attr('disabled','disabled');
      $('#savePart').attr('disabled','disabled');

      // initialize window
      init();
      });

   // respond to geometry modification
   $('#parameterForm').on('submit', function (event) {
      event.preventDefault();

      $.each ( $('#selectPartForm select').serializeArray(), function ( i, obj ) {
          $('<input type="hidden">').prop( obj ).appendTo( $('#parameterForm') );
      } );

      // enabling and disabling buttons
      $('#select').attr('disabled','disabled');
      $('#savePart').attr('disabled','disabled');
 
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
                $('#savePart').removeAttr('disabled');
                document.getElementById('status').innerHTML = '<p>status: complete </p>';

                var partname = response.partName;
                var data = {'partname': partname}
                display(data);
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

      $('#partNameMessage').hide();
   
   });

   // respond to geometry modification
   $('#saveForm').on('submit', function (event) {
      event.preventDefault();

      $.each ( $('#parameterForm input').serializeArray(), function ( i, obj ) {
          $('<input type="hidden">').prop( obj ).appendTo( $('#saveForm') );
      } );

      // enabling and disabling buttons
      $('#select').attr('disabled','disabled');
      $('#savePart').attr('disabled','disabled');
 
      // display status
      document.getElementById('partNameMessage').innerHTML = '<p>status: proceeding ... </p>';
      $('#partNameMessage').show();

      $.ajax({
         url: 'savePart',
         type: 'POST',
         data: $(this).serialize(),
         dataType: 'json',
         success: function (response) {
             // display proceeding status
             if (response.flag) {
                document.getElementById('partNameMessage').innerHTML = '<p>status: part is saved </p>';
                $('#savePart').attr('disabled','disabled');
                $('#argsubmit').attr('disabled','disabled');
             } else {
                document.getElementById('partNameMessage').innerHTML = '<p>status: the name exists. change name. </p>';
                $('#savePart').removeAttr('disabled');
             }
         }
      });
   });

});
