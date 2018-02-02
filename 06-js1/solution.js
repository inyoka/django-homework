var firstname = prompt("Enter your firstname :")
var secondname = prompt("Enter your surname :")
var age = prompt("Enter your age :")
var height = prompt("What is your height : ")
var pet = prompt("Enter your pet name :")
alert("Thank you for your information!")


if (firstname[0]==secondname[0] && age>20 && age<30 && height>=170 && pet.slice(-1)=="y"){
  console.log("Welcome comrade.");
}else {
  console.log("Nothing to see here.");
}
