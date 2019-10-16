Function pause ($message)
{
    # Check if running Powershell ISE
    if ($psISE)
    {
        Add-Type -AssemblyName System.Windows.Forms
        [System.Windows.Forms.MessageBox]::Show("$message")
    }
    else
    {
        Write-Host "$message" -ForegroundColor Yellow
        $x = $host.ui.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    }
}

$FileName = "nd-proceesed-dnd-players2"
$FolderPath= ".\DnD_Data"
$Path = $FolderPath+"\"+ $FileName+".json"

if (!(Test-Path $Path))
{
   New-Item -itemType File -Path $FolderPath -Name ($FileName + ".json")
   Write-Host "Created new file"+$FileName+".json"
}

Get-Content .\DnD_Data\nd-proceesed-dnd-players.json | Where-Object {$_ -notmatch "null"} | Set-Content .\DnD_Data\nd-proceesed-dnd-players2.json
pause("If no text above, then all null records have been removed and your free to move onto Claen_and_Make_KVPairs.py (waiting for Keypress)")

