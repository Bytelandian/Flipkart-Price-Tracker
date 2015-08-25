<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" href="css/main.css" />
<style>
td,th{
	padding:10px;
}
th{
	border-bottom:1px dashed black;
}
.details{
	position:absolute;
	width:50%;
	right:50px;
	height:400px;
	top:50px;
	
}

</style>
<title>Untitled Document</title>
</head>
<?php
include('connection.php');
if(isset($_GET['name'])){
	$name =$_GET['name'];
	$query = "select * from records where product_name='$name'";
	$result = mysqli_query($dbc,$query) OR die('error counting number of records');
	$i=0;
	$id = array(); $name = array(); $description = array();$url = array();$price = array();$rating = array();$num_rating = array();
	$num_review = array();$date = array();$time = array();
	while($row = mysqli_fetch_array($result)){
		$i=$i+1;
		$id[$i]=$row['id'];
		$name[$i]=$row['product_name'];
		$description[$i]=$row['description'];
		$url[$i]=$row['product_url'];
		$price[$i]=$row['price'];
		$rating[$i]=$row['rating'];
		
		$num_review[$i]=$row['num_review'];
		$date[$i]=$row['date'];
		$time[$i]=$row['time'];
	}
}

?>
<body>

<div id="bodysub" class="bodysub">
<div id="topheader" class="topheader">
<h1 style="text-align:center;">Single result  :: <?php echo $_GET['name']?></h1>
</div>

<div style="position:absolute; min-height:400px; width:100%; top:150px; background-color:#fff;">
<p style="margin:40px; ">Price Comparison along the crawling:</p>
<table style="margin:40px; border:1px solid black;"><tr><th>Price</th><th>Date</th><th>Time</th></tr>
<?php
for($k=1;$k<=$i;$k=$k+1){
?>
<tr><td><?php echo $price[$k];?></td>
	<td><?php echo $date[$k];?></td>
    <td><?php echo $time[$k];?></td>
    </tr>    
<?php
	
}
?>
</table>
<a style="margin-left:40px;" href="index.php">Back</a>

<div id="details" class="details">
<p style="padding-left:20px; margin-top:-10px;"><b>Description of Product:</b> <?php echo $description[1];?></p>
<p style="padding-left:20px;"><b>Product Rating: </b><?php echo $rating[1]?></p>

<p style="padding-left:20px;"><b>Number of reviews:</b><?php echo $num_review[1]?></p>
<p style="padding-left:20px;"><b>Link: <a href="<?php echo $url[1];?>"><?php echo $url[1];?>
</div>
</div>
</body>
</html>
