function func_true()
{
  console.log("func_true has been called");
  return true;
}

function func_false()
{
  console.log("func_false has been called");
  return false;
}

if(func_false() && func_true())
{
} else {
  console.log("For false and true, only func_false has been called");
}

if(func_true() && func_false())
{
} else {
  console.log("For true and false, only func_false has been called");
}

if(func_true() || func_false())
{
  console.log("For true or false, only func_true has been called");
}

if(func_false() || func_true())
{
  console.log("For false or true, func_false and func_true has been called");
}
