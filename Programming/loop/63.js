function gateCheck(age) {
  if (age < 18) {
    console.log("Go home, kid");
  } else if (age < 25) {
    console.log("Entry allowed, normal pass");
  } else {
    console.log("VIP entry");
  }
}

gateCheck(16); // Go home, kid
gateCheck(20); // Entry allowed, normal pass
gateCheck(30); // VIP entry
