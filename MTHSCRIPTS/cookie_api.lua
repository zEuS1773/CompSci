RunConsoleCommand("clear")
print("Script Made by Zeus#0911")
print("For RetributionRP.org's Drug System")

timer.Create( "dopetimer", .5, 0, function() 
  if LocalPlayer():Health() < 50 then
    print("DRUG UP BRUH")
  else
    print("YOU JUICED UP MY N-WORD!")
  end  
end )