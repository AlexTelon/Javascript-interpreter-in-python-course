while(true)
{
  console.log("a")
  break;
}

while(false)
{
  console.log("c")
  break;
}

for(;;)
{
  console.log("b")
  break;
}

for(;true;)
{
  console.log("e");
  break;
}

var i = 0

while(true)
{
  i = i + 1;
  if(i < 2)
  {
    continue;
  }
  console.log("d")
  if(i == 5)
  {
    break;
  }
}

for(;; i = i + 1)
{
  if(i < 6)
    continue;
  console.log("f")
  if(i < 7)
    break;
}


