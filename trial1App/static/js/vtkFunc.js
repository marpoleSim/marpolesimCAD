let vtkRenderScreen;
let renderer;
let renderWindow;

let reader;
let mapper;
let actor;

export function init(data){

    // ----
    // standard rendering code setup
    // ---
    vtkRenderScreen = vtk.Rendering.Misc.vtkFullScreenRenderWindow.newInstance({
        container: document.querySelector('#vtkContainer'), background: [0.2, 0.3, 0.4] });
    renderer = vtkRenderScreen.getRenderer();
    renderWindow = vtkRenderScreen.getRenderWindow();
      
    // ---
    // create instances
    // ---
    reader = vtk.IO.XML.vtkXMLPolyDataReader.newInstance();
    mapper   = vtk.Rendering.Core.vtkMapper.newInstance();
    actor    = vtk.Rendering.Core.vtkActor.newInstance();

    // ---
    // vtk pipeline source --> mapper --> actor
    // ---

    // source
    let vtpsrc = '/media/trial1/mCAD.vtp'
    reader.setUrl(vtpsrc).then(() => {
        reader.loadData().then(() => {

          zoomAll();
      });
    });

    // ---
    // mapper
    // ---
    mapper.setInputConnection(reader.getOutputPort());

    // ---
    // actor
    // ---
    actor.setMapper(mapper);
    actor.getProperty().setColor(1, 0.6, 0.2);

    // ---
    // add the actor to the render
    // ---
    renderer.addActor(actor);

    // slightly adjust camera angles
    renderer.getActiveCamera().azimuth(20);
    renderer.getActiveCamera().pitch(-10);

}

export function display(data){

    // load data and display
    let partname = data.partname;
    let submitOrderButton = data.submitOrderButton;

    let vtpsrc = '/media/trial1/' + partname + '.vtp';  
    reader.setUrl(vtpsrc).then(() => {
        reader.loadData().then(() => {
          actor.getProperty().setColor(0.78, 0.80, 0.81);  // aluminium color
          if (submitOrderButton) {
              renderer.resetCamera();
          }
          renderWindow.render();
      });
    }); 
}

export function zoomAll(data) {

    renderer.resetCamera();
    renderWindow.render();
}

export function clearDisplay(data) {

    renderer.removeActor(actor);
    renderWindow.render();

}

