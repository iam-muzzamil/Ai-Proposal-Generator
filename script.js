<<<<<<< HEAD
// Wait for the page to load fully before running JavaScript
document.addEventListener("DOMContentLoaded", function () {
  // Grab the form element by its ID
  const form = document.getElementById("proposalForm");

  // Grab the output section & proposal result area
  const outputSection = document.getElementById("outputSection");
  const proposalResult = document.getElementById("proposalResult");

  // Add event listener when the form is submitted
  form.addEventListener("submit", function (e) {
    // Stop the default form action (page reload)
    e.preventDefault();

    // Show the output section and set temporary message
    outputSection.classList.remove("hidden");
    proposalResult.textContent = "⏳ Generating proposal...";

    // Collect user input values from the form
    const name = document.getElementById("name").value;
    const skills = document.getElementById("skills").value;
    const platform = document.getElementById("platform").value;
    const tone = document.getElementById("tone").value;
    const job = document.getElementById("job").value;

    // Prepare the data object to send to backend
    const data = {
      name: name,
      skills: skills,
      platform: platform,
      tone: tone,
      job: job,
    };

    // Send the data to the Flask backend using fetch
    fetch("http://localhost:5000/generate", {
      method: "POST", // HTTP method POST
      headers: {
        "Content-Type": "application/json", // We're sending JSON
      },
      body: JSON.stringify(data), // Convert JS object to JSON
    })
      .then((response) => response.json()) // Parse JSON response
      .then((result) => {
        // Display the generated proposal returned by Flask
        proposalResult.textContent = result.proposal;
      })
      .catch((error) => {
        // Handle errors like network or server issues
        proposalResult.textContent =
          "❌ Error generating proposal. Please try again.";
        console.error("Error:", error);
      });
  });
});
=======
// Wait for the page to load fully before running JavaScript
document.addEventListener("DOMContentLoaded", function () {
  // Grab the form element by its ID
  const form = document.getElementById("proposalForm");

  // Grab the output section & proposal result area
  const outputSection = document.getElementById("outputSection");
  const proposalResult = document.getElementById("proposalResult");

  // Add event listener when the form is submitted
  form.addEventListener("submit", function (e) {
    // Stop the default form action (page reload)
    e.preventDefault();

    // Show the output section and set temporary message
    outputSection.classList.remove("hidden");
    proposalResult.textContent = "⏳ Generating proposal...";

    // Collect user input values from the form
    const name = document.getElementById("name").value;
    const skills = document.getElementById("skills").value;
    const platform = document.getElementById("platform").value;
    const tone = document.getElementById("tone").value;
    const job = document.getElementById("job").value;

    // Prepare the data object to send to backend
    const data = {
      name: name,
      skills: skills,
      platform: platform,
      tone: tone,
      job: job,
    };

    // Send the data to the Flask backend using fetch
    fetch("http://localhost:5000/generate", {
      method: "POST", // HTTP method POST
      headers: {
        "Content-Type": "application/json", // We're sending JSON
      },
      body: JSON.stringify(data), // Convert JS object to JSON
    })
      .then((response) => response.json()) // Parse JSON response
      .then((result) => {
        // Display the generated proposal returned by Flask
        proposalResult.textContent = result.proposal;
      })
      .catch((error) => {
        // Handle errors like network or server issues
        proposalResult.textContent =
          "❌ Error generating proposal. Please try again.";
        console.error("Error:", error);
      });
  });
});
>>>>>>> 74fc07ea5efd77b7835f9ab7be4c66cca8cec472
