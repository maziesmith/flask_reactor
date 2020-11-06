const dayThemeColor = "rgb(238, 238, 238)";
const nightThemeColor = "rgba(28, 43, 45, 0.9)";
const lightMoonImage = document.getElementById("nightTheme__Image");
const darkMoonImage = document.getElementById("dayTheme__Image");
const baseTemplateBlock = document.getElementById("base__Template");
const chemTemplateArrowImage = document.getElementById("chem__Image");
const chemTemplateCarousel = document.getElementById("chem__CarouselSection");
const dailyTemplatetable = document.querySelector("table");
const dailyTemplateData = document.querySelectorAll("td");
const dailyTemplateDayToggler = document.querySelectorAll(".daily-button-day");
const dailyTemplateNightToggler = document.querySelectorAll(
  ".daily-button-night"
);
const homeTemplateAtomImage = document.getElementById("home__Atom");
const homeTemplateFlaskImage = document.getElementById("home__Image");
const industryTemplateGridItems = document.querySelectorAll(".grid-item");
const globalAnchorTags = document.querySelectorAll("a");
const reactorTemplateImage = document.getElementById("alchemy__Image");
const reactorTemplateDropdownOne = document.querySelector(
  ".reactor__SelectBox1"
);
const reactorTemplateDropdownTwo = document.querySelector(
  ".reactor__SelectBox2"
);
const reactorTemplateOptionsOne = document.querySelector(
  ".reactor__OptionsContainer1"
);
const reactorTemplateOptionsTwo = document.querySelector(
  ".reactor__OptionsContainer2"
);
const reactorTemplateInputOne = document.querySelector(
  ".reactor__SearchBox1 input"
);
const reactorTemplateInputTwo = document.querySelector(
  ".reactor__SearchBox2 input"
);
let reactorTemplateSelectedOne = document.querySelector(".reactor__Selected1");
let reactorTemplateSelectedTwo = document.querySelector(".reactor__Selected2");

document.addEventListener("DOMContentLoaded", () => {
  if (localStorage.getItem("theme")) {
    let saved_theme = localStorage.getItem("theme");
    if (saved_theme === dayThemeColor) {
      goDayTheme();
    } else if (saved_theme === nightThemeColor) {
      goNightTheme();
    }
  }
});

const toggleTheme = () => {
  const backdropComputedColor = getComputedStyle(
    baseTemplateBlock,
    null
  ).getPropertyValue("background-color");
  console.log(
    `theme is toggling => current theme is ${
      backdropComputedColor === dayThemeColor ? "day" : "night"
    }, new theme is going to be ${
      backdropComputedColor === dayThemeColor ? "night" : "day"
    }`
  );
  if (backdropComputedColor === dayThemeColor) {
    goNightTheme();
  } else if (backdropComputedColor === nightThemeColor) {
    goDayTheme();
  }
};

const goDayTheme = () => {
  document.body.style.color = "black";

  if (chemTemplateCarousel) {
    let chemSquares = document.querySelectorAll(".chem__CarouselNightContent");
    if (chemSquares.length > 0) {
      for (let i of chemSquares) {
        i.classList.remove("chem__CarouselNightContent");
        i.classList.add("chem__CarouselDayContent");
      }
    }
  }

  for (let a of globalAnchorTags) {
    a.style.color = "black";
  }

  if (dailyTemplatetable) {
    dailyTemplatetable.style.border = "1px solid black";
    for (let td of dailyTemplateData) {
      td.style.border = "1px solid black";
    }
  }

  darkMoonImage.style.display = "";
  lightMoonImage.style.display = "none";

  if (homeTemplateFlaskImage) {
    homeTemplateFlaskImage.style.backgroundColor = "";
    homeTemplateFlaskImage.style.padding = "";
    homeTemplateFlaskImage.style.borderRadius = "";
  }

  if (industryTemplateGridItems) {
    for (let grid of industryTemplateGridItems) {
      grid.style.backgroundColor = "rgba(255, 255, 255, 0.8)";
    }
  }

  if (dailyTemplateDayToggler.length) {
    dailyTemplateDayToggler.forEach((item) => {
      item.style.display = "";
    });
  }

  if (dailyTemplateNightToggler.length) {
    dailyTemplateNightToggler.forEach((item) => {
      item.style.display = "none";
    });
  }

  if (reactorTemplateImage) {
    reactorTemplateImage.style.backgroundColor = "";
    reactorTemplateImage.style.borderRadius = "";
  }

  if (homeTemplateAtomImage) {
    homeTemplateAtomImage.style.backgroundColor = "";
    homeTemplateAtomImage.style.padding = "";
    homeTemplateAtomImage.style.borderRadius = "";
  }

  if (chemTemplateArrowImage) {
    chemTemplateArrowImage.style.backgroundColor = "";
    chemTemplateArrowImage.style.padding = "";
    chemTemplateArrowImage.style.borderRadius = "";
  }

  if (reactorTemplateDropdownOne && reactorTemplateDropdownTwo) {
    reactorTemplateOptionsOne.style.backgroundColor = "rgba(0,0,0,0.6)";
    reactorTemplateOptionsOne.style.color = "white";
    reactorTemplateOptionsTwo.style.backgroundColor = "rgba(0,0,0,0.6)";
    reactorTemplateOptionsTwo.style.color = "white";
  }

  baseTemplateBlock.style.backgroundColor = dayThemeColor;

  window.localStorage.clear();
  window.localStorage.setItem("theme", dayThemeColor);
};

