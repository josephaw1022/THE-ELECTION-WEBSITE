<!DOCTYPE html>
<html lang = "en">
<body>
  <?php
  $name = $_GET["names"];
  $email  = $_GET["emails"];?>

  Welcome  <?php printf("%s",$name); ?> <br />
  Your email address is: <?php printf("%s",$email); ?>

</body>
</html>
