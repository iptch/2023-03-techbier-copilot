$filename = $args[0]
$base64string = Get-Content -Path ./solutions/$filename.base64
[System.Text.Encoding]::UTF8.GetString(([System.Convert]::FromBase64String($base64string)|?{$_}))

