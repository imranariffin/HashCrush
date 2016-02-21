<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>backend</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min\
.js"></script>
    <script src="bower_components/bootstrap/dist/js/bootstrap.js"></script>

    <link href="bower_components/bootstrap/dist/css/bootstrap.min.css" rel="sty\
lesheet" media="screen">
    <link href="static/css/main.css" rel="stylesheet" media="screen">

</head>
<body>
<table>
    <ul>
  % for item in basket:
    <li>{{item}}</li>
  % end
</ul>
</table>

</body>
</html>