<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>backend</title>
    <script type='text/javascript' src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
    <!-- // <script src="bower_components/bootstrap/dist/js/bootstrap.js"></script> -->
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">
    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>

    <script type="text/javascript">
        // (function () {
        //     $('#postform').submit(function (e) {
        //         e.preventDefault();
        //         dataString = $('#postform').serialize();
        //         console.log(dataString);
        //         $.ajax({
        //             url : '/get-hashcrush',
        //             type : 'POST',
        //             data : dataString,
        //             dataType : 'json',
        //             success : function (response) {
        //                 console.log(response);

        //                 // $('#list').
        //             },
        //             error : function (err) {
        //                 console.log(err);
        //             }
        //         });
        //     });
        // });
    </script>

</head>
<body>
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">
      </a>
      <p class="navbar-text navbar-right">Hash Crush</a></p>
    </div>
  </div>
</nav>
    <div class="container">


        <p text-align="center">
            
        </p>

        <div class="jumbotron">
        <form id="postform" method="POST" action="/hashcrushtable">
            <div class="input-group">
              <span class="input-group-addon" id="basic-addon1">#</span>
              <input type="text" name="tweet" class="form-control" placeholder="put your tweets here" aria-describedby="basic-addon1">
            </div>
          <!-- <input type="text" style="width:50%" placeholder="put your tweets here" name="tweet"> -->
          <p>
            <input type="submit" value="Hash Crush" id="MyButton">
          </p>
        </form>
        </div>
    </div>

<div class="list-group" id="list">
    <button type="button" class="list-group-item"></button>
</div>
    
</body>
</html>

