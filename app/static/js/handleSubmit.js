var fileInput=document.getElementById("file")
var mysubmit1=document.getElementById("mysubmit1")
fileInput.addEventListener("change",function(){

    if(fileInput.value == ""){

        mysubmit1.disabled = true
    }else{
        mysubmit1.disabled = false

    }

})


