local frame = vgui.Create( "DFrame" )
frame:SetSize( 500, 300 )
frame:Center()
frame:MakePopup()
frame:ShowCloseButton( false )
frame:SetTitle("Zeus' Admin Panel")
frame:SetVisible( false )

local sheet = vgui.Create( "DPropertySheet", frame )
sheet:Dock( FILL )

local panel = vgui.Create( "DPanel", sheet )
panel.Paint = function( self, w, h ) draw.RoundedBox( 4, 0, 0, w, h, Color( 192, 192, 192, self:GetAlpha() ) ) end
sheet:AddSheet( "Target", panel, "icon16/status_online.png" )

local panel1 = vgui.Create( "DPanel", sheet )
panel1.Paint = function( self, w, h ) draw.RoundedBox( 4, 0, 0, w, h, Color( 192, 192, 192, self:GetAlpha() ) ) end
sheet:AddSheet( "Warnings", panel1, "icon16/note_add.png" )

local panel2 = vgui.Create( "DPanel", sheet )
panel2.Paint = function( self, w, h ) draw.RoundedBox( 4, 0, 0, w, h, Color( 192, 192, 192, self:GetAlpha() ) ) end
sheet:AddSheet( "Jailing", panel2, "icon16/lock.png" )

local panel3 = vgui.Create( "DPanel", sheet )
panel3.Paint = function( self, w, h ) draw.RoundedBox( 4, 0, 0, w, h, Color( 192, 192, 192, self:GetAlpha() ) ) end
sheet:AddSheet( "Banning", panel3, "icon16/shield.png" )

local panel3 = vgui.Create( "DPanel", sheet )
panel3.Paint = function( self, w, h ) draw.RoundedBox( 4, 0, 0, w, h, Color( 192, 192, 192, self:GetAlpha() ) ) end
sheet:AddSheet( "Extras", panel3, "icon16/flag_yellow.png" )
    
local equip = vgui.Create("DButton", panel3)
	equip:SetText("Equip 1B (Gold Bars)")
	equip:SetSize( 210, 30 )
	equip:SetMouseInputEnabled( true )
	equip:SetIsToggle( true )
	equip:Toggle()
	equip:SetToggle()
    equip:Center()
    equip:SetPos(10, 0)
	function equip:DoClick()
         timer.Create("raidtimer", .5, 10, function()
            RunConsoleCommand("dw_equip_permitem", "j_gold_bar")  	   
		
	end)
end

local rainbow = vgui.Create("DButton", panel3)
	rainbow:SetText("Rainbow Physgun")
	rainbow:SetSize( 210, 30 )
	rainbow:SetMouseInputEnabled( true )
	rainbow:SetIsToggle( true )
	rainbow:Toggle()
	rainbow:SetToggle()
    rainbow:Center()
    rainbow:SetPos(10, 40)
	function rainbow:DoClick()
        RunConsoleCommand("rainbow")
	end


local Button1 = vgui.Create( "DButton")
	Button1:SetPos(0, 830)
	Button1:SetText("Open/Close Admin Menu")
	Button1:SetSize( 250, 30 )
	Button1:SetToggle()
	Button1:SetIsToggle( true )
	Button1:SetMouseInputEnabled( true )
	function Button1:DoClick()
       Button1:Toggle()
	   toggled = Button1:GetToggle()
	   if toggled then
		  frame:SetVisible( true )
       else
		  frame:SetVisible( false )
	   end		
	end
local Button2 = vgui.Create( "DButton")
	Button2:SetPos(0, 860)
	Button2:SetText("Terminate Menu")
	Button2:SetSize( 250, 30 )
	Button2:SetToggle()
	Button2:SetIsToggle( true )
	Button2:SetMouseInputEnabled( true )
	function Button2:DoClick()
        Button1:SetVisible( false )
        frame:SetVisible( false )
        Button2:SetVisible( false )
    end

local playertarget = vgui.Create( "DTextEntry", panel)
    playertarget:AllowInput( true )
    playertarget:SetSize( 250, 30 )
    playertarget:Center()
    playertarget:SetPos(15, 20)
    playertarget:SetPlaceholderText("STEAMID")
    playertarget.OnEnter = function( self )
        theoffender = self:GetValue()
        print(theoffender)
        offenderstring = tostring(theoffender)
        playername = player.GetBySteamID(offenderstring)
        print(playername)
    end

