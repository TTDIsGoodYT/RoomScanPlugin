fetch("/progress.json?cache=" + Date.now())
  .then(response => {
    if (!response.ok) {
      throw new Error("Could not load progress.json");
    }

    return response.json();
  })
  .then(data => {

  document.querySelectorAll(".room-progress").forEach(element => {
    element.textContent =
      `${data.rooms} / ${data.total} Rooms — ${data.percent.toFixed(1)}% Complete`;
  });

  const bar = document.querySelector(".progress-fill");

if (bar instanceof HTMLElement) {
  bar.style.width = `${data.percent}%`;
}

})