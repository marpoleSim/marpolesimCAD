import { init, load, zoomAll, } from '/static/js/vtkFunc.js';

$(function () {

   // respond to geometry modification
   $('#parameterForm').on('submit', function (event) {
      event.preventDefault();
      $.ajax({
         url: 'modelling',
         type: 'POST',
         data: $(this).serialize(),
         dataType: 'json',
         success: function (response) {
         }
      });
   });

   // respond to initialize visualization
   $('#initForm').on('submit', function (event) {
      event.preventDefault();
      init();
   });

   // respond to initialize visualization
   $('#loadForm').on('submit', function (event) {
      event.preventDefault();
      load();
   });

   // respond to resetting visualization
   $('#zoomAllForm').on('submit', function (event) {
      event.preventDefault();
      zoomAll();
   });

});
