const menu = document.getElementById("hamburger");
const navigation = document.querySelector("nav > div:nth-child(1)");

menu.onclick = function () {
  menu.classList.toggle("active");
  navigation.classList.toggle("max-md:opacity-0");
  navigation.classList.toggle("max-md:opacity-100");
};