const goNightTheme = () => {
  document.body.style.color = "white";

  for (let a of globalAnchorTags) {
    a.style.color = "white";
  }

  if (dailyTemplatetable) {
    dailyTemplatetable.style.border = "1px solid white";
    for (let td of dailyTemplateData) {
      td.style.border = "1px solid white";
    }
  }

  lightMoonImage.style.display = "";
  darkMoonImage.style.display = "none";

  if (homeTemplateFlaskImage) {
    homeTemplateFlaskImage.style.backgroundColor = "white";
    homeTemplateFlaskImage.style.padding = "2rem";
    homeTemplateFlaskImage.style.borderRadius = "25%";
  }

  if (industryTemplateGridItems) {
    for (let grid of industryTemplateGridItems) {
      grid.style.backgroundColor = "rgba(255, 255, 255, 0.2)";
    }
  }

  if (dailyTemplateNightToggler.length) {
    dailyTemplateNightToggler.forEach((item) => {
      item.style.display = "";
    });
  }

  if (dailyTemplateDayToggler.length) {
    dailyTemplateDayToggler.forEach((item) => {
      item.style.display = "none";
    });
  }

  if (reactorTemplateImage) {
    reactorTemplateImage.style.backgroundColor = "white";
    reactorTemplateImage.style.borderRadius = "50%";
  }

  if (chemTemplateCarousel) {
    let chemSquares = document.querySelectorAll(".chem__CarouselDayContent");
    for (let i of chemSquares) {
      i.classList.remove("chem__CarouselDayContent");
      i.classList.add("chem__CarouselNightContent");
    }
  }

  if (homeTemplateAtomImage) {
    homeTemplateAtomImage.style.backgroundColor = "white";
    homeTemplateAtomImage.style.padding = "2rem";
    homeTemplateAtomImage.style.borderRadius = "50%";
  }

  if (reactorTemplateSelectedOne && reactorTemplateSelectedTwo) {
    reactorTemplateSelectedOne.style.backgroundColor = "white";
    reactorTemplateSelectedOne.style.color = "black";
    reactorTemplateSelectedTwo.style.color = "black";
    reactorTemplateSelectedTwo.style.backgroundColor = "white";
  }

  if (chemTemplateArrowImage) {
    chemTemplateArrowImage.style.backgroundColor = "white";
    chemTemplateArrowImage.style.padding = "0 1rem";
    chemTemplateArrowImage.style.borderRadius = "15%";
  }

  if (reactorTemplateDropdownOne && reactorTemplateDropdownTwo) {
    reactorTemplateOptionsOne.style.backgroundColor =
      "rgba(238, 238, 238, 0.9)";
    reactorTemplateOptionsOne.style.color = "black";
    reactorTemplateOptionsTwo.style.backgroundColor =
      "rgba(238, 238, 238, 0.9)";
    reactorTemplateOptionsTwo.style.color = "black";
    reactorTemplateInputOne.style.border = "8px solid rgba(238, 238, 238, 0.9)";
    reactorTemplateInputTwo.style.border = "8px solid rgba(238, 238, 238, 0.9)";
  }

  baseTemplateBlock.style.backgroundColor = nightThemeColor;
  window.localStorage.clear();
  window.localStorage.setItem("theme", nightThemeColor);
};

darkMoonImage.addEventListener("click", toggleTheme);
lightMoonImage.addEventListener("click", toggleTheme);
