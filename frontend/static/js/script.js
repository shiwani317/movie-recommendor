async function getRecommendations() {
    const movie = document.getElementById("movie").value;

    const response = await fetch("/recommend", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ movie })
    });

    const data = await response.json();

    const results = document.getElementById("results");
    results.innerHTML = "";

    data.forEach(movie => {
        const li = document.createElement("li");
        li.textContent = movie;
        results.appendChild(li);
    });
}
