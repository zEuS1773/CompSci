RunConsoleCommand("cls")

chat.AddText( Color( 100, 100, 255 ), "\nScript Loaded! Current Config:\n Health: 50HP\n Armor: 50AP\n Stimpack: None (In Dev)")
MsgC( Color( 255, 0, 0 ), "Current Stats:")
print("Script Made by Zeus#0911")
print("For RetributionRP.org's Drug System")
timer.Create( "dopetimer", .25, 0, function() 
  if LocalPlayer():Health() < 50 then
	RunConsoleCommand("dw_equip_permitem", "sdc_health")
    chat.AddText( Color( 100, 100, 255 ), "Juiced up! (Used a Health Drug!) ")
  else
    
  end  
end )

timer.Create( "dopetimer1", .75, 0, function() 
  if LocalPlayer():Armor() < 50 then
	--RunConsoleCommand("dw_equip_permitem", "sdc_armor")
   -- chat.AddText( Color( 255, 50, 255 ), "Gassed Up! (Used a Armor Drug!) ")
  else
    
  end  
end )