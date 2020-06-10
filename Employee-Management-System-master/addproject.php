<?php
session_start();
if(!$_SESSION['name'])
{
header("location:login.php");
}

include 'conn.php';

if(isset($_POST['done']))
{
	$pname  = $_POST['pname'];
	$pid = $_POST['pid'];
	$manager = $_POST['manager'];


	$q="INSERT INTO `project`(`project_name`, `project id`, `manager`) VALUES ('$pname','$pid','$manager')";

$query = mysqli_query($conn,$q);

}
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
	background-image:linear-gradient(rgba(71,71,71,0.7),rgba(71,71,71,0.7)),url("img/a2.jpg");

  	
	background-size: cover;
  	background-position: center;
  	
	height: 100vh;
}


</style>

</head>
<body>
<br>


<div>
<h2 class="text-white"><center><font size="10">Employee Management System</font></center></h2>

</div><br>

<div class="col-lg-6 m-auto">

	<form method="post">
		<br><div>
			<div class="card-header bg-dark">
				<h1 class="text-white text-center">Insert Project Details</h1>
			</div><br>


			<label class="text-warning">Project Name</label>
			<input type="text" name="pname" class="form-control" required><br>

			<label class="text-warning">Project Id</label>
			<input type="text" name="pid" class="form-control" required pattern="[0-9]{1,15}"
        title="this field accepts only numbers"><br>

			<label class="text-warning">Manager</label>
			<input type="text" name="manager" class="form-control" required><br>
          <div  class="row m-auto">
			<div class="col-md-5"><button class="btn btn-success col-lg-12" name="done">Add</button>
			</div>
			<div class="col-md-5"><a href="display.php"><input type="button" name="" value="Back to records" class="btn btn-danger col-lg-12"></a></div>
			</div>
		   </div>
		   		 		<table class="table table-stripped table-hover table-bordered">
				<tr class="text-white">
					<th><h5>Project Name</h5></th>
					<th><h5>Project Id</h5></th>
					<th><h5>Manager Name</h5></th>
				</tr>   
			<br>
<?php
include 'conn.php';


$q="select * from project";

$query = mysqli_query($conn,$q);

while ($res = mysqli_fetch_array($query)) {
?>

			<tr class="text-white">
				<th><?php echo $res['project_name'] ?></th>
				<th><?php echo $res['project id'] ?></th>
				<th><?php echo $res['manager'] ?></th>
			</tr>
<?php }
?>	
	</form>	
</div>


		</table>
</script>
</body>
</html>
