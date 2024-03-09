const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');
const startButton = document.getElementById('startButton');
const output = document.getElementById('output');

// Function to start listening
function startListening() {
    output.textContent = 'Listening...';
    
    const recognition = new webkitSpeechRecognition() || new SpeechRecognition();
    recognition.lang = 'en-US';
    
    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        searchInput.value = transcript;
        output.textContent = 'You said: ' + transcript;
    };
    
    recognition.start();
}

startButton.addEventListener('click', startListening);

// Function to handle search
function handleSearch() {
    const searchTerm = searchInput.value.trim();
    
    if (searchTerm !== '') {
        output.textContent = 'Searching for: ' + searchTerm;
        // Your code to perform search action with searchTerm
    } else {
        output.textContent = 'Please enter a search term.';
    }
}

searchButton.addEventListener('click', handleSearch);

// Pressing Enter in search input triggers search
searchInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        handleSearch();
    }
});
