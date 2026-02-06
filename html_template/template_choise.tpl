<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Choice</title>
</head>
<body>

<h2>Список словарей</h2>

<ul>
% for item in data:
    <li>
         <a href="./dic/{{ item[0] }}">{{ item[1] }}</a>
    </li>
% end
</ul>

</body>
</html>