import { renderer, renderWindow, reader, actor, mapper } from '/static/js/vtkFunc.js';

function reset(data) {

    renderer.resetCamera();
    renderWindow.render();
}

function renderVtk(data) {

    let vtpsrc = `${data.vtpURLPath}/simpleBlock.vtp`;    
    reader.setUrl(vtpsrc);
    reader.loadData();
    mapper.setInputConnection(reader.getOutputPort());
    actor.setMapper(mapper);
    renderWindow.render();
}

$(function () {

   // respond to geometry modification
   $('#holeForm').on('submit', function (event) {
      event.preventDefault();
      $.ajax({
         url: 'setHole',
         type: 'POST',
         data: $(this).serialize(),
         dataType: 'json',
         success: function (response) {
            renderVtk(response);
         }
      });
   });

   // respond to resetting visualization
   $('#resetForm').on('submit', function (event) {
      event.preventDefault();
      reset();
   });

});
