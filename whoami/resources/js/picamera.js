//var imageNr = 0; // Serial number of current image
//var finished = new Array(); // References to img objects which have finished downloading
//var paused = false;

//var imageNr2 = 0; // Serial number of current image
//var finished2 = new Array(); // References to img objects which have finished downloading
//var paused2 = false;

var imageNr = [0, 0, 0, 0];
var paused = [false, false, false, false];
var finished = new Array(4);
for(var i=0; i<finished.length; i++) {
  finished[i] = new Array();
}

function createImageLayer1() {
  var img1 = new Image();
  img1.style.position = "absolute";
  img1.style.zIndex = -1;
  img1.onload = imageOnload1;
  img1.onclick = imageOnclick1;
  img1.width = 320;
  img1.height = 240;
  img1.src = "http://10.1.4.207:8080/?action=snapshot&n=" + (++imageNr[0]);
  var webcam1 = document.getElementById("mycam");
  webcam1.insertBefore(img1, webcam1.firstChild);
}

function createImageLayer2() {
  var img2 = new Image();
  img2.style.position = "absolute";
  img2.style.zIndex = -1;
  img2.onload = imageOnload2;
  img2.onclick = imageOnclick2;
  img2.width = 320;
  img2.height = 240;
  img2.src = "http://10.1.4.206:8080/?action=snapshot&n=" + (++imageNr[1]);
  var webcam2 = document.getElementById("frontcam");
  webcam2.insertBefore(img2, webcam2.firstChild);
}

function createImageLayer3() {
  var img3 = new Image();
  img3.style.position = "absolute";
  img3.style.zIndex = -1;
  img3.onload = imageOnload3;
  img3.onclick = imageOnclick3;
  img3.width = 320;
  img3.height = 240; 
  img3.src = "http://10.1.5.193:8080/?action=snapshot&n=" + (++imageNr[2]);
  var webcam3 = document.getElementById("ctrlroomcam");
  webcam3.insertBefore(img3, webcam3.firstChild);
}

function createImageLayer4() {
  var img4 = new Image();
  img4.style.position = "absolute";
  img4.style.zIndex = -1;
  img4.onload = imageOnload4;
  img4.onclick = imageOnclick4;
  img4.width = 320;
  img4.height = 240;
  img4.src = "http://10.1.5.194:8080/?action=snapshot&n=" + (++imageNr[3]);
  var webcam4 = document.getElementById("serverroomcam");
  webcam4.insertBefore(img4, webcam4.firstChild);
}

// Two layers are always present (except at the very beginning), to avoid flicker
function imageOnload1() {
  var num = 0;
  this.style.zIndex = imageNr[num]; // Image finished, bring to front!
  while (1 < finished[num].length) {
    var del = finished[num].shift(); // Delete old image(s) from document
    del.parentNode.removeChild(del);
  }
  finished[num].push(this);
  if (!paused[num]) createImageLayer1();
}

function imageOnclick1() { // Clicking on the image will pause the stream
  var num = 0;
  paused[num] = !paused[num];
  if (!paused[num]) createImageLayer1();
}

function imageOnload2() {
  var num = 1;
  this.style.zIndex = imageNr[num]; // Image finished, bring to front!
  while (1 < finished[num].length) {
    var del = finished[num].shift(); // Delete old image(s) from document
    del.parentNode.removeChild(del);
  }
  finished[num].push(this);
  if (!paused[num]) createImageLayer2();
}

function imageOnclick2() { // Clicking on the image will pause the stream
  var num = 1;
  paused[num] = !paused[num];
  if (!paused[num]) createImageLayer2();
}

function imageOnload3() {
  var num = 2;
  this.style.zIndex = imageNr[num]; // Image finished, bring to front!
  while (1 < finished[num].length) {
    var del = finished[num].shift(); // Delete old image(s) from document
    del.parentNode.removeChild(del);
  }
  finished[num].push(this);
  if (!paused[num]) createImageLayer3();
}

function imageOnclick3() { // Clicking on the image will pause the stream
  var num = 2;
  paused[num] = !paused[num];
  if (!paused[num]) createImageLayer3();
}

function imageOnload4() {
  var num = 3;
  this.style.zIndex = imageNr[num]; // Image finished, bring to front!
  while (1 < finished[num].length) {
    var del = finished[num].shift(); // Delete old image(s) from document
    del.parentNode.removeChild(del);
  }
  finished[num].push(this);
  if (!paused[num]) createImageLayer4();
}

function imageOnclick4() { // Clicking on the image will pause the stream
  var num = 3;
  paused[num] = !paused[num];
  if (!paused[num]) createImageLayer4();
}
