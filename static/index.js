let led = true
function home(e) {
    fetch( `/main`)
  .then( response => {
    console.log(response);
  })
}
function other(e) {
    fetch( `/other`)
  .then( response => {
    console.log(response);
  })
}
function shutdown(e) {
    fetch( `/shutdown`)
  .then( response => {
    console.log(response);
  })
}

function Led(e) {
  fetch( `/main/toggle`)
  .then( response => {
      console.log(response);
  })
  let nf = document.getElementById("col");
  if (led) {
    if(!nf.classList.contains("bg-green-400")){
      nf.classList.remove("bg-rose-500");
      nf.classList.add("bg-green-400");
      nf.classList.add("animate-ping");
    }
  }
  else {
    if(!nf.classList.contains("bg-rose-500")){
      nf.classList.remove("bg-green-400");
      nf.classList.remove("animate-ping");
      nf.classList.add("bg-rose-500");
    }
  }
  led = !led;
}