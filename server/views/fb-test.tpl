<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>backend</title>

    <script src="bower_components/jquery/dist/jquery.js"></script>
    <script src="bower_components/bootstrap/dist/js/bootstrap.js"></script>

  <script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js"></script>
  <link rel="stylesheet" href="style.css" />
  <title>jQuery Example</title>
  <script>
    $(document).ready(function() {
      $.ajaxSetup({ cache: true });
      $.getScript('//connect.facebook.net/en_US/sdk.js', function(){
        FB.init({
          appId: '1686788251598601',
          version: 'v2.5' // or v2.0, v2.1, v2.2, v2.3
        });     
        // $('#loginbutton,#feedbutton').removeAttr('disabled');
        FB.getLoginStatus(updateStatusCallback);
      });
    });
  </script>
    <link href="bower_components/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <link href="static/css/main.css" rel="stylesheet" media="screen">

</head>
<body>
<script>
  // window.fbAsyncInit = function() {
  //   FB.init({
  //     appId      : '1686788251598601',
  //     xfbml      : true,
  //     version    : 'v2.5'
  //   });
  // };

  // (function(d, s, id){
  //    var js, fjs = d.getElementsByTagName(s)[0];
  //    if (d.getElementById(id)) {return;}
  //    js = d.createElement(s); js.id = id;
  //    js.src = "//connect.facebook.net/en_US/sdk.js";
  //    fjs.parentNode.insertBefore(js, fjs);
  //  }(document, 'script', 'facebook-jssdk'));
</script>

    <div
      class="fb-like"
      data-share="true"
      data-width="450"
      data-show-faces="true">Like?
    </div>    
    <div class="container">
        <div class="header">
            <ul class="nav nav-pills pull-right">
                <li class="active"><a ng-href="#">Home</a></li>
                <li><a ng-href="#">About</a></li>
                <li><a ng-href="#">Contact</a></li>
            </ul>
            <h3 class="text-muted">backend</h3>
        </div>

        <div class="jumbotron">
            <h1>'Allo, 'Allo!</h1>
            <p class="lead">
                <img src="static/img/yeoman.png" alt="I'm Yeoman"><br>
                Always a pleasure scaffolding your apps.
            </p>
            <p><a class="btn btn-lg btn-success" ng-href="#">Splendid!<span class="glyphicon glyphicon-ok"></span></a></p>
        </div>
    </div>
</body>
</html>