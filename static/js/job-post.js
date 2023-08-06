const salaryRange = document.getElementById("salaryRange");
const rangeValue = document.getElementById("rangeValue");

salaryRange.addEventListener("input", function () {
  rangeValue.textContent = salaryRange.value;
});

const jobForm = document.getElementById("jobForm");
const postedJobs = document.getElementById("postedJobs");

jobForm.addEventListener("submit", function (event) {
  event.preventDefault();

  const jobTitle = document.getElementById("jobTitle").value;
  const jobDescription = document.getElementById("jobDescription").value;
  const jobMode = document.getElementById("jobMode").value;

  const jobCard = document.createElement("div");
  jobCard.classList.add("job-card");
  jobCard.innerHTML = `
    <h2>${jobTitle}</h2>
    <p>${jobDescription}</p>
    <p>Job Mode: ${jobMode}</p>
    <p>Salary Range: $${salaryRange.value}</p>
    <h3>Required Skills:</h3>
    ${getSkillsHTML()}
  `;

  postedJobs.appendChild(jobCard);

  // Clear the form fields and skills
  jobForm.reset();
  clearSkills();
});

function getSkillsHTML() {
  const skillInputs = document.querySelectorAll(".skill-input");
  let skillsHTML = "<ul>";

  skillInputs.forEach((skillInput) => {
    const skillName = skillInput.querySelector(".skill-name").value;
    const skillWeight = skillInput.querySelector(".skill-weight").value;
    skillsHTML += `<li>${skillName} (Weight: ${skillWeight})</li>`;
  });

  skillsHTML += "</ul>";
  return skillsHTML;
}

function addSkillInput() {
  const skillsSection = document.getElementById("skillsSection");
  const skillInputDiv = document.createElement("div");
  skillInputDiv.className = "skill-input";
  
  const skillNameInput = document.createElement("input");
  skillNameInput.type = "text";
  skillNameInput.className = "skill-name";
  skillNameInput.placeholder = "Enter Skill Name";
  
  const skillWeightInput = document.createElement("select");
  skillWeightInput.className = "skill-weight";
  for (let i = 1; i <= 5; i++) {
    const option = document.createElement("option");
    option.value = i;
    option.textContent = i;
    skillWeightInput.appendChild(option);
  }
  
  const removeButton = document.createElement("button");
  removeButton.className = "remove-button";
  removeButton.textContent = "X";
  removeButton.onclick = function() {
    skillInputDiv.remove();
  };
  
  skillInputDiv.appendChild(skillNameInput);
  skillInputDiv.appendChild(skillWeightInput);
  skillInputDiv.appendChild(removeButton);
  
  skillsSection.appendChild(skillInputDiv);
}

// Add a default skill input when the page loads
window.onload = function() {
  addSkillInput();
};

function clearSkills() {
  const skillsSection = document.getElementById("skillsSection");
  skillsSection.innerHTML = ""; // Clear skills section
}

// $(function() {

//   // Initiate Slider
//   $('#slider-range').slider({
//     range: true,
//     min: 0,
//     max: 10000,
//     step: 10,
//     values: [45000, 75000]
//   });

//   // Move the range wrapper into the generated divs
//   $('.ui-slider-range').append($('.range-wrapper'));

//   // Apply initial values to the range container
//   $('.range').html('<span class="range-value"><sup>$</sup>' + $('#slider-range').slider("values", 0).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider"></span><span class="range-value"><sup>$</sup>' + $("#slider-range").slider("values", 1).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');

//   // Show the gears on press of the handles
//   $('.ui-slider-handle, .ui-slider-range').on('mousedown', function() {
//     $('.gear-large').addClass('active');
//   });

//   // Hide the gears when the mouse is released
//   // Done on document just incase the user hovers off of the handle
//   $(document).on('mouseup', function() {
//     if ($('.gear-large').hasClass('active')) {
//       $('.gear-large').removeClass('active');
//     }
//   });

//   // Rotate the gears
//   var gearOneAngle = 0,
//   gearTwoAngle = 0,
//   rangeWidth = $('.ui-slider-range').css('width');

// $('.gear-one').css('transform', 'rotate(' + gearOneAngle + 'deg)');
// $('.gear-two').css('transform', 'rotate(' + gearTwoAngle + 'deg)');

// $('#slider-range').slider({
//   slide: function(event, ui) {

//     // Update the range container values upon sliding
//     $('.range').html('<span class="range-value"><sup>$</sup>' + ui.values[0].toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider"></span><span class="range-value"><sup>$</sup>' + ui.values[1].toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');

//     // Get old value
//     var previousVal = parseInt($(this).data('value'));

//     // Save new value
//     $(this).data({
//       'value': parseInt(ui.value)
//     });

//     // Figure out which handle is being used
//     if (ui.values[0] == ui.value) {

//       // Left handle
//       if (previousVal > parseInt(ui.value)) {
//         // value decreased
//         gearOneAngle -= 7;
//         $('.gear-one').css('transform', 'rotate(' + gearOneAngle + 'deg)');
//       } else {
//         // value increased
//         gearOneAngle += 7;
//         $('.gear-one').css('transform', 'rotate(' + gearOneAngle + 'deg)');
//       }

//     } else {

//       // Right handle
//       if (previousVal > parseInt(ui.value)) {
//         // value decreased
//         gearOneAngle -= 7;
//         $('.gear-two').css('transform', 'rotate(' + gearOneAngle + 'deg)');
//       } else {
//         // value increased
//         gearOneAngle += 7;
//         $('.gear-two').css('transform', 'rotate(' + gearOneAngle + 'deg)');
//       }

//     }

//     if (ui.values[1] === 110000) {
//       if (!$('.range-alert').hasClass('active')) {
//         $('.range-alert').addClass('active');
//       }
//     } else {
//       if ($('.range-alert').hasClass('active')) {
//         $('.range-alert').removeClass('active');
//       }
//     }
//   }
// });

// // Prevent the range container from moving the slider
// $('.range, .range-alert').on('mousedown', function(event) {
//   event.stopPropagation();
// });

// });
