const check = function (_id){
    const checkBox=document.getElementById(_id)
    if (checkBox.value=='False'){ //not js false
        checkBox.value='True'
    }
}