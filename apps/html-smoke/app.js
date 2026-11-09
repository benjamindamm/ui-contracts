const count = document.querySelector("#count");
const increment = document.querySelector("#increment");
let value = 0;

increment.addEventListener("click", () => {
  value += 1;
  count.textContent = String(value);
});
