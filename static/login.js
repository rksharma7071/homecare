function validateForm() {
    var username = document.forms["signup"]["username"].value;
    var email = document.forms["signup"]["email"].value;
    var password = document.forms["signup"]["password"].value;
    
    if (username == "") {
      alert("Username must be filled out");
      return false;
    }
    
    if (email == "") {
      alert("Email must be filled out");
      return false;
    }
    
    if (password == "") {
      alert("Password must be filled out");
      return false;
    }
  }
  