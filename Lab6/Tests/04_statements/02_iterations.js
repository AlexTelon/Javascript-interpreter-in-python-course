var i = 0
do
{
  console.log(i)
  i = i + 1
} while(i < 0)

while(i < 1)
{
  console.log("a")
  i = i + 1  
}

i = 0

while(i < 1)
{
  console.log("e")
  i = i + 1  
}

for(i = 0;i < 2; i = i + 1)
{
  console.log("b")
}

for(;false;)
{
  console.log("f")
  break;
}

for(;i < 4; i = i + 1)
{
  console.log("c")
}

for(var j = 0; j < 2; j = j + 1)
{
  console.log(j)
}

