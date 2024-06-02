const filterButtons = document.querySelectorAll("#filter-buttons button");
const filterablesContainer = document.querySelectorAll("#filterables");
const filterables = document.querySelectorAll("#filterables .relative");

console.log(filterablesContainer);

const filterItems = (e) => {
  document.querySelector("button.active").classList.remove("active");
  e.target.classList.add("active");

  filterables.forEach((item) => {
    item.classList.add("hide");

    if (
      item.dataset.set === e.target.dataset.set ||
      e.target.dataset.set === "all"
    ) {
      item.classList.remove("hide");
    }
  });

  if (e.target.dataset.set != "all") {
    filterablesContainer[0].classList.remove("lg:grid-cols-2");
    filterablesContainer[0].classList.add("lg:grid-cols-1");
  } else {
    filterablesContainer[0].classList.add("lg:grid-cols-2");
    filterablesContainer[0].classList.remove("lg:grid-cols-1");
  }
};

filterButtons.forEach((button) =>
  button.addEventListener("click", filterItems)
);
