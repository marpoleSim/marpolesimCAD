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
}

export function load(data){
    // ---
    // vtk pipeline source --> mapper --> actor
    // ---

    // source
    let partname = Object.values(data)[0];
    let vtpsrc = '/media/trial1/' + partname + '.vtp';  
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
    
    // ---
    // add the actor to the render
    // ---
    renderer.addActor(actor);
}

export function zoomAll(data) {

    renderer.resetCamera();
    renderWindow.render();
}

export function clearDisplay(data) {

    renderer.removeActor(actor);
    renderWindow.render();

}

