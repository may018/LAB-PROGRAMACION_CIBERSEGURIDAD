$ipPub = Invoke-RestMethod ifconfig.me
$ipL = Get-NetIPAddress -AddressFamily IPV4
$nmapPriv = nmap 192.168.100.12
$nmapPub = nmap 10.102.66.70
$nmapL = nmap --script=http-auth-finder 192.168.100.12
$contenido = """La IP Publica es:`n$ipPub`nlas IP privadas son:`n$ipL
              `nLa IP local que se usara para el ejercicio es 10.102.66.70, el resultado es:`n$nmapPriv
              `nEl siguiente nmap es a la IP publica es:`n$nmapPub
              `nY la IP privada para el ejercicio es 192.168.100.12 y el resultado es:`n$nampL """


$codificado = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($contenido))
Set-Content -Value "$codificado" -Path D:\Users\Mayel\Descargas\ip_scan.txt