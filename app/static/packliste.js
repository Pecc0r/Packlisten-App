function handleFormSubmit(event) {
  event.preventDefault();

let cbs = document.querySelectorAll("input[type=checkbox]");
let res = [...cbs].filter(a => a.checked).map(b => b.name);

let slidervalue = document.getElementById("slider").value

console.log (res)
fetch(`${window.origin}/api/packliste`,
  { method: 'POST',
  body: JSON.stringify({"checkboxes":res, "slider":slidervalue}),
  headers: new Headers({"content-type":"application/json"})})
  .then(response => response.json())
  .then(data => render(data));

  /*
  const data = new FormData(event.target);

  const formJSON = Object.fromEntries(data.entries());

  // for multi-selects, we need special handling
  const results = document.querySelector('.results pre');
  results.innerText = JSON.stringify(formJSON, null, 2);
  */
}

const form = document.querySelector('.contact-form');
form.addEventListener('submit', handleFormSubmit);

let volumeSlider = document.getElementById('name');

function setzeVolumeAnzeige(wert) {
    document.getElementById('output').value = wert;
}
volumeSlider.addEventListener('input', function(event) {
   setzeVolumeAnzeige(event.target.value);
});
setzeVolumeAnzeige(volumeSlider.value);

function render (content) {
  document.getElementById("content").innerHTML =`
   <h1> Packliste </h1>
   <div class="columns">
      <div class="col">
      <p>${key}</p>
         <div class="item">
            <input type="checkbox" name="${val}"/>
            <label for="${val}">${val}</label>
         </div>
      </div>
   </div>
   ${JSON.stringify(content)}
   </p>
  `
}

let cbs = document.querySelectorAll("input[type=checkbox]");
let res = [...cbs].filter(a => a.checked).map(b => b.name);
