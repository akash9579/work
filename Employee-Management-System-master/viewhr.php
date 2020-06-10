<?php
session_start();
if(!$_SESSION['name'])
{
header("location:login.php");
}

error_reporting(0);
include 'conn.php';

$id = $_GET['id'];
$name = $_POST['name'];
$age = $_POST['age'];
$salary = $_POST['salary'];
$qualification = $_POST['qualification'];
$dob = date("Y-m-d",strtotime($_POST['dob']));
$doj = date("Y-m-d",strtotime($_POST['doj']));
$date_of_birth = $dob;
$date_of_join = $doj;


$day = $_POST['day'];
$hours = $_POST['t_in1'];
$hours1 = $_POST['t_out1'];
$timein = "$hours";
$timeout = "$hours1";
$date = date("y-m-d");

$q="select * from employee where id = $id";
$query = mysqli_query($conn,$q);
$res=mysqli_fetch_array($query);

$q2="INSERT INTO time(id,name, day, time_in, time_out,date) VALUES ('$id','$name','$day','$timein','$timeout','$date')";

if (isset($_POST['add'])) 
{
	
	mysqli_query($conn,$q2);
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
	background-image:linear-gradient(rgba(71,71,71,0.9),rgba(71,71,71,0.9)),url("img/a4.jpg");

  	
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
				<h1 class="text-white text-center">Displaying Employee Details</h1>
			</div><br>

			<input type="hidden" name="id" value="<?php echo $res['id']; ?>">
			<label class="text-warning">Name</label>
			<input type="text" name="name" class="form-control" value="<?php echo $res['name']; ?>" readonly><br>

			<label class="text-warning">age</label>
			<input type="text" name="age" class="form-control" value="<?php echo $res['age']; ?>" readonly><br>

			<label class="text-warning">salary</label>
			<input type="text" name="salary" class="form-control" value="<?php echo $res['salary']; ?>" readonly><br>

			<label class="text-warning">qualification</label>
			<input type="text" name="qualification" class="form-control" value="<?php echo $res['qualification']; ?>" readonly><br>

            <label class="text-warning">date of Birth</label>
			<input type="text" name="dob" class="form-control"
			value="<?php echo $res['date_of_birth']; ?>" readonly><br>

			<label class="text-warning">date of Joining</label>
			<input type="text" name="doj" class="form-control" value="<?php echo $res['date_of_join']; ?>" readonly><br>


            
            <div class="row">
			<div class="col-md-3"><button class="btn btn-success" name="Back">Back</button></div>
		    </div>
		   <script type="text/javascript">

</script>
		<?php
        
        if(isset($_POST['Back']))
        {
            header("location:displayhr.php");
        }

if (isset($_POST['view'])) {

$_SESSION['id'] = $id;
	header("location:attendance.php");

}
		?>
		</div>
		
	</form>
</div>

</body>
</html>