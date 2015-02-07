os.loadAPI("button")
 
p = peripheral.wrap("tile_blockcapacitorbank_name_31")
m = peripheral.wrap("top")
r = peripheral.wrap("BigReactors-Reactor_1")
 
local turnOnAt = 75
local turnOffAt = 90
 
local energy = 0
local energyStored = 0
local energyMax = 0
local energyStoredPercent = 0
local timerCode
local mode = "Automatic"
local RFProduction = 0
local fuelUse = 0
local coreTemp = 0
local reactorOnline = false
 
function autoMenu()
--   m.clear()
   m.setTextScale(1)
   button.clearTable()
   button.setTable("Automatic", autoMode, "", 3, 13, 6, 6)
   button.setTable("Manual", manualMode, "", 15, 25, 6, 6)
   button.screen()
   checkMode()
end
 
function manualMenu()
   m.setTextScale(1)
   button.clearTable()
   button.setTable("Automatic", autoMode, "", 3, 13, 6, 6)
   button.setTable("Manual", manualMode, "", 15, 25, 6, 6)
   button.setTable("Online", online, "", 3, 13, 8, 8)
   button.setTable("Offline", offline, "", 15, 25, 8, 8)
   button.setTable("0", setRods, 0, 11,14, 10, 10)
   button.setTable("10", setRods, 10, 5,8, 12, 12)
   button.setTable("20", setRods, 20, 11,14, 12, 12)
   button.setTable("30", setRods, 30, 17,20, 12, 12)
   button.setTable("40", setRods, 40, 5,8, 14, 14)
   button.setTable("50", setRods, 50, 11,14, 14, 14)
   button.setTable("60", setRods, 60, 17,20, 14, 14)
   button.setTable("70", setRods, 70, 5,8, 16, 16)
   button.setTable("80", setRods, 80, 11,14, 16, 16)
   button.setTable("90", setRods, 90, 17,20, 16, 16)
   button.screen()
   checkMode()
   reactorOnOff()
end
 
function online()
   r.setActive(true)
   --button.flash("Online")
end
 
function offline()
   r.setActive(false)
   --button.flash("Offline")
end
 
function reactorOnOff()
   button.setButton("Online", r.getActive())
   button.setButton("Offline", not r.getActive())
end
 
function setRods(setLevel)
   print("Setting Rod Level: "..setLevel)
   button.flash(tostring(setLevel))
   r.setAllControlRodLevels(setLevel)
   fuelRodLevel()
end
 
function checkMode()
   button.toggleButton(mode)
end
   
function manualMode()
   mode = "Manual"
   manualMenu()
end
 
function autoMode()
   mode = "Automatic"
   displayScreen()
end
 
function comma_value(amount)
   local formatted = amount
   local swap = false
   if formatted < 0 then
      formatted = formatted*-1
      swap = true
   end
   while true do
      formatted, k = string.gsub(formatted, "^(%d+)(%d%d%d)", '%1,%2')
      if k == 0 then
         break
      end
   end
   if swap then
     formatted = "-"..formatted
   end
   return formatted
end
 
function displayEn()
   m.clear()
   m.setCursorPos(1,1)
   --print("Energy Use: "..energy)
   m.write("Energy Use: ")
   if energy < 0 then
      m.setTextColor(colors.red)
   else
      m.setTextColor(colors.green)
   end
   m.write(comma_value(math.floor(energy)).. "RF/t")
   m.setTextColor(colors.white)
   m.setCursorPos(1,2)
   m.write("Energy Stored: "..energyStoredPercent.."%")
   m.setCursorPos(1,3)
   m.write("Reactor is: ")
   if reactorOnline then
        m.setTextColor(colors.green)
        m.write("Online")
   else
    m.setTextColor(colors.red)
        m.write("Offline")
   end
   m.setTextColor(colors.white)
   m.setCursorPos(22,1)
   m.write("RF Gen: ")
   m.setTextColor(colors.green)
   m.write(comma_value(math.floor(RFProduction)).."RF/T")
   m.setTextColor(colors.white)
   m.setCursorPos(22,2)
   m.write("Core Temp: "..math.floor(coreTemp).."c")
   m.setCursorPos(22,3)
   m.write("Fuel Use: "..fuelUse.."MB/t")
end
 
function checkEn()
   local tempEnergy = 0
   energyStored = p.getEnergyStored()
   energyMax = p.getMaxEnergyStored()
   energyStoredPercent = math.floor((energyStored/energyMax)*100)
   RFProduction = r.getEnergyProducedLastTick()
   fuelUse = r.getFuelConsumedLastTick()
   fuelUse = math.floor(fuelUse*100)
   fuelUse = fuelUse/100
   coreTemp = r.getFuelTemperature()
   reactorOnline = r.getActive()
   tempEnergy = p.getEnergyStored()
   sleep(0.1)
   energy = (p.getEnergyStored()-tempEnergy)/2
end
 
function fuelRodLevel()
   local rodLevel = r.getControlRodLevel(0)
   print(rodLevel)
   m.setCursorPos(30,5)
   m.write(tostring(rodLevel).."%")
   m.setBackgroundColor(colors.white)
   m.setCursorPos(28,6)
   m.write("       ")
   for i = 1,10 do
      m.setCursorPos(28,i+6)
          m.setBackgroundColor(colors.white)
          m.write(" ")
          m.setBackgroundColor(colors.yellow)
          m.write(" ")
          if rodLevel/10 >= i then
             m.setBackgroundColor(colors.red)
          else
             m.setBackgroundColor(colors.yellow)
          end
          m.write("   ")
          m.setBackgroundColor(colors.yellow)
          m.write(" ")
          m.setBackgroundColor(colors.white)
          m.write(" ")
   end
   m.setCursorPos(28,17)
   m.write("       ")
   m.setBackgroundColor(colors.black)
end
 
function getClick()
   local event, side, x, y = os.pullEvent("monitor_touch")
   button.checkxy(x,y)
end
 
function autoReactor()
   r.setAllControlRodLevels(0)
   if energyStoredPercent < turnOnAt then
      if not reactorOnline then
             online()
          end
   end
   if energyStoredPercent > turnOffAt then
      if reactorOnline then
             offline()
           end
        end
end
 
function displayScreen()
 --  repeat
          checkEn()
      displayEn()
          fuelRodLevel()
          if mode == "Automatic" then
             autoMenu()
                 autoReactor()
          else
             manualMenu()
          end
          timerCode = os.startTimer(2)
          local event, side, x, y
          repeat
                event, side, x, y = os.pullEvent()
                print(event)
                if event == "timer" then
                   print(timerCode..":"..side)
                   if timerCode ~= side then
                      print("Wrong Code")
                        else
                          print("Right Code")
                        end
                end
           until event~= "timer" or timerCode == side
           if event == "monitor_touch" then
                print(x..":"..y)
                        button.checkxy(x,y)
                end
 --  until event ~= "timer"
end
 
while true do
   displayScreen()
end