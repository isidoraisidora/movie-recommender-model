document.getElementById('predictBtn').addEventListener('click', async () => {
    const movieInput = document.getElementById('movieInput');
    const resultsContainer = document.getElementById('resultsContainer');
    const loader = document.getElementById('loading');
    const movieName = movieInput.value;

    if (!movieName) {
        alert("Please enter a movie name!");
        return;
    }

    // Show loading spinner and clear previous results
    loader.classList.remove('d-none');
    resultsContainer.innerHTML = '';

    try {
        // Added 'predict' to the end of the URL
        const response = await fetch('https://movie-recommender-model-fzfv.onrender.com/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt: movieName })
        });

        const data = await response.json();
        loader.classList.add('d-none');

        // Check if there are recommendations
        // Check if there are recommendations
        if (data.recommendations) {
            data.recommendations.forEach(movie => {
                const card = `
                    <div class="col-12 col-lg-8 mx-auto mb-3"> <div class="card shadow-sm">
                            <div class="card-body">
                                <h5 class="card-title text-primary mb-0">${movie}</h5>
                            </div>
                        </div>
                    </div>
                `;
                resultsContainer.innerHTML += card;
            });
        }
    } catch (error) {
        console.error("Connection Error:", error);
        loader.classList.add('d-none');
        alert("Could not connect to the backend. Make sure Uvicorn is running!");
    }
});