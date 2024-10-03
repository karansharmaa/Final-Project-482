// Function to update the current date and time
function updateDateTime() {
    const d = new Date();
    const dateString = d.toLocaleDateString(); // Get current date
    const timeString = d.toLocaleTimeString(); // Get current time
    
    document.getElementById("date").innerHTML = "Today's date is: " + dateString;
    document.getElementById("time").innerHTML = "Current time: " + timeString;
}

// Update the clock every second
setInterval(updateDateTime, 999.99);

// Initial call to display the date and time immediately when the page loads
updateDateTime();
