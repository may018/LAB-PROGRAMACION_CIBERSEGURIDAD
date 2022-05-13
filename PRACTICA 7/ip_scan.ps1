$ipPublica = Invoke-RestMethod ifconfig.me
$ipLocal = Get-NetIPAddress -AddressFamily IPV4
$nmapPriv = nmap 192.168.100.12
$nmapPublica = nmap 187.188.73.85
$nmapLocal = nmap --script=http-auth-finder 192.168.100.12
$contenido = """Hola, mi IP publica es:`n$ipPublica`nmis IP privadas son:`n$ipLocal
              `nLa IP local que usaré para el nmap será: 192.168.100.12, el resultado fue:`n$nmapPriv
              `nEl siguiente nmap es a la IP publica es:`n$nmapPublica
              `nY por ultimo la IP privada que usaré para este nmap es: 192.168.100.12 y el resultado fue:`n$nampLocal """


$codificado = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($contenido))
Set-Content -Value "$codificado" -Path D:\Users\Mayel\Descargas\ip_scan.txt