document.addEventListener("DOMContentLoaded", function() {
  var shareButton = document.getElementById("shareButton");
  var closeButton = document.getElementById("closeButton");
  var notificationBox = document.getElementById("myModal");
  var notificationContent = document.getElementById("linkInput");

  shareButton.addEventListener("click", function() {
      // Get the team names and prediction results
      var team1 = "{{ team1 }}";
      var team2 = "{{ team2 }}";
      var predictionResults = "{{ predictionResults }}";

      // Update the notification box content
      var message = "Team 1: " + team1 + "\n" +
                    "Team 2: " + team2 + "\n" +
                    "Prediction Results: " + predictionResults;
      notificationContent.value = message;

      // Show the notification box
      notificationBox.style.display = "block";
  });

  closeButton.addEventListener("click", function() {
      // Hide the notification box
      notificationBox.style.display = "none";
  });
});
