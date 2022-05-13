#Este es un script de powershell

for ($i = 1; $i -lt 5; $i++) {
  Write-Output "Vamos en el numero $i"
  Start-Sleep -Seconds $i
}