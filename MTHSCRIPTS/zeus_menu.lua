tr = true
timer1 = "salt"
timer2 = "salt2"





REFRESHRATE = 0.1 -- CHANGE THE NUMBER TO HOW OFTEN YOU WANT THE CONSOLE TO PRINT AN ENTITY


print( Entity( 1 ):GetEyeTrace().Entity )

-- START OF GUIS
local StaffButton = vgui.Create( "DButton")
	StaffButton:SetPos(0, 770)
	StaffButton:SetText("Open/Close Staff Menu")
	StaffButton:SetSize( 250, 30 )
	StaffButton:SetToggle()
	StaffButton:SetIsToggle( true )
	StaffButton:SetMouseInputEnabled( true )
	function StaffButton:DoClick()
		StaffButton:Toggle()
	end


local Button1 = vgui.Create( "DButton")
	Button1:SetPos(0, 800)
	Button1:SetText("Open/Close Script Menu")
	Button1:SetSize( 250, 30 )
	Button1:SetToggle()
	Button1:SetIsToggle( true )
	Button1:SetMouseInputEnabled( true )
	function Button1:DoClick()
		Button1:Toggle()
	end


local Frame = vgui.Create("DFrame")
    Frame:SetIcon("C:\\The_Best.png")
    Frame:ShowCloseButton( false )
    Frame:SetSize(300, 500)
    Frame:SetSizable( true )
    Frame:SetDraggable( true )
    Frame:SetTitle("Zeus' Menu")
    Frame:Center()
    Frame:MakePopup()

local StaffMenu = vgui.Create("DFrame")
    StaffMenu:SetIcon("C:\\The_Best.png")
    StaffMenu:ShowCloseButton( false )
    StaffMenu:SetSize(300, 500)
    StaffMenu:SetSizable( true )
    StaffMenu:SetDraggable( true )
    StaffMenu:SetTitle("Zeus' Menu")
    StaffMenu:Center()
    StaffMenu:MakePopup()


    

local Button3 = vgui.Create( "DButton", Frame)
	Button3:SetPos(25, 30)
	Button3:SetText("Health/Armor Script")
	Button3:SetSize( 250, 30 )
	Button3:SetMouseInputEnabled( true )
	
	Button3:SetIsToggle( true )
	Button3:Toggle()
	Button3:SetToggle()
	function Button3:DoClick()
		Button3:Toggle()
	end

local x, y = Button3:GetBounds()


local Button4 = vgui.Create("DButton", Frame)
    Button4:SetPos(x, y + 40)
	Button4:SetText("Stimpack Script")
	Button4:SetSize( 250, 30 )
	Button4:SetMouseInputEnabled( true )
	Button4:SetIsToggle( true )
	Button4:Toggle()
	Button4:SetToggle()
	function Button4:DoClick()
		Button4:Toggle()
	end
local Button5 = vgui.Create("DButton", Frame)
    Button5:SetPos(x, y + 80)
	Button5:SetText("Physgun Script")
	Button5:SetSize( 250, 30 )
	Button5:SetMouseInputEnabled( true )
	Button5:SetIsToggle( true )
	Button5:Toggle()
	Button5:SetToggle()
	function Button5:DoClick()
		Button5:Toggle()
	end

local Button6 = vgui.Create("DButton", Frame)
    Button6:SetPos(x, y + 120)
	Button6:SetText("Tipjar Script")
	Button6:SetSize( 250, 30 )
	Button6:SetMouseInputEnabled( true )
	Button6:SetIsToggle( true )
	Button6:Toggle()
	Button6:SetToggle()
	function Button6:DoClick()
		Button6:Toggle()
	end

timer.Create("gangert yall", REFRESHRATE, 0, function()
    toggled = StaffButton:GetToggle()
    if toggled then
        StaffMenu:SetVisible( true )
    else
        StaffMenu:SetVisible( false )
    end
end)


