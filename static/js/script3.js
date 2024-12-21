const filterBtn = document.querySelector(".filter-btn");
const closeFilterBtn = document.querySelector(".close-filter i");

filterBtn?.addEventListener("click", function () {
  document.querySelector(".filter-layout")?.classList.remove("hide");
  document
    .querySelector(".form-filter")
    ?.classList.add("form-filter-animation");
});

closeFilterBtn?.addEventListener("click", function () {
  document.querySelector(".filter-layout")?.classList.add("hide");
  document
    .querySelector(".form-filter")
    ?.classList.remove("form-filter-animation");
});

document
  .querySelector(".filter-layout")
  ?.addEventListener("click", function (event) {
    const formFilter = document.querySelector(".form-filter");
    if (formFilter && !formFilter.contains(event.target)) {
      document.querySelector(".filter-layout")?.classList.add("hide");
      document
        .querySelector(".form-filter")
        ?.classList.remove("form-filter-animation");
    }
  });



      document.addEventListener("DOMContentLoaded", function () {
        // Initialize the first slider by its ID or class
        new Splide("#slider1", {
          type: "loop",
          perPage: 1,
          perMove: 1,
          pagination: true,
        }).mount();

        // Initialize the second slider with a different set of options
        new Splide("#slider2", {
          rewind: true,
          pagination: false,
          autoWidth: true,
          autoplay: true,
          perPage: 3,
        }).mount();
      });

      window.addEventListener("scroll", function () {
        const navbar = document.querySelector(".main-nav");
        console.log(navbar);
        if (window.scrollY > 50) {
          navbar.classList.add("navbar-shadow");
        } else {
          navbar.classList.remove("navbar-shadow");
        }
      });

     let currentIndex = 0;
const images = [];

document.addEventListener('DOMContentLoaded', function () {
    // Gather all images for the popup slider
    const imageElements = document.querySelectorAll('.slider-img');
    imageElements.forEach((img, index) => {
        images.push(img.src);
        img.addEventListener('click', () => {
            openModal(index);
        });
    });
});

// Function to open the modal and set the image
function openModal(index) {
    currentIndex = index;
    const modal = document.getElementById('modal');
    const popupImage = document.getElementById('popup-image');

    popupImage.src = images[currentIndex];
    modal.style.display = 'flex';
}

// Function to change the slide
function changeSlide(direction) {
    currentIndex += direction;

    // Wrap around logic
    if (currentIndex < 0) {
        currentIndex = images.length - 1;
    } else if (currentIndex >= images.length) {
        currentIndex = 0;
    }

    const popupImage = document.getElementById('popup-image');
    popupImage.src = images[currentIndex];
}

// Function to close the modal
function closeModal() {
    const modal = document.getElementById('modal');
    modal.style.display = 'none';
}

