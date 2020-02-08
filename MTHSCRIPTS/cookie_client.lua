RunConsoleCommand("cls")
table1 = player.GetHumans()
print(table1)

chat.AddText( Color( 100, 100, 255 ), "Juiced up! (Used a Health Drug!) ")


MsgC( Color( 255, 0, 0 ), "Current Stats:")
print("Script Made by Zeus#0911")
print("For RetributionRP.org's Drug System")
timer.Create( "dopetimer", .5, 0, function() 
  if LocalPlayer():Health() < 50 then
	RunConsoleCommand("dw_equip_permitem" "sdc_health")
    chat.AddText( Color( 100, 100, 255 ), "Juiced up! (Used a Health Drug!) ")
  else
    
  end  
end )