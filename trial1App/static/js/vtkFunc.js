// ----
// standard rendering code setup
// ---
  
const vtkRenderScreen = vtk.Rendering.Misc.vtkFullScreenRenderWindow.newInstance({
container: document.querySelector('#vtkContainer'), background: [0.2, 0.3, 0.4] });

export var renderer = vtkRenderScreen.getRenderer();
export var renderWindow = vtkRenderScreen.getRenderWindow();
  
// ---
// vtk pipeline source --> mapper --> actor
// ---
  
// source
export const reader = vtk.IO.XML.vtkXMLPolyDataReader.newInstance();

let simpleBlocksrc = '/media/trial1/simpleBlock.vtp';  
reader.setUrl(simpleBlocksrc).then(() => {
    reader.loadData().then(() => {

      renderer.resetCamera();
      renderWindow.render();
  });
}); 

// ---
// mapper
// ---
export var mapper             = vtk.Rendering.Core.vtkMapper.newInstance();
mapper.setInputConnection(reader.getOutputPort());

// ---
// actor
// ---
export var actor              = vtk.Rendering.Core.vtkActor.newInstance();
actor.setMapper(mapper);

// ---
// add the actor to the render
// ---
renderer.addActor(actor);
