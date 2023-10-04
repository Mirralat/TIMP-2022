const ifFalseSave = (event) => {
  if (event.keyCode == 83) {  
    event.preventDefault();
    return false;
  }
}

const ifFalsePrntScrn = (event) => {
  if (event.keyCode == 44) {  
    stopPrntScr();
  }
}


function stopPrntScr() {
  var inpFld = document.createElement("input");
  inpFld.setAttribute("value", ".");
  inpFld.setAttribute("width", "0");
  inpFld.style.height = "0px";
  inpFld.style.width = "0px";
  inpFld.style.border = "0px";
  document.body.appendChild(inpFld);
  inpFld.select();
  document.execCommand("copy");
  inpFld.remove(inpFld);
}


function main_part(cond) {
 
  document.ondragstart = () => cond;
  document.onselectstart = () => cond; 
  document.oncontextmenu =  () => cond;
  
  if (!cond) {  
    
    document.addEventListener('keydown', ifFalseSave);
    document.addEventListener('keyup', ifFalsePrntScrn);
  } else {  
    
    document.removeEventListener('keydown', ifFalseSave);
    document.removeEventListener('keyup', ifFalsePrntScrn);
  }
}

main_part(false);

document.getElementById("check").onclick = () => {
  const hashed_passwd = "1076595487";
  const passwd = document.getElementById("password").value;
  if (passwd.length == 0) alert("Пароль не введен. А зря.");
  let x = func(passwd)
  if (x == hashed_passwd) {
    alert("Пароль введен. Это хорошо.");
    main_part(true);
  }
  else {
    alert("Пароль неверный. Доступ я не дам.");
    main_part(false);
  }
}

function func(string) {
 
  var hash = 0;
  
  if (string.length == 0) return hash;
  for (i = 0 ;i<string.length ; i++)
  {
  ch = string.charCodeAt(i);
  hash = ((hash << 5) - hash) + ch;
  hash = hash & hash;
  }
  return hash;
}
