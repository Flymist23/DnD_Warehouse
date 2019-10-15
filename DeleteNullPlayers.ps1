Get-Content .\DnD_Warehouse\DnD_Data\nd-proceesed-dnd-players.json | Where-Object {$_ -notmatch "null"} | Set-Content .\DnD_Warehouse\DnD_Data\nd-proceesed-dnd-players2.json
