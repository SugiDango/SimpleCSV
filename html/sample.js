
//ボタン１をクリックした時の処理
function btn1Click(){
  alert('ボタン１がクリックされました');
}
//ボタン２をクリックした時の処理
function btn2Click(){
  document.getElementById("btn1").click();
}

onload = function() {
  draw();
};
function draw() {
  /* canvas要素のノードオブジェクト */
  var canvas = document.getElementById('canvassample');
  /* canvas要素の存在チェックとCanvas未対応ブラウザの対処 */
  if ( ! canvas || ! canvas.getContext ) {
    return false;
  }
  /* 2Dコンテキスト */
  var ctx = canvas.getContext('2d');
  /* 四角を描く */
  ctx.beginPath();
  ctx.moveTo(20, 20);
  ctx.lineTo(400, 20);
  ctx.lineTo(400, 400);
  ctx.lineTo(20, 400);
  ctx.closePath();
  ctx.stroke();
  
  
  
}

function draw2() {
  /* canvas要素のノードオブジェクト */
  var canvas = document.getElementById('canvassample');
  /* canvas要素の存在チェックとCanvas未対応ブラウザの対処 */
  if ( ! canvas || ! canvas.getContext ) {
    return false;
  }
  /* 2Dコンテキスト */
  var ctx = canvas.getContext('2d');
  /* 四角を描く */
  ctx.beginPath();
  ctx.moveTo(20, 20);
  ctx.lineTo(60, 20);
  ctx.lineTo(60, 60);
  ctx.lineTo(20, 60);
  ctx.closePath();
  ctx.stroke();
 
  ctx.beginPath();
  ctx.moveTo(40, 40);
  ctx.lineTo(60, 40);

  ctx.stroke();
  
  
}

function drawBS(){


}

function drawCB() {
  var canvas = document.getElementById('canvassample');
  if ( ! canvas || ! canvas.getContext ) { return false; }
  var ctx = canvas.getContext('2d');
  ctx.beginPath();
  ctx.fillRect(40, 40, 10, 10);
}





