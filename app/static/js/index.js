const dayTheme = "rgb(238, 238, 238)";
const nightTheme = "rgba(28, 43, 45, 0.9)";
const lightMoon = document.querySelector(".theme__link--night");
const darkMoon = document.querySelector(".theme__link--day");
const baseTemplate = document.querySelector(".base");
const arrowIcon = document.querySelector(".chem-image");
const elementCarousel = document.querySelector(".chem__carousel");
const dailyTable = document.querySelector("table");
const dailyData = document.querySelectorAll("td");
const tempToggleDay = document.querySelectorAll(".button--day");
const tempToggleNight = document.querySelectorAll(".button--night");
const atomIcon = document.querySelector(".home-atom");
const flaskIcon = document.querySelector(".home-flask");
const industryGrid = document.querySelectorAll(".industry-column");
const anchorTags = document.querySelectorAll("a");
const alchemyIcon = document.querySelector(".head__image");
const dropdownOneStatic = document.querySelector(".dropdown-1__select");
const dropdownTwoStatic = document.querySelector(".dropdown-2__select");
const dropdownOneOptions = document.querySelector(".dropdown-1__options");
const dropdownTwoOptions = document.querySelector(".dropdown-2__options");
const dropdownOneInput = document.querySelector(".dropdown-1__search input");
const dropdownTwoInput = document.querySelector(".dropdown-2__search input");
let dropdownOneSelected = document.querySelector(".dropdown-1__selected");
let dropdownTwoSelected = document.querySelector(".dropdown-2__selected");

document.addEventListener("DOMContentLoaded", () => {
  if (localStorage.getItem("theme")) {
    let saved_theme = localStorage.getItem("theme");
    if (saved_theme === dayTheme) {
      goDayTheme();
    } else if (saved_theme === nightTheme) {
      goNightTheme();
    }
  }
});

const toggleTheme = () => {
  const backdropComputedColor = getComputedStyle(
    baseTemplate,
    null
  ).getPropertyValue("background-color");
  console.log(
    `theme is toggling => current theme is ${
      backdropComputedColor === dayTheme ? "day" : "night"
    }, new theme is going to be ${
      backdropComputedColor === dayTheme ? "night" : "day"
    }`
  );
  if (backdropComputedColor === dayTheme) {
    goNightTheme();
  } else if (backdropComputedColor === nightTheme) {
    goDayTheme();
  }
};

const goDayTheme = () => {
  document.body.style.color = "black";
  if (elementCarousel) {
    let chemSquares = document.querySelectorAll(".carousel__content");

    if (chemSquares.length > 0) {
      for (let i of chemSquares) {
        i.classList.remove("carousel__content--night");
        i.classList.add("carousel__content--day");
      }
    }
  }

  for (let a of anchorTags) {
    a.style.color = "black";
  }

  if (dailyTable) {
    dailyTable.style.border = "1px solid black";
    for (let td of dailyData) {
      td.style.border = "1px solid black";
    }
  }

  darkMoon.style.display = "";
  lightMoon.style.display = "none";

  if (flaskIcon) {
    flaskIcon.style.backgroundColor = "";
    flaskIcon.style.padding = "";
    flaskIcon.style.borderRadius = "";
  }

  if (industryGrid) {
    for (let grid of industryGrid) {
      grid.style.backgroundColor = "rgba(255, 255, 255, 0.8)";
    }
  }

  if (tempToggleDay.length) {
    tempToggleDay.forEach((item) => {
      item.style.display = "";
    });
  }

  if (tempToggleNight.length) {
    tempToggleNight.forEach((item) => {
      item.style.display = "none";
    });
  }

  if (alchemyIcon) {
    alchemyIcon.style.backgroundColor = "";
    alchemyIcon.style.borderRadius = "";
  }

  if (atomIcon) {
    atomIcon.style.backgroundColor = "";
    atomIcon.style.padding = "";
    atomIcon.style.borderRadius = "";
  }

  if (arrowIcon) {
    arrowIcon.style.backgroundColor = "";
    arrowIcon.style.padding = "";
    arrowIcon.style.borderRadius = "";
  }

  if (dropdownOneStatic && dropdownTwoStatic) {
    dropdownOneOptions.style.backgroundColor = "rgba(0,0,0,0.6)";
    dropdownOneOptions.style.color = "white";
    dropdownTwoOptions.style.backgroundColor = "rgba(0,0,0,0.6)";
    dropdownTwoOptions.style.color = "white";
  }

  baseTemplate.style.backgroundColor = dayTheme;

  window.localStorage.clear();
  window.localStorage.setItem("theme", dayTheme);
};

const goNightTheme = () => {
  document.body.style.color = "white";

  for (let a of anchorTags) {
    a.style.color = "white";
  }

  if (dailyTable) {
    dailyTable.style.border = "1px solid white";
    for (let td of dailyData) {
      td.style.border = "1px solid white";
    }
  }

  lightMoon.style.display = "";
  darkMoon.style.display = "none";

  if (flaskIcon) {
    flaskIcon.style.backgroundColor = "white";
    flaskIcon.style.padding = "2rem";
    flaskIcon.style.borderRadius = "25%";
  }

  if (industryGrid) {
    for (let grid of industryGrid) {
      grid.style.backgroundColor = "rgba(255, 255, 255, 0.2)";
    }
  }

  if (tempToggleNight.length) {
    tempToggleNight.forEach((item) => {
      item.style.display = "";
    });
  }

  if (tempToggleDay.length) {
    tempToggleDay.forEach((item) => {
      item.style.display = "none";
    });
  }

  if (alchemyIcon) {
    alchemyIcon.style.backgroundColor = "white";
    alchemyIcon.style.borderRadius = "50%";
  }

  if (elementCarousel) {
    let chemSquares = document.querySelectorAll(".carousel__content");
    for (let i of chemSquares) {
      i.classList.remove("carousel__content--day");
      i.classList.add("carousel__content--night");
    }
  }

  if (atomIcon) {
    atomIcon.style.backgroundColor = "white";
    atomIcon.style.padding = "2rem";
    atomIcon.style.borderRadius = "50%";
  }

  if (dropdownOneSelected && dropdownTwoSelected) {
    dropdownOneSelected.style.backgroundColor = "white";
    dropdownOneSelected.style.color = "black";
    dropdownTwoSelected.style.color = "black";
    dropdownTwoSelected.style.backgroundColor = "white";
  }

  if (arrowIcon) {
    arrowIcon.style.backgroundColor = "white";
    arrowIcon.style.padding = "0 1rem";
    arrowIcon.style.borderRadius = "15%";
  }

  if (dropdownOneStatic && dropdownTwoStatic) {
    dropdownOneOptions.style.backgroundColor = "rgba(238, 238, 238, 0.9)";
    dropdownOneOptions.style.color = "black";
    dropdownTwoOptions.style.backgroundColor = "rgba(238, 238, 238, 0.9)";
    dropdownTwoOptions.style.color = "black";
    dropdownOneInput.style.border = "8px solid rgba(238, 238, 238, 0.9)";
    dropdownTwoInput.style.border = "8px solid rgba(238, 238, 238, 0.9)";
  }

  baseTemplate.style.backgroundColor = nightTheme;
  window.localStorage.clear();
  window.localStorage.setItem("theme", nightTheme);
};

darkMoon.addEventListener("click", toggleTheme);
lightMoon.addEventListener("click", toggleTheme);