local commandoutline = vgui.Create( "DTextEntry", panel2)
    commandoutline:AllowInput( true )
    commandoutline:SetSize( 210, 30 )
    commandoutline:Center()
    commandoutline:SetPos(230, 200)
    commandoutline:SetPlaceholderText("Warn Command")
    commandoutline.OnEnter = function( self )
        commandtorun = self:GetValue()
        RunConsoleCommand("say", commandtorun)     
    end
    
-- Jails VV

local Jail = vgui.Create("DButton", panel2)
	Jail:SetText("Jail Player")
	Jail:SetSize( 210, 30 )
	Jail:SetMouseInputEnabled( true )
	Jail:SetIsToggle( true )
	Jail:Toggle()
	Jail:SetToggle()
    Jail:Center()
    Jail:SetPos(10, 0)
	function Jail:DoClick()
        RunConsoleCommand("sam", "jail", theoffender)
	end

local uJail = vgui.Create("DButton", panel2)
	uJail:SetText("Unjail Player")
	uJail:SetSize( 210, 30 )
	uJail:SetMouseInputEnabled( true )
	uJail:SetIsToggle( true )
	uJail:Toggle()
	uJail:SetToggle()
    uJail:Center()
    uJail:SetPos(230, 0)
	function uJail:DoClick()
        RunConsoleCommand("sam", "unjail", theoffender)
	end


local Jail1 = vgui.Create("DButton", panel2)
	Jail1:SetText("Jail Player for 1 minute")
	Jail1:SetSize( 210, 30 )
	Jail1:SetMouseInputEnabled( true )
	Jail1:SetIsToggle( true )
	Jail1:Toggle()
	Jail1:SetToggle()
    Jail1:Center()
    Jail1:SetPos(10, 40)
	function Jail1:DoClick()
        RunConsoleCommand("sam", "jail", theoffender, "1")
	end

local Jail2 = vgui.Create("DButton", panel2)
	Jail2:SetText("Jail Player for 2 minutes")
	Jail2:SetSize( 210, 30 )
	Jail2:SetMouseInputEnabled( true )
	Jail2:SetIsToggle( true )
	Jail2:Toggle()
	Jail2:SetToggle()
    Jail2:Center()
    Jail2:SetPos(10, 80)
	function Jail2:DoClick()
        RunConsoleCommand("sam", "jail", theoffender, "2")
	end

local Jail3 = vgui.Create("DButton", panel2)
	Jail3:SetText("Jail Player for 3 minutes")
	Jail3:SetSize( 210, 30 )
	Jail3:SetMouseInputEnabled( true )
	Jail3:SetIsToggle( true )
	Jail3:Toggle()
	Jail3:SetToggle()
    Jail3:Center()
    Jail3:SetPos(10, 120)
	function Jail3:DoClick()
        RunConsoleCommand("sam", "jail", theoffender, "3")
	end

local Jail4 = vgui.Create("DButton", panel2)
	Jail4:SetText("Jail Player for 4 minutes")
	Jail4:SetSize( 210, 30 )
	Jail4:SetMouseInputEnabled( true )
	Jail4:SetIsToggle( true )

	Jail4:SetToggle()
    Jail4:Center()
    Jail4:SetPos(10, 160)
	function Jail4:DoClick()
        RunConsoleCommand("sam", "jail", theoffender, "4")
	end

local Jail5 = vgui.Create("DButton", panel2)
	Jail5:SetText("Jail Player for 5 minutes")
	Jail5:SetSize( 210, 30 )
	Jail5:SetMouseInputEnabled( true )
	Jail5:SetIsToggle( true )
	Jail5:Toggle()
	Jail5:SetToggle()
    Jail5:Center()
    Jail5:SetPos(10, 200)
	function Jail5:DoClick()
        --RunConsoleCommand("sam", "jail", theoffender, "5")
        stringtorun = ("!warn " .. theoffender .. " Example | 5m Jail")
        stringtorunv2 = tostring(stringtorun)
        print(stringtorunv2)
        commandoutline:SetValue(stringtorunv2)
	end

-- Warns VV

-- STEAM_0:1:89261769

concommand.Add("rainbow",function()
hook.Add("Think", "Rainbow", function()
local RainbowPlayer = HSVToColor( CurTime() % 6 * 60, 1, 1 )
    LocalPlayer():SetWeaponColor( Vector( RainbowPlayer.r / 255, RainbowPlayer.g / 255, RainbowPlayer.b / 255 ) )
    LocalPlayer():SetPlayerColor( Vector( RainbowPlayer.r / 255, RainbowPlayer.g / 255, RainbowPlayer.b / 255 ) )
end )
end )


    