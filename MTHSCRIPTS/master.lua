--adding meth API
local console = meth_lua_api.console;


RunConsoleCommand("cls")
timer.Create( "start", 3, 1, function()
        print("A script made for RetributionRP.org!")
        print("Current Server:"+ game.GetIPAddress())
        print("Current Server Name:"+ GetHostName())
        print("Current Perms:")
end)




chat.AddText( Color( 100, 100, 255 ), "\nScript Loaded! Current Config:\n Health: 50HP\n Armor: 50AP\n Stimpack: None (In Dev)")

function health()
    timer.Create( "dopetimer", .75, 80, function() 
      if LocalPlayer():Health() < 50 then
        RunConsoleCommand("dw_equip_permitem", "sdc_health")
        chat.AddText( Color( 100, 100, 255 ), "Juiced up! (Used a Health Drug!) ")
      else

      end  
      if LocalPlayer():Armor() < 50 then
        RunConsoleCommand("dw_equip_permitem", "sdc_armor")
        chat.AddText( Color( 255, 50, 255 ), "Gassed Up! (Used a Armor Drug!) ")
      else

      end  
    end )
end




console.AddCommand("raid", health())



function raidbuff()
    timer.Create("raidtimer", .75, 80, function()
        if LocalPlayer():Health() < 50 then
                RunConsoleCommand("dw_redeem_unclaimed", "6")
                chat.AddText( Color(255, 0, 255), "Used a stimpack!")
		else
	
		end
	end)
end

console.AddCommand("raidstim", raidbuff())


-- tipjar spammer toggable by typing "tip_spam" in console
x = true

timer.Create( "IDKWhatever", 0.1, 0, function()
if x then
for k, v in pairs(ents.FindByClass("darkrp_tip_jar")) do
net.Start("DarkRP_TipJarDonate")
net.WriteEntity(v)
net.WriteUInt(1, 32)
net.SendToServer()
end
end
end )

concommand.Add("tip_spam", function()
x = !x
end )



-- rainbow physgun, toggable by typing "rainbow" in console
concommand.Add("rainbow",function()
hook.Add("Think", "Rainbow", function()
local RainbowPlayer = HSVToColor( CurTime() % 6 * 60, 1, 1 )
    LocalPlayer():SetWeaponColor( Vector( RainbowPlayer.r / 255, RainbowPlayer.g / 255, RainbowPlayer.b / 255 ) )
    LocalPlayer():SetPlayerColor( Vector( RainbowPlayer.r / 255, RainbowPlayer.g / 255, RainbowPlayer.b / 255 ) )
end )
end )



