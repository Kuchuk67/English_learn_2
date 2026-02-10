<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Choice</title>
</head>
<body>
<div class="fon">
<h2>Учим слова</h2>
<p>Осталось {{ counter }}, ошибок {{ erall }} </p>

<div id="block">
    <div class="word">{{ word[1] }}</div>
    <div class="txt">{{ word[3] }}</div>

    <div class="btn">
        <div onclick="Show();">Показать ответ </div>
    </div>
    <div class="ot50">
    </div>
    <div id="answer">
        <div class="txt">
            <div>{{ word[2] }} </div>
            
        </div>
        <div  class="btn">
            <a onclick="Hide();" href="/dic/{{ dic }}/{{ rate }}?rg={{ word[0] }}&er=0&erall={{ erall }}">знаю </a>
            <a onclick="Hide();" href="/dic/{{ dic }}/{{ rate }}?rg=0&er=0&erall={{ erall }}">повторить</a>
            <a onclick="Hide();" href="/dic/{{ dic }}/{{ rate }}?rg=0&er={{ word[0] }}&erall={{ erall }}">не знаю </a>
        </div>
    </div>
</div>
</div>

<script>
function Show(){
    document.getElementById('answer').style.display = 'block';
}
function Hide(){
    document.getElementById('block').style.display = 'none';
}
</script>

<style>
    body {
        font-size: 16pt;}
    .fon {
        width: 100%;
        max-width:400px;
        margin: 0 auto;
    }
    #answer {display: none;}
    .word {
        text-align: center;
        font-size: 22pt;
        padding: 0 0 20px 0;
    }
    .txt {
        text-align: center;
        padding: 0 0 20px 0;
    }
    .btn {
        display: flex;
    }
    .btn div {
        width: 200px;
        background: #dedede;
        text-align: center;
        padding: 5px 10px;
        margin: 0 10px;
        cursor: pointer;
    }
    .btn a {
        width: 100px;
        background: #dedede;
        text-align: center;
        padding: 5px 10px;
        margin: 0 10px;
        cursor: pointer;
        color: #000;
        text-decoration: none;
    }
    .ot50 {
        width:100%;
        height: 50px;
    }

</style>

</body>
</html>
