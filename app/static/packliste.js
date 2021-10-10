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

let volumeSlider = document.getElementById('slider');

function setzeVolumeAnzeige(wert) {
    document.getElementById('output').value = wert;
}
volumeSlider.addEventListener('input', function(event) {
   setzeVolumeAnzeige(event.target.value);
});
setzeVolumeAnzeige(volumeSlider.value);

function render (c) {
  let val="foo"
  document.getElementById("content").innerHTML =`
   <div class="packliste">
     <h1> Packliste </h1>
     <div class="columns" style="  display: flex;
       justify-content: space-between;">

      <!-- Infrastruktur --!>
      <div class="col">
      <p>Infrastruktur</p>

        ${c["Infrastruktur"].map(val => `
          <div class="item">
            <label for="${val}">
              <input type="checkbox" name="${val}" id="${val}"/>
             ${val}
            </label>
          </div>
          `).join("")
       }
      </div>


      <!-- Kleidung --!>
      <div class="col">
        <p>Kleidung</p>
        ${c["Kleidung"].map(val => `
          <div class="item">
            <label for="${val}">
              <input type="checkbox" name="${val}" id="${val}"/>
              ${val}
            </label>
          </div>
          `).join("")
       }
      </div>

      <!-- Kochen --!>
      <div class="col">
        <p>Kochen</p>
        ${c["Kochen"].map(val => `
          <div class="item">
            <label for="${val}">
              <input type="checkbox" name="${val}" id="${val}"/>
              ${val}
            </label>
          </div>
          `).join("")
       }
      </div>

      <!-- Hygiene --!>
      <div class="col">
        <p>Hygiene</p>
        ${c["Hygiene"].map(val => `
          <div class="item">
            <label for="${val}">
              <input type="checkbox" name="${val}" id="${val}"/>
              ${val}
            </label>
          </div>
          `).join("")
       }
      </div>
    </div>
  </div>
  `

  document.body.classList.remove("bg1")
  document.body.classList.add("bg2")

}

let cbs = document.querySelectorAll("input[type=checkbox]");
let res = [...cbs].filter(a => a.checked).map(b => b.name);

document.body.classList.add("bg1");