timer.Create(timer1, REFRESHRATE, 0, function()
	toggled = Button1:GetToggle()
	if toggled then
		Frame:SetVisible( true )
			else
		Frame:SetVisible( false )
	end
end)

	local Button2 = vgui.Create( "DButton")
	Button2:SetPos(0, 830)
	Button2:SetText("Terminate Menu")
	Button2:SetSize( 250, 30 )
	function Button2:DoClick()
		Button1:SetVisible( false )
		Button2:SetVisible( false )
        Button3:SetVisible( false )
        Button4:SetVisible( false )
        StaffButton:SetVisible( false )
        StaffMenu:SetVisible( false )
		Frame:SetVisible( false )
	end

timer.Create(timer2, REFRESHRATE, 0, function()
	toggled2 = Button3:GetToggle()
	if toggled2 then
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
    else
    
	end
end)

timer.Create("gamer", REFRESHRATE, 0, function()
	toggled2 = Button4:GetToggle()
	if toggled2 then
        if LocalPlayer():Health() < 50 then
            RunConsoleCommand("dw_redeem_unclaimed", "6")
            chat.AddText( Color( 100, 100, 255 ), "Juiced up! (Used a Stimpack!) ")
        else
        
        end
    else
    
	end
end)

timer.Create("gamer123", REFRESHRATE, 0, function()
	toggled2 = Button5:GetToggle()
	if toggled2 then
        hook.Add("Think", "Rainbow", function()
        local RainbowPlayer = HSVToColor( CurTime() % 6 * 60, 1, 1 )
        LocalPlayer():SetWeaponColor( Vector( RainbowPlayer.r / 255, RainbowPlayer.g / 255, RainbowPlayer.b / 255 ) )
        LocalPlayer():SetPlayerColor( Vector( RainbowPlayer.r / 255, RainbowPlayer.g / 255, RainbowPlayer.b / 255 ) )
        end )
    else
    
	end
end)


timer.Create("gamer12345", REFRESHRATE, 0, function()
	toggled2 = Button6:GetToggle()
	if toggled2 then
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
    else
    
	end
end)

--STAFF SCRIPTS HERE VVVV
local Jail1 = vgui.Create("DButton", StaffMenu)
	Jail1:SetText("Get Player's Name")
	Jail1:SetSize( 250, 30 )
	Jail1:SetMouseInputEnabled( true )
	Jail1:SetIsToggle( true )
	Jail1:Toggle()
	Jail1:SetToggle()
    Jail1:Center()
    Jail1:SetPos(25, 60)
	function Jail1:DoClick()
        
		chat.AddText( Color( 100, 100, 255 ), "Name: ")
	end

local Jail2 = vgui.Create("DButton", StaffMenu)
	Jail2:SetText("Jail Player for 1 minute")
	Jail2:SetSize( 250, 30 )
	Jail2:SetMouseInputEnabled( true )
	Jail2:SetIsToggle( true )
	Jail2:Toggle()
	Jail2:SetToggle()
    Jail2:Center()
    Jail2:SetPos(25, 120)
	function Jail2:DoClick()
        RunConsoleCommand("sam", "jail", theoffender, "1")
	end

local Jail3 = vgui.Create("DButton", StaffMenu)
	Jail3:SetText("Jail Player for 2 minutes")
	Jail3:SetSize( 250, 30 )
	Jail3:SetMouseInputEnabled( true )
	Jail3:SetIsToggle( true )
	Jail3:Toggle()
	Jail3:SetToggle()
    Jail3:Center()
    Jail3:SetPos(25, 150)
	function Jail3:DoClick()
        RunConsoleCommand("sam", "jail", theoffender, "2")
	end


function saveid()
    playertargetid = playertarget:GetValue()
    return playertargetid
end

local playertarget = vgui.Create( "DTextEntry", StaffMenu)
    playertarget:AllowInput( true )
    playertarget:SetSize( 250, 30 )
    playertarget:Center()
    playertarget:SetPos(25, 30)
    playertarget.OnEnter = function( self )
        theoffender = self:GetValue()
        print(theoffender)
    end
    
    
    


