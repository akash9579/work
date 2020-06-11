<?php
session_start();
include 'conn.php';
if(!$_SESSION['name'])
{
  header("location:login.php");
 }

$id = $_SESSION['id'];
$q="select * from time1 where id=$id";
$p="SELECT sum(`work_h`) FROM `time1` WHERE id=$id";

$query = mysqli_query($conn,$q);
$res = mysqli_fetch_array($query);

$query1 = mysqli_query($conn,$p);
$res1 = mysqli_fetch_array($query1);



?>
<!DOCTYPE html>
<html>
<head>
	<title></title>
		<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">

<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>

<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.bundle.min.js" integrity="sha384-u/bQvRA/1bobcXlcEYpsEdFVK/vJs3+T+nXLsBYJthmdBuavHvAW6UsmqO2Gd/F9" crossorigin="anonymous"></script>


<style>
body{
	background-image:linear-gradient(rgba(00,0,0,0.7),rgba(0,0,0,0.7)),url("img/a7.jpg");

  	
	background-size: cover;
  	background-position: center;
  	
	height: 100vh;
}


</style>



</head>
<body>
<br>
<div>
<h2 class="text-white"><center><font size="10">Sallery Details</font></center></h2>

</div><br>
</br>

<div class="container">
	<div class="col-lg-12">

        </div>
		<table class="table table-stripped table-hover table-bordered">
			<tr class="text-dark">


				<th><h5 class="text-white">day</h5></th>
				<th><h5 class="text-white">date</h5></th>
				<th><h5 class="text-white">time in</h5></th>
				<th><h5 class="text-white">time out</h5></th>
				<th><h5 class="text-white">working hours</h5></th>

			</tr>

			<?php
include 'conn.php';


$q="select * from time1 where id=$id";

$query = mysqli_query($conn,$q);

while ($res = mysqli_fetch_array($query)) {
?>

			<tr class="text-white">

				<th><?php echo $res['day'] ?></th>
				<th><?php echo $res['date'] ?></th>
				<th><?php echo $res['In_time'] ?></th>
				<th><?php echo $res['out_time'] ?></th>
				<th><?php echo $res['work_h'] ?></th>
			</tr>
<?php }
?>

		</table>
			</br>
			<label class="text-warning">Total Sallery</label>
			<input type="text" name="age" class="form-control" value="<?php echo $res1['sum(`work_h`)']*1250 ?>" readonly><br>

		<div class="col-lg-12">
			<div class="row">

		<a href="viewemp1.php?id=<?php echo $id; ?>" class="col-lg-3"><button class="btn btn-success col-lg-4" name="logout">back</button></a>
		<a href="logout.php" class="col-lg-3"><button class="btn btn-success col-lg-4" name="logout">logout</button></a>
			</div>
        </div>
	</div>


</body>
</html>
