//-----------------------//
//    クラスの定義       //
//-----------------------//
//CB情報クラス
class CBInfo {
  constructor(id){
    this.id = id ;//CBのSVGでのＩＤ
    this.on_off  = true ;//CBのオンオフ状態
    this.linkedBSId= null;
    this.linkId = []
  }
  //CBに接続している設備を定義する
  setLinkedBSId(id){
    this.linkedBSId= id;
  }

  setLinkedGNId(id){
    this.linkedGNId= id;
  }

  //CBシンボルの再描画.リンクされた設備についてもthisを渡し、再描画する。
  reDraw(){
    //HTMLオブジェクトのＣＢをidから取得
    var cb_symbol = document.getElementById(this.id);
    //オンオフ状態によって色を切り替える
    if(this.on_off == 0){
      cb_symbol.setAttribute("fill","green");  
    }
    else{
      cb_symbol.setAttribute("fill","red");
    }
    //CBに所属するBSの再描画を行う
    if (this.linkedBSId != null ){
      hash_bs_info[this.linkedBSId].reDraw(this);
    }

    //CBに所属するGNの再描画を行う
    if (this.linkedGNId != null ){
      hash_gn_info[this.linkedGNId].reDraw(this);
    }

  }
}
//TM情報クラス
class TMInfo {
  constructor(id){
    this.id = id ;//SVGでのＩＤ
    this.val_now     = 0 ;//現在のＴＭ値
    this.val_control = 0;//指令値
  }
  //指令値TMシンボル用の文字列を作成
  getTextValControl(){
    return "指令値:" + this.val_control + "MW"
  }
  //発電量TMシンボル用の文字列を作成
  getTextValNow(){
    return "発電量:" + this.val_now + "MW"
  }
  getControlSymbolID(){
    return this.id + "CON"
  }
  getNowSymbolID(){
    return this.id + "NOW"
  }
  //TMIDを元にTMシンボルの更新処理
  reDraw(){
    //指令値TMシンボルの取得
    var tm_con_symbol = document.getElementById(this.getControlSymbolID());
    //指令値TMシンボルの更新
    tm_con_symbol.textContent = this.getTextValControl();
    //発電量TMシンボルの取得
    var tm_now_symbol = document.getElementById(this.getNowSymbolID());
    //発電量TMシンボルの更新
    tm_now_symbol.textContent = this.getTextValNow();
  }
}

//BS情報クラス
class BSInfo {
  constructor(id){
    this.id         = id ;//SVGでのＩＤ
  }
  //TMIDを元にTMシンボルの更新処理
  reDraw(cb){
    var bs_symbol = document.getElementById(this.id);
    if(cb.on_off == 0){
      bs_symbol.setAttribute("stroke","green");  
    }
    else{
      bs_symbol.setAttribute("stroke","red");
    }
  }
}


//GN情報クラス
class GNInfo {
  constructor(id){
    this.id         = id ;//SVGでのＩＤ
  }
  //TMIDを元にTMシンボルの更新処理
  reDraw(cb){
    var bs_symbol = document.getElementById(this.id);
    if(cb.on_off == 0){
      bs_symbol.setAttribute("fill","green");  
    }
    else{
      bs_symbol.setAttribute("fill","red");
    }
  }
}


//----------------------------//
//    グローバル変数の定義    //
//----------------------------//
var hash_cb_info = {};
var hash_tm_info = {};
var hash_bs_info = {};
var hash_gn_info = {};
//ＣＢの連想配列にＣＢを追加
hash_cb_info["CB1"] = new CBInfo("CB1");
hash_cb_info["CB2"] = new CBInfo("CB2");
hash_cb_info["CB3"] = new CBInfo("CB3");


//TMの連想配列にTMを追加
hash_tm_info["TM1"] = new TMInfo("TM1");
hash_tm_info["TM2"] = new TMInfo("TM2");
//BSの連想配列にBSを追加
hash_bs_info["BS1"] = new BSInfo("BS1");
hash_cb_info["CB1"].setLinkedBSId("BS1");
hash_bs_info["BS3"] = new BSInfo("BS3");
hash_cb_info["CB2"].setLinkedBSId("BS3");

//GN1の連想配列にGNを追加
hash_gn_info["GN1"] = new GNInfo("GN1");
hash_cb_info["CB1"].setLinkedGNId("GN1");

hash_gn_info["GN2"] = new GNInfo("GN2");
hash_cb_info["CB2"].setLinkedGNId("GN2");



//----------------------------//
//       関数の宣言           //
//----------------------------/.

