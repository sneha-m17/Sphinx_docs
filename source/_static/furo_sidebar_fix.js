document.addEventListener("DOMContentLoaded", function () {
  const sections = document.querySelectorAll(".sidebar-tree > li.toctree-l1");
  sections.forEach((el) => el.classList.add("current"));
});
