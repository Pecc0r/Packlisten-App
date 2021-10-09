fetch(`${window.origin}/api/packliste`,
  { method: 'POST',
  body: JSON.stringify({}),
  headers: new Headers({"content-type":"application/json"})}).then(response => response.json()).then(data => console.log(data));
