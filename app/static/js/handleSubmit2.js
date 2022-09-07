
var videoInput=document.getElementById("video")
var mysubmit1=document.getElementById("mysubmit1")
// var errfile=document.getElementById("errorfile")
// var filesel=false



videoInput.addEventListener("change",function(){

    if(videoInput.value == ""){
        mysubmit1.disabled = true
    // errfile.style.display="flex";
    // errfile.style.color="red";
    // errfile.innerHTML="select an image plese"
    }else{
    // errfile.style.color="green"
    // errfile.innerHTML="selected"
    // errfile.style.display="flex"
        mysubmit1.disabled = false

    }

})