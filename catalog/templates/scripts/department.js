function togglePositions(departmentId) {
    const positionsList = document.getElementById(`positions-${departmentId}`);
    const triangle = document.getElementById(`triangle-${departmentId}`);
    if (positionsList.style.display === "none") {
        positionsList.style.display = "block";
        triangle.textContent = '▲';  // Change to solid triangle
    } else {
        positionsList.style.display = "none";
        triangle.textContent = '▼';  // Change back to hollow triangle
    }
}