//PyhtonのCGIを実行し現在DBを取得する。
function getJSON() {
  var req = new XMLHttpRequest();                     // XMLHttpRequest オブジェクトを生成する
  req.onreadystatechange = function() {               // XMLHttpRequest オブジェクトの状態が変化した際に呼び出されるイベントハンドラ
    if(req.readyState == 4 && req.status == 200){   // サーバーからのレスポンスが完了し、かつ、通信が正常に終了した場合
          console.log(req.responseText);
          var data = JSON.parse(req.responseText);    // 取得した JSON ファイルの中身を変数へ格納
          var len = data.length;                      // JSON のデータ数を取得
          
          // JSON のデータ数分処理
          for(var i=0; i<len; i++) {
              //console.log("id: " + data[i].id + ", name: " + data[i].name);

              //typeがＣＢの場合、ＣＢの更新処理を行う
              if(data[i].type == "CB"){
                console.log("id: " + data[i].id);
                console.log("val: " + data[i].val);
                if(hash_cb_info[data[i].id]){
                  hash_cb_info[data[i].id].on_off = data[i].val
                  hash_cb_info[data[i].id].reDraw()
                }
              }
              else if(data[i].type == "TM"){//typeがＴＭの場合、ＴＭの更新処理を行う。
                console.log("id: " + data[i].id);
                console.log("now: " + data[i].now);
                console.log("control: " + data[i].control);
                if(hash_tm_info[data[i].id]){
                  hash_tm_info[data[i].id].val_now = data[i].now;
                  hash_tm_info[data[i].id].val_control = data[i].control
                  hash_tm_info[data[i].id].reDraw()
                }

              }
          }

      }
  };
  //req.open("GET", "cgi-bin/json_test.py", false);              // HTTPメソッドとアクセスするサーバーのURLを指定
  req.open("GET", "cgi-bin/json_test.py?kind=CB", false);
  req.send(null);                                     // 実際にサーバーへリクエストを送信
}

//getJSON関数を一秒毎に実行する
var timer_id = setInterval(getJSON,1000);

//TM背景の自動作成
document.addEventListener("DOMContentLoaded", function(){
	var text = document.querySelector("#TM1NOW");
	var bbox = text.getBBox();
	var rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
	rect.x.baseVal.value = bbox.x;
	rect.y.baseVal.value = bbox.y;
	rect.width.baseVal.value = bbox.width;
	rect.height.baseVal.value = bbox.height;
	rect.style.fill = "gray";
	text.parentNode.insertBefore(rect, text);
}, false);

//TMのHTMLオブジェクトのIDを変換する
function tmIdTranser(id){
  return id.slice(0,3)
}

//CB操作ダイアログ
function operateCB(item){
  _id = item.getAttribute("id")
	// 入力ダイアログを表示 ＋ 入力内容を val に代入
	val = window.prompt( _id+"入り切り(1/0)を入力してください", "");
  console.log("operation:"+val);
	// 空の場合やキャンセルした場合は警告ダイアログを表示
	if( (val == "") || (val ==   null)  ){
		window.alert('キャンセルされました');
  }
  else{
      sendOperation("CB",_id,val)
  }
}

//TMの指令値入力ダイアログ
function operateTM(item){
  // 入力ダイアログを表示 ＋ 入力内容を user に代入
  _id = item.getAttribute("id");
  _id = tmIdTranser(_id);
  val = window.prompt( _id+":指令値を入力してください", "");
  console.log("operation:"+val);
	// 空の場合やキャンセルした場合は警告ダイアログを表示
	if( (val == "") || (val ==   null)  ){
		window.alert('キャンセルされました');
  }
  else{
      sendOperation("TM",_id,val)
  }
}

//操作ダイアログで入力された値をCGIに送信する関数
function sendOperation(_type,_id,val) {
  var req = new XMLHttpRequest();                     // XMLHttpRequest オブジェクトを生成する
  req.onreadystatechange = function() {               // XMLHttpRequest オブジェクトの状態が変化した際に呼び出されるイベントハンドラ
      if(req.readyState == 4 && req.status == 200){   // サーバーからのレスポンスが完了し、かつ、通信が正常に終了した場合
          console.log(req.responseText);
          //var data = JSON.parse(req.responseText);    // 取得した JSON ファイルの中身を変数へ格納
          //var len = data.length;                      // JSON のデータ数を取得
          console.log("end_operation")
      }
  };
  //CGIに送信する情報の作成
  send_str = "type=" +_type + "&id=" + _id + "&val=" + val
  req.open("GET", "cgi-bin/get_control.py?"+send_str, false);
  req.send(null);                                     // 実際にサーバーへリクエストを送信
}

