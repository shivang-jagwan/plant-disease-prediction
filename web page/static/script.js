document.addEventListener('DOMContentLoaded', function () {
    const pages = document.querySelectorAll('.page');
    const navLinks = document.querySelectorAll('.nav-link');

    // Navigation logic
    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const targetPage = this.getAttribute('data-page');
            pages.forEach(page => page.classList.remove('active'));
            document.getElementById(targetPage).classList.add('active');
            navLinks.forEach(link => link.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // Form submission
    document.getElementById('upload-form').addEventListener('submit', async function (e) {
        e.preventDefault();
        const fileInput = document.getElementById('file-input');
        const formData = new FormData();
        formData.append('file', fileInput.files[0]);
    
        try {
            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
    
            if (result.error) {
                alert(result.error);
            } else {
                document.getElementById('uploaded-image').src = result.image_url;
                document.getElementById('disease-result').innerHTML = `
                    🌿 <strong>पौधा (Plant):</strong> ${result.plant_name_hin} (${result.plant_name_eng}) <br>
                    ⚠️ <strong>रोग (Disease):</strong> ${result.disease_hin} (${result.disease_eng}) <br>
                    📊 <strong>विश्वसनीयता (Confidence):</strong> ${result.confidence.toFixed(2)}%
                `;
    
                // Show the recommendation button
                document.getElementById('recommendation-button').style.display = 'block';
                document.getElementById('recommendation-button').onclick = async () => {
                    try {
                        const recommendationResponse = await fetch('/get_recommendation', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify({ 
                                plant_name_eng: result.plant_name_eng, 
                                disease_eng: result.disease_eng 
                            }),
                        });
    
                        const recommendationData = await recommendationResponse.json();
                        document.getElementById('recommendation-text').innerText = recommendationData.recommendation;
                        document.getElementById('recommendation-section').style.display = 'block';
                    } catch (error) {
                        alert('Error fetching recommendation: ' + error.message);
                    }
                };
            }
        } catch (error) {
            alert('Error: ' + error.message);
        }
    });
});
