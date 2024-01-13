function confirmBox()
{
	var message=confirm("Are you sure you want to proceed?");
	if(message==true)
	{
		return true;
	}
	else{
		return false;
	}
}
