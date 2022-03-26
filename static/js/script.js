$(function() {
  var buttons = document.getElementsByName("myBtn");
  var buttonsCount = buttons.length;
  for (var i = 0; i <= buttonsCount; i += 1) {
    buttons[i].onclick = function(e) {
       var email = document.getElementById('email').value;
       if ($.trim(email).length == 0) {
            alert("Please enter valid email address!");
            return;
       }
       var myId = this.id;
       var btn = document.getElementById("btn "+myId);
       var jsonCall = $.getJSON('/initiate_vote/'+myId+'/'+email,
            function(data) {
                var jsonData = JSON.parse(jsonCall.responseText);
                if (jsonData.statusCode === 400) alert("You have already voted");
                else {
                    btn.innerHTML = "You have voted!"
                    btn.disabled = true;
                    document.getElementById("txt "+myId).innerHTML = jsonData.message+" people have said Yes!";
                }
       });
       return false;
    };
  }
});