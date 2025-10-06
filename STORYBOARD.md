# SOP Guide Studio · Storyboard



## 🏇 Doing

- Add rich text (new URL, bold, italic, …) (add link and upload file is left, also you may add variable from here) 
- highlight the add button after clicking on it, on click again it should be cancelled

- show actual values insted of variables on view guide
- make on single select, it automatically jumps to the next one in the wizard
- change the title name of the browser tab, make it sop - medical
- fix is editable field, i have thought of making all fields an indicator to check if need to set dirty or not, because when we create a new link in the rich text, while typing the link it will highlight the save button
- on enter click it should go next

- have map link in the preview 

- select does not render pictures, not sure how will you do it, either remove it from select and input, or keep it in both
- mandate starter label while editing
- group right label to have matching fields together
- make selected or active starter and active step on the url instead of variable to be able to share it
- required should not exist, probably only in the single select, and maybe in the input but i am not sure


---

## ✅ Done
- Fix the logic in the previous option in the wizard screen, specially when having options.
-  Setting to combine some header buttons
-  download button
-  Delete Starter
-  we must have start point in our graph, wether it's an indicator or a step
-  required is checkbox
-  after loading, ensure all data are correct like starter and types of steps and all position are correct
-  remove right panel in the edit starter, and put the add +Before +after Duplicate and delete
-  ADD Button to Save Changes
-  only one save button shown in the edit mode, lighted when form is dirty, discard changes when go to preview
-  New SOP
-  CTRL + S to save
- Dark mode  
- Add to GitHub  
- Download picture  
- Set starter node 
- Ability to view only current step + step before + step after (during development)  
- Remove description if not necessary  
- Remove image from select  
- On remove: focus when changing the ID not working 100%   
- On import ask if everything will be overrided, if yes then override it and import it
- Take full screen, shrink side panels, make more space for the map  
- Allow user to view current progress in a dialog (before exporting)  
- Add new starter from outside  
- Add Save and Cancel buttons in the map editor  
- On Cancel/Import/Export, add discard prompt (same for map edit)  
- Fix crash when: enter **Edit** → click on **Starter** → click on **Preview**  
- Download HTML exactly as what we have without the need to upload it everytime 
- fix on select step in the edit mode
- Hand tool to move the map, cursor to select  
- delete starter
- Scroll up and down in the graph
- for multi select it should have onle one next
- move starters around to make them ordered as i need


---

## ⏳ Not Done
- Add, delete, duplicate and delete should be well functioning
- import single starter to this current starter
- make the user to choose the start of the starter step (if so we need to update the ensureMandatory function to say if it has already startId, then don't update it)
- when right panel is changed like required checkbox, it should render the preview wizard
- const viewState = { starterIdx: 0, answers: {}, selectedStepId: 0, stepIdx: 0 }; here is should only rely on selectedStepId or stepIdx
- selectedIdx or selectedStepId should reflect in both wizard and edit
- don't render while typing in title or body, rerender on blur:
bodyEl.addEventListener('blur', () => {
  renderViewStep();
});

- Undo and redo    
- on click enter should go the next step on view guide
- Search capability  
- Zoom on cursor (not general zoom probably on shift + scroll) 
- View picture (small, then maximize)  
- ability to morge two files
- Fix the image size so it dose not change. in the wizard
- Interactive steps on the map
- Stop warning discard changes option for the user
- Redirect to step using URL  
- Auto complete (e.g. when typing `role.` or showing variables)  
- One step with multiple pictures and multiple inputs  


