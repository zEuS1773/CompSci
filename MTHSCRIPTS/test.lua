tr = true
timer1 = "salt"
timer2 = "salt2"


REFRESHRATE = 0.1 -- CHANGE THE NUMBER TO HOW OFTEN YOU WANT THE CONSOLE TO PRINT AN ENTITY


print( Entity( 1 ):GetEyeTrace().Entity )

-- START OF GUIS

local Frame = vgui.Create( "DFrame" )
	Frame:SetPos( 5, 5 )
	Frame:SetSize( 300, 150 )
	Frame:SetTitle( "Octo's Entity Grabber" )
	Frame:SetVisible( true )
	Frame:SetDraggable( false )
	Frame:ShowCloseButton( true )
	Frame:MakePopup()
	Frame:Center()
	Frame:SetDraggable( true )

local Button1 = vgui.Create( "DButton")
	Button1:SetPos(0, 250)
	Button1:SetText("Open/Close Menu")
	Button1:SetSize( 250, 30 )
	Button1:SetToggle()
	Button1:SetIsToggle( true )
	Button1:SetMouseInputEnabled( true )
	function Button1:DoClick()
		Button1:Toggle()
	end


	
local Button3 = vgui.Create( "DButton", Frame)
	Button3:SetPos(0, 630)
	Button3:SetText("Press & Check Console")
	Button3:SetSize( 250, 30 )
	Button3:SetMouseInputEnabled( true )
	Button3:Center()
	Button3:SetIsToggle( true )
	Button3:Toggle()
	Button3:SetToggle()
	function Button3:DoClick()
		Button3:Toggle()
	end

	local Button2 = vgui.Create( "DButton")
	Button2:SetPos(0, 630)
	Button2:SetText("Terminate Menu")
	Button2:SetSize( 250, 30 )
	function Button2:DoClick()
		Button1:SetVisible( false )
		Button2:SetVisible( false )
		Frame:SetVisible( false )
	end
-- END OF GUIS 





timer.Create(timer1, REFRESHRATE, 0, function()
	toggled = Button1:GetToggle()
	if toggled then
		Frame:SetVisible( true )
			else
		Frame:SetVisible( false )
	end
end)

timer.Create(timer2, REFRESHRATE, 0, function()
	toggled2 = Button3:GetToggle()
	if toggled2 then
		print( Entity( 1 ):GetEyeTrace().Entity )
	end
end)