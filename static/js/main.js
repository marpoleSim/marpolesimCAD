import { init, load, clearDisplay, zoomAll, } from '/static/js/vtkFunc.js';
import { showParameter, } from '/static/js/html.js';

$(function () {

   $(document).ready(function(){

      // enabling and disabling buttons
      $('#argsubmit').attr('disabled','disabled');
      $('#load').attr('disabled','disabled');
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
      $('#load').attr('disabled','disabled');
      $('#savePart').attr('disabled','disabled');
 
      // clear display area
      clearDisplay()           

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
                document.getElementById('status').innerHTML = '<p>status: complete </p>';
                $('#load').removeAttr('disabled');
             } else {
                document.getElementById('status').innerHTML = '<p>status: failed to make part, adjust parameter(s). </p>';
                $('#load').attr('disabled','disabled');
             }
         }
      });
   });

   // respond to load file to display 
   $('#loadForm').on('submit', function (event) {
      event.preventDefault();

      $('#savePart').removeAttr('disabled');

      // add selectpartForm input to the current load form so we 
      // know what is the part name
      $.each ( $('#selectPartForm select').serializeArray(), function ( i, obj ) {
          $('<input type="hidden">').prop( obj ).appendTo( $('#loadForm') );
      } );

      // to get object of select item
      var partname = $('#selectPartForm select').serializeArray()[0].value;
      var data = {'partname': partname}

      // load data to screen 
      load(data);

      // hide status
      $('#status').hide();
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
      $('#load').attr('disabled','disabled');
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
      $('#load').attr('disabled','disabled');
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
