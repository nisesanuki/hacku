function login()
{
    var email = document.getElementById("email").value;
    var pass  = document.getElementById("pass").value;

    // 入力値チェック
    if (pass == "" && email == "")
    {
        alert("ユーザ名とパスワードを入力してください");
    }
    else if (pass == "")
    {
        alert("パスワードを入力してください");
    }
    else if (email == "")
    {
        alert("ユーザ名を入力してください");
    }

    // API 実行
    $.post("http://localhost:37564/login",
           {email:email, password:pass},
           function(data){alert(data)});
}

function user_registration()
{
    var email = document.getElementById("email").value;
    var pass  = document.getElementById("pass").value;

    // 入力値チェック
    if (pass == "" && email == "")
    {
        alert("ユーザ名とパスワードを入力してください");
    }
    else if (pass == "")
    {
        alert("パスワードを入力してください");
    }
    else if (email == "")
    {
        alert("ユーザ名を入力してください");
    }

    // API 実行
    $.post("http://localhost:37564/regist",
           {email:email, password:pass},
           function(data){alert(data)});
}


