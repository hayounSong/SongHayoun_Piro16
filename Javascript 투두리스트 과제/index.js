const plus = document.querySelector('.plus');
const whatinput=document.querySelector('.whatinput')
const list =document.querySelector('.list')
const deleteall=document.querySelector('.alldelete')
const deletelast=document.querySelector('.lastdelete')
const deleteselect=document.querySelector('.selectdelete')
const section=document.querySelector('section')
const originalheight=window.getComputedStyle(section).height
function init(){
    plus.addEventListener('click',plusdiv)
    plus.addEventListener('click',pluslist)
    deleteall.addEventListener('click',alldelete)
    deletelast.addEventListener('click',lastdelete)
    deleteselect.addEventListener('click',selectdelete)
}
let count=0;
function plusdiv(){
    const div=document.createElement('div');
    list.appendChild(div);
    
}
function pluslist(){
    const input= document.createElement('input')
    const span=document.createElement('span')
    let finddiv=document.querySelectorAll(".list div")
    console.log(count)
    finddiv[count].append(input,span)
  
    console.log(section.style.height)
    
    input.type='checkbox'
    const intext=whatinput.value 
    span.innerText=intext
    count=count+1
    

}
function lastdelete(){
    let divlist=document.querySelectorAll('.list div')
    for (var i=0; i<divlist.length; i++){
        if(i==divlist.length-1){
            divlist[i].remove()
        }
      }
    count=count-1
}
function alldelete(){
    let divlist=document.querySelectorAll('.list div')
    for (var i=0; i<divlist.length; i++){
        
        divlist[i].remove()
        
      }
      
    count=0
}
function selectdelete(){
    let checkcheck=document.querySelectorAll('.list input')
    let divlist=document.querySelectorAll('.list div')
    for (var i=0; i<checkcheck.length; i++){
        
        if(checkcheck[i].checked==true){
            divlist[i].remove()
            count=count-1
        }
        
      }
      
    }
init()