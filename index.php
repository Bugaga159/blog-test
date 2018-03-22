<?php 

$connect = mysqli_connect('127.0.0.1','root','','blog-test');

if ($connect == false) {
	echo "Соединение отсутствует с БД!</br>";
	echo mysqli_connect_error();
	exit();
}
$result = mysqli_query($connect,'SELECT * FROM `articles_categories`');
?>

<ul>
	<?php	

while (($res = mysqli_fetch_assoc($result))) {
	echo "<li>". $res['catigorie'] . "</li>" ;
}
?>

</ul>
<?php
mysqli_close($connect);
?>