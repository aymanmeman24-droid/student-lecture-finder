function findLectures() {

    const input = document.getElementById("enrollmentInput");
    const message = document.getElementById("message");

    const enrollment = input.value.trim().toUpperCase();

    // Empty input check
    if (enrollment === "") {
        message.textContent = "⚠️ Please enter your enrollment number.";
        message.style.color = "#dc2626";
        return;
    }

    // Button loading
    const button = document.querySelector(".find-btn");
    button.textContent = "🔄 Finding...";
    button.disabled = true;

    // Check enrollment from backend
    fetch(`/api/lectures/${encodeURIComponent(enrollment)}`)
        .then(response => response.json())
        .then(data => {

            if (data.success) {

                // Save enrollment for other pages
                localStorage.setItem("enrollment", enrollment);

                message.textContent = "✅ Lectures found!";
                message.style.color = "#16a34a";

                // Open today's lecture page
                setTimeout(() => {
                    window.location.href = "/today.html";
                }, 300);

            } else {

                message.textContent = "❌ Enrollment number not found.";
                message.style.color = "#dc2626";

                button.textContent = "🔍 Find My Lectures";
                button.disabled = false;
            }

        })
        .catch(error => {

            console.error("Error:", error);

            message.textContent = "⚠️ Server connection problem.";
            message.style.color = "#dc2626";

            button.textContent = "🔍 Find My Lectures";
            button.disabled = false;
        });
}


// Press Enter to search
document.addEventListener("DOMContentLoaded", function () {

    const input = document.getElementById("enrollmentInput");

    if (input) {
        input.addEventListener("keydown", function (event) {

            if (event.key === "Enter") {
                findLectures();
            }

        });
    }

});