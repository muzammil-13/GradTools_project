// script.js
const activityElement = document.getElementById('activity');
const getActivityButton = document.getElementById('getActivity');

function getRandomActivity() {
    fetch('https://www.boredapi.com/api/activity')
        .then(response => response.json())
        .then(data => {
            activityElement.textContent = data.activity;
        })
        .catch(error => {
            console.error('Error fetching activity:', error);
        });
}

getActivityButton.addEventListener('click', getRandomActivity);
