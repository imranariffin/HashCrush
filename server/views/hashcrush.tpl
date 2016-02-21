<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>backend</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
    <script src="bower_components/bootstrap/dist/js/bootstrap.js"></script>

    <link href="bower_components/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <link href="static/css/main.css" rel="stylesheet" media="screen">

</head>
<body>

    <div class="container">
        <div class="jumbotron">
        <form action="/get-hashcrush" method="POST">
          <input type="text" style="width:50%" placeholder="put your tweets here" name="tweet">
          <p>
            <input type="submit" value="Hash Crush" id="MyButton">
          </p>
        </form>
        </div>
    </div>
    
</body>
</html>

