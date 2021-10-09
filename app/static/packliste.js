function handleFormSubmit(event) {
  event.preventDefault();

  const data = new FormData(event.target);

  const formJSON = Object.fromEntries(data.entries());

  // for multi-selects, we need special handling

  const results = document.querySelector('.results pre');
  results.innerText = JSON.stringify(formJSON, null, 2);
}

let volumeSlider = document.getElementById('name');

function setzeVolumeAnzeige(wert) {
    document.getElementById('output').value = wert;
}
volumeSlider.addEventListener('input', function(event) {
   setzeVolumeAnzeige(event.target.value);
});
setzeVolumeAnzeige(volumeSlider.value);



const form = document.querySelector('.contact-form');
form.addEventListener('submit', handleFormSubmit);
