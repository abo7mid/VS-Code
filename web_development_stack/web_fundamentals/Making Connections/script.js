//edit the profile name

var edit = document.querySelector("#editProfile");
edit.addEventListener("click",changProfileName);



var box1 = document.querySelector("#box1");




function changProfileName(){
        /// find our target
        var name = document.getElementById("name");
        text = document.createElement('input');
        button = document.createElement('button');
        button.innerText = "Change";
        text.value = name.innerText;

        var editedText = box1.appendChild(text);   
        var change = box1.appendChild(button);
        change.onclick = function(){
        name.innerText = text.value;
        };
        // change.id = "change";
        editedText.style.margin = "0px 10px";
        edit.remove();
}


var accept = document.getElementById("accept");
accept.addEventListener("click",AcceptConnection);

var close = document.getElementById("close");
close.addEventListener("click",RejectConnection);


//get connection requests number
var connectionReq = document.querySelector(".connectionReq");
//get current connections number
var connections = document.querySelector(".connections");
//get element to hide 
var conneReqList = document.getElementById("conneReqList");
var conneReqList1 = document.getElementById("conneReqList1");




document.getElementById("accept1").onclick =  function(){
    connections.innerText = parseInt(connections.innerText)+1;
    connectionReq.innerText = parseInt(connectionReq.innerText)-1
    conneReqList1.remove();

};

document.getElementById("close1").onclick =  function(){
    connectionReq.innerText = parseInt(connectionReq.innerText)-1
    conneReqList1.remove();

};




function RejectConnection(){
    connectionReq.innerText = parseInt(connectionReq.innerText)-1
    conneReqList.remove();
}

function AcceptConnection(){
    connections.innerText = parseInt(connections.innerText)+1
    connectionReq.innerText = parseInt(connectionReq.innerText)-1
    conneReqList.remove();

}


