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
$day1 = $_POST['day1'];
$month1 = $_POST['month1'];
$year1 = $_POST['year1'];
$date1 = "$day1-$month1-$year1";


$day = $_POST['day'];
$hours = $_POST['t_in1'];
$hours1 = $_POST['t_out1'];
$work_h = $_POST['wh'];
$timein = "$hours";
$timeout = "$hours1";
$date = date("y-m-d");
$work_hr = "$work_h";


$q="select * from employee where id = $id";
$query = mysqli_query($conn,$q);
$res=mysqli_fetch_array($query);


$q2="INSERT INTO `time1`(`id`, `name`, `date`, `day`, `In_time`, `out_time`, `work_h`) VALUES ('$id','$name','$date1','$day','$timein','$timeout','$work_hr')";

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

			<label class="text-warning">Date</label>
			<div class="row">
			<div class="col-md-3"><input type="text" name="day1" class="form-control" placeholder="date" 
        	title="this field accepts only numbers  and two characters"></div>-

			<div class="col-md-3"><input type="text" name="month1" class="form-control" placeholder="month" 
        	title="this field accepts only numbers  and two characters"></div>-

			<div class="col-md-3"><input type="text" name="year1" class="form-control" placeholder="year" 
        	title="this field accepts only numbers  and 4 characters"></div><br>
            </div> <br>

			<label class="text-warning">day</label>
			<select name="day" class="form-control">
				<option>monday</option>
				<option>tuesday</option>
				<option>wednesday</option>
				<option>thursday</option>
				<option>friday</option>
				<option>saturday</option>
			</select><br>

			<label class="text-warning">time in</label>
			<div class="row">
			<div class="col-md-3"><input type="text" name="t_in1" class="form-control" value="0" required pattern="[0-9]{1,2}"
        title="this field accepts only numbers  and two characters"></div>
			<div class="col-md-3"></div>
			<div class="col-md-3"></div>
		    </div>
			<br>

			<label class="text-warning">time out</label>
			<div class="row">
			<div class="col-md-3"><input type="text" name="t_out1" class="form-control" value="0" required pattern="[0-9]{1,2}"
        title="this field accepts only numbers  and two characters"></div>
			<div class="col-md-3"></div>
			<div class="col-md-3"></div>
		    </div><br>

		    <label class="text-warning">working_hours</label>
			<div class="row">
			<div class="col-md-3"><input type="text" name="wh" class="form-control" value="0" required pattern="[0-9]{1,2}"
        title="this field accepts only numbers  and two characters"></div>
			<div class="col-md-3"></div>
			<div class="col-md-3"></div>
		    </div><br>
            
            <div class="row">
			<div class="col-md-3"><button class="btn btn-success" name="Back">Logout</button></div>
			<div class="col-md-3"><button class="btn btn-success" name="add">add attendence</button></div>
			<div class="col-md-3"><button class="btn btn-success" name="view">sallery</button></div>
		    </div>
		   <script type="text/javascript">

</script>
		<?php
        
        if(isset($_POST['Back']))
        {
            header("location:login.php");
        }

if (isset($_POST['view'])) {

$_SESSION['id'] = $id;
	header("location:sallery.php");

}
		?>
		</div>
		
	</form>
</div>

</body>
</html>