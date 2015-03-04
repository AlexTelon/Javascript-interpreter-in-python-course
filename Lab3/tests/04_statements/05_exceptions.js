try {
  console.log("a")
  throw "Failed";
  console.log("b")
} catch(err)
{
  console.log(err)
}

try {
  console.log("c")
  throw "Failed";
  console.log("d")
} catch(err)
{
  console.log(err)
} finally {
  console.log("e")
}

try {
  console.log("f")
  console.log("g")
} catch(err)
{
  console.log(err)
} finally {
  console.log("h")
}


