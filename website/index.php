<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Untitled Document</title>
<link rel="stylesheet" type="text/css" href="css/main.css" />
</head>
<?php
include('connection.php');
$query="select distinct product_name from records";
$result = mysqli_query($dbc,$query) OR die('error counting number of records');
$num = mysqli_num_rows($result);
$num_single=10;
$cur_page=1;
if(isset($_GET['num_single'])){
	$num_single=$_GET['num_single'];
}
if(isset($_GET['cur_page'])){
	$cur_page=$_GET['cur_page'];
}

$q = "select * from records group by product_name";
$result1 = mysqli_query($dbc,$q) OR die('error counting number of records11');
$i=0;
$id = array(); $name = array(); $para = array();$description = array();$url = array();$price = array();$rating = array();
$num_review = array();$date = array();$time = array();
while($row = mysqli_fetch_array($result1)){
	$i=$i+1;
	$id[$i]=$row['id'];
	$name[$i]=$row['product_name'];
	$para[$i]=str_replace("&","%26",$name[$i]);
	$description[$i]=substr($row['description'],0,100)."...";
	$url[$i]=substr($row['product_url'],0,60)."...";
	$price[$i]=$row['price'];
	$rating[$i]=$row['rating'];
	$num_review[$i]=$row['num_review'];
	$date[$i]=$row['date'];
	$time[$i]=$row['time'];
}
?>
<body>
<div id="bodysub" class="bodysub">
<div id="topheader" class="topheader">
<h1 style="text-align:center;">Crawled Results</h1>
</div>

<div id="test" class="test">
<h2 style="text-align:center; padding-top:20px;">Total Number of recorded products: <?php echo $num?></h2>
<?php
$top = $i*350 +130;
?>
<div id="machine" class="machine" style="position:absolute; top:250px; width:100%; background-color:white; border-radius:10px; left:0px; height:<?php echo $top?>px;">
<?php

if($i>0){
	$size=-200;
for($k=1;$k<=$i;$k=$k+1){
	$size=$size+350;
	?>
    <div style="position:absolute; width:90%; left:50px; border:1px solid black; top:<?php echo $size?>px; height:300px;">
    <a href="single.php?name=<?php echo $para[$k]?>" style="text-decoration:none;"><h2 style=" text-align:center; color:#555">Name :: <?php echo $name[$k];?></h2></a>
    <p style="padding-left:20px;">Description :: <?php echo $description[$k];?></p>
    <p style="padding-left:20px;">Url of product ::	<?php echo $url[$k];?></p>
    <p style="padding-left:20px;">Rating ::	<?php echo $rating[$k];?></p>
    <p style="padding-left:20px;">Number of reviews :: <?php echo $num_review[$k]?></p>
    <h3 style=" text-align:center">Price :: Rs. <?php echo $price[$k]?> /-</h3>
    
    
    </div>
    <?php
}
}
?>

</div>
</div>
</div>

</body>
</html>
