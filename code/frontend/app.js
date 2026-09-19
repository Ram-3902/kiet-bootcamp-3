// app.js — the whole frontend. Plain JavaScript, no library.
// The ONLY line to change if your backend runs somewhere else:
const BACKEND = "http://localhost:8080";

// The pieces of the page this script touches.
const collegeSelect = document.getElementById("college");
const locationInput = document.getElementById("location");
const resultsBody = document.getElementById("results");
const countLine = document.getElementById("count");
const logBox = document.getElementById("log");
const banner = document.getElementById("banner");

// Every request goes through here. It does what  curl -i URL  does:
// send a GET, then write method, URL, status and time to the Request log.
function call(path, whenDone) {
  const url = BACKEND + path;
  const started = Date.now();
  fetch(url)
    .then(function (response) {
      const ms = Date.now() - started;
      logBox.textContent = "GET " + url + "  ->  " + response.status + "  (" + ms + " ms)\n" + logBox.textContent;
      return response.json();          // the body, parsed from JSON into an object
    })
    .then(whenDone)
    .catch(function (error) {
      // The browser refused or the server is down. The Console tab has the real reason.
      logBox.textContent = "GET " + url + "  ->  FAILED (see the Console tab)\n" + logBox.textContent;
      banner.hidden = false;
      console.error(error);
    });
}

// Puts a {"count": n, "students": [...]} answer into the table.
function showStudents(data) {
  resultsBody.innerHTML = "";
  if (data.error) {                    // a 400 from the server: {"error": "..."}
    countLine.textContent = "error: " + data.error;
    return;
  }
  data.students.forEach(function (student) {
    const row = document.createElement("tr");
    [student.student_name, student.inter_college, student.inter_city].forEach(function (value) {
      const cell = document.createElement("td");
      cell.textContent = value;
      row.appendChild(cell);
    });
    resultsBody.appendChild(row);
  });
  countLine.textContent = data.count + " rows";
}

// On page load. Same as:   curl localhost:8080/colleges
function loadColleges() {
  call("/colleges", function (data) {
    banner.hidden = true;
    collegeSelect.innerHTML = "";
    data.colleges.forEach(function (name) {
      const option = document.createElement("option");
      option.value = name;
      option.textContent = name;
      collegeSelect.appendChild(option);
    });
  });
}

// Button 1. Same as:   curl "localhost:8080/students?college=Narayana+Junior+College"
// (curl needed + for the spaces; the browser writes %20. The server reads both as a space.)
document.getElementById("byCollege").onclick = function () {
  call("/students?college=" + encodeURIComponent(collegeSelect.value), showStudents);
};

// Button 2. Same as:   curl "localhost:8080/students/by-location?location=Vijayawada"
document.getElementById("byLocation").onclick = function () {
  call("/students/by-location?location=" + encodeURIComponent(locationInput.value), showStudents);
};

// Button 3. Same as:   curl "localhost:8080/students/search?college=Narayana+Junior+College&location=Vijayawada"
document.getElementById("search").onclick = function () {
  call("/students/search?college=" + encodeURIComponent(collegeSelect.value) +
       "&location=" + encodeURIComponent(locationInput.value), showStudents);
};

loadColleges();
