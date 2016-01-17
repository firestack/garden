#include <EditConstants.au3>
#include <GUIConstantsEx.au3>
#include <WindowsConstants.au3>
#include <Inet.au3>
;#include <ExtraCommands.au3>
#include <Array.au3>
#include <File.au3>
#RequireAdmin
Opt("GUIOnEventMode", 1)
#Region ### START Koda GUI section ### Form=
$Form1 = GUICreate("Twitch Chat", 200, 500, 0, (@DesktopHeight / 2) - 300, $GUI_SS_DEFAULT_GUI, BitOR($WS_EX_TOOLWINDOW, $WS_EX_WINDOWEDGE, $WS_EX_TOPMOST))
$Edit1 = GUICtrlCreateList("", 0, 0, 200, 500, BitOR($ES_READONLY, $ES_WANTRETURN))
GUISetState(@SW_SHOW)
#EndRegion ### END Koda GUI section ###

TCPStartup()

Global $server = "irc.twitch.tv"
Global $Port = 6667
Global $channel = InputBox("Channel", "Channel to join, Must begin with #", "#1862011")
Global $Nick = "bagos_bot"
Global $Sock
Global $token = "***** OAUTH TOKEN GOES HERE :P ********"
Global $Userlist = "1337kobzinfinity"
Global $Rafflelist = "1337kobzinfinity"
Global $Modlist = "1337kobzinfinity"
Global $GreetPeople = 1
Global $oldrequest = "null"
Global $banlinks = 1
Global $Rng = 1
Global $timestamp = "@error"
Global $Delay=15
Global $TimeNow=(@HOUR*60)+@MIN
Global $TimeNext=$TimeNow+$Delay
Global $automsg = ""

$oSp = ObjCreate("SAPI.SpVoice")

HotKeySet("|","Override")

If $channel = "#1862011" Then
	$banlinks = 1
ElseIf $channel = "#themightygrowlie" Then
	$GreetPeople = 0
EndIf

$Sock = _IRCConnect($server, $Port, $Nick, $token)

While 1
	$Recv = TCPRecv($Sock, 8192)
	If Not $Recv Then ContinueLoop
	$sData = StringSplit($Recv, @CRLF, 1)
	For $i = 1 To $sData[0]
		$sTemp = StringSplit($sData[$i], " ")
		If $sTemp[1] = "PING" Then TCPSend($Sock, "PONG " & $sTemp[2] & @CRLF)
		If $sTemp[0] < 3 Then ContinueLoop
		Switch $sTemp[2]
			Case "PRIVMSG"
				$User = StringMid($sTemp[1], 2, StringInStr($sTemp[1], "!") - 2)
				$Message = StringMid($sData[$i], StringInStr($sData[$i], ":", 0, 2) + 1)
				GUICtrlSetData($Edit1, $User & ": " & $Message & @CRLF, 1)
				Switch StringLower($Message)
					Case "!uptime"
						_IRCSendMessage($Sock, _INetGetSource('http://nightdev.com/hosted/uptime.php?channel=' & StringRight($channel, StringLen($channel) - 1)), $channel)
					Case StringLeft($Message, 6) = "!colour";
						If StringInStr($Modlist,$User) Then
							_IRCSendMessage($Sock, ".color " & StringRight($Message, StringLen($Message) - 7), $channel)
						EndIf
					Case StringLeft($Message, 6) = "!throw"
						If StringLower(StringRight($Message, StringLen($Message) - 7)) = "kobz" Then
							_IRCSendMessage($Sock, "(/^.^)/ " & $User, $channel)
						ElseIf StringLower(StringRight($Message, StringLen($Message) - 7)) = "1337kobzinfinity" Then
							_IRCSendMessage($Sock, "(/^.^)/ " & $User, $channel)
						Else
							_IRCSendMessage($Sock, "(/^.^)/ " & StringRight($Message, StringLen($Message) - 7), $channel)
						EndIf
					Case StringLeft($Message, 5) = "!roll"
						$Number = StringRight($Message, StringLen($Message) - 6)
						If $Number = "0" Then
							_IRCSendMessage($Sock, "You can't roll a 0 sided dice. FailFish", $channel)
						ElseIf StringIsDigit($Number) Then
							_IRCSendMessage($Sock, $User & " rolled a: " & Random(1, $Number, 1) & " out of " & $Number, $channel)
						Else
							_IRCSendMessage($Sock, $Number & " is not a number.", $channel)
						EndIf
					Case StringLeft($Message, 7) = "!define"
						$query = StringRight($Message, StringLen($Message) - 8)
						$response = _INetGetSource('http://www.google.com/search?q=define%3A' & $query)
						ClipPut($response)
						If StringInStr($response, '<li style="list-style-type:decimal">') Then
							$response = StringTrimLeft($response, StringInStr($response, '<li style="list-style-type:decimal">') + 35)
							$response = StringTrimRight($response, (StringLen($response) - StringInStr($response, '</li>')) + 1)
							_IRCSendMessage($Sock, $response, $channel)
						ElseIf StringInStr($response, '<ol><li>') Then
							$response = StringTrimLeft($response, StringInStr($response, '<ol><li>') + 7)
							$response = StringTrimRight($response, (StringLen($response) - StringInStr($response, '</li>')) + 1)
							_IRCSendMessage($Sock, $response, $channel)
						Else
							_IRCSendMessage($Sock, "Unable to find definition", $channel)
						EndIf
					Case StringLeft($Message, 6) = "!conch"
						$Random = Random(1, 19, 1)
						If $Random = 1 Then
							_IRCSendMessage($Sock, "This will never happen.", $channel)
						ElseIf $Random = 2 Then
							_IRCSendMessage($Sock, "Outlook doesn't look good.", $channel)
						ElseIf $Random = 3 Then
							_IRCSendMessage($Sock, "Signs point to yes", $channel)
						ElseIf $Random = 4 Then
							_IRCSendMessage($Sock, "Outlook seems legit.", $channel)
						ElseIf $Random = 5 Then
							_IRCSendMessage($Sock, "This will happen.", $channel)
						ElseIf $Random = 6 Then
							_IRCSendMessage($Sock, "It is certain", $channel)
						ElseIf $Random = 7 Then
							_IRCSendMessage($Sock, "It is decidedly so", $channel)
						ElseIf $Random = 8 Then
							_IRCSendMessage($Sock, "Without a doubt", $channel)
						ElseIf $Random = 9 Then
							_IRCSendMessage($Sock, "Yes definitely", $channel)
						ElseIf $Random = 10 Then
							_IRCSendMessage($Sock, "You may rely on it", $channel)
						ElseIf $Random = 11 Then
							_IRCSendMessage($Sock, "As I see it, yes", $channel)
						ElseIf $Random = 12 Then
							_IRCSendMessage($Sock, "Most likely", $channel)
						ElseIf $Random = 13 Then
							_IRCSendMessage($Sock, "Outlook good", $channel)
						ElseIf $Random = 14 Then
							_IRCSendMessage($Sock, "Yes", $channel)
						ElseIf $Random = 15 Then
							_IRCSendMessage($Sock, "Don't count on it", $channel)
						ElseIf $Random = 16 Then
							_IRCSendMessage($Sock, "My reply is no", $channel)
						ElseIf $Random = 17 Then
							_IRCSendMessage($Sock, "My sources say no", $channel)
						ElseIf $Random = 18 Then
							_IRCSendMessage($Sock, "Outlook not so good", $channel)
						ElseIf $Random = 19 Then
							_IRCSendMessage($Sock, "Very doubtful", $channel)
						Else
							_IRCSendMessage($Sock, "I am Error.", $channel)
						EndIf
					Case StringLeft($Message, 5) = "!roIl";
						$Number = StringRight($Message, StringLen($Message) - 6)
						If StringInStr($Modlist,$User) Then
							_IRCSendMessage($Sock, $User & " rolled a: " & $Number & " out of " & $Number, $channel)
						ElseIf $Number = "0" Then
							_IRCSendMessage($Sock, "You can't roll a 0 sided dice. FailFish", $channel)
						ElseIf StringIsDigit($Number) Then
							_IRCSendMessage($Sock, $User & " rolled a: " & Random(1, $Number, 1) & " out of " & $Number, $channel)
						Else
							_IRCSendMessage($Sock, $Number & " is not a number.", $channel)
						EndIf
					 Case StringLeft($Message, 9) = "!giveaway"
						If StringInStr($Modlist,$User) Then
						   $Prize = StringRight($Message, StringLen($Message) - 10)
						   $Array = StringSplit($Rafflelist, ",")
						   $Rng = Random(1, $Array[0], 1)
						   If $Rng = 0 Then
							  $Rng = 1
						   EndIf
						   _IRCSendMessage($Sock, $Array[$Rng] & " won: " & $Prize, $channel)
					 EndIf
					Case StringLeft($Message, 6) = "!quote"
						$string = StringRight($Message, StringLen($Message) - 7)
						If StringIsDigit($string) Then
							$q = FileReadLine(@desktopdir & "\TwitchBot\quote\" & $channel & ".txt", $string)
							If $q = "" Then
								_IRCSendMessage($Sock, "There is no quote #" & $string, $channel)
							Else
								_IRCSendMessage($Sock, $q, $channel)
							 EndIf
						  ElseIf $string = "random" Then
							 $q = FileReadLine(@desktopdir & "\quote\" & $channel & ".txt", Random(1, _FileCountLines(@desktopdir & "\quote\" & $channel & ".txt"), 1)
						_IRCSendMessage($Sock, $q, $channel)
						ElseIf StringInStr($Modlist,$User) Then
							FileWriteLine(@desktopdir & "\TwitchBot\quote\" & $channel & ".txt", $string)
							_IRCSendMessage($Sock, "added, this is quote #" & _FileCountLines(@desktopdir & "\TwitchBot\quote\" & $channel & ".txt"), $channel)
						EndIf
					Case "!enter"
						If Not StringInStr($Rafflelist, $User) Then
							$Rafflelist &= "," & $User
						EndIf
					Case "!title"
						$1 = _INetGetSource('https://api.twitch.tv/kraken/channels/' & StringRight($channel, StringLen($channel) - 1))
						$title = StringMid($1, StringInStr($1, '"status":') + 10, StringInStr($1, "broadcaster_language") - (StringInStr($1, '"status":') + 13))
						_IRCSendMessage($Sock, 'Title is "' & $title & '"', $channel)
					Case "!game"
						$1 = _INetGetSource('https://api.twitch.tv/kraken/channels/' & StringRight($channel, StringLen($channel) - 1))
						$game = StringMid($1, StringInStr($1, '"game":') + 8, StringInStr($1, '"delay"') - (StringInStr($1, '"game":') + 10))
						_IRCSendMessage($Sock, 'Currently Playing: ' & $game, $channel)
					Case "!ht"
						;$timestamp = _INetGetSource('http://nightdev.com/hosted/uptime.php?channel=' & StringRight($channel, StringLen($channel)-1))
						$1 = _INetGetSource('https://api.twitch.tv/kraken/streams/' & StringRight($channel, StringLen($channel) - 1))
						$t = StringSplit(StringMid($1, StringInStr($1, "created_at") + 24, (StringInStr($1, 'Z","') - StringInStr($1, "created_at")) - 24), ":")
						If $t[1] = 0 Then
						   $t[1] = 24
						EndIf
						$timestart = ((($t[1] * 60) + $t[2]) * 60) + $t[3]
						$timecurrent = ((((@HOUR + 4) * 60) + @MIN) * 60) + @SEC
						$timediff = $timecurrent - $timestart
						$hours = 0
						$mins = 0
						While $timediff > 3600
							$timediff = $timediff - 3600
							$hours = $hours + 1
						WEnd
						While $timediff > 60
							$timediff = $timediff - 60
							$mins = $mins + 1
						WEnd
						$timestamp = $hours & ":" & $mins & ":" & $timediff
						If not @error Then
							FileWrite(@DesktopDir & "\TwitchBot\ht.txt", @CRLF & $channel & " " & $timestamp & " ")
							_IRCSendMessage($Sock, "Highlight timestamp: " & $timestamp, $channel)
						Else
							IRCSendMessage($Sock, "The channel is not live.", $channel)
						EndIf
					Case "!raffleclear";
						If StringInStr($Modlist,$User) Then
							$Rafflelist = "1337kobzinfinity"
							_IRCSendMessage($Sock, "Raffle list cleared", $channel)
						EndIf
					Case "^";
						If StringInStr($Modlist,$User) Then
							_IRCSendMessage($Sock, "^", $channel)
						EndIf
					Case "!greeton";
						If StringInStr($Modlist,$User) Then
							$GreetPeople = 1
							_IRCSendMessage($Sock, "I will now greet users as they enter", $channel)
						EndIf
					Case "!greetoff";
						If StringInStr($Modlist,$User) Then
							$GreetPeople = 0
							_IRCSendMessage($Sock, "no longer greeting users", $channel)
						EndIf
					Case Else
						Extra()
						Automessage()
						If FileRead(@desktopdir & "\TwitchBot\speak.txt", 1) = "1" And $User <> "1337Kobzinfinity" Then
							$oSp.Speak($Message)
						EndIf
						If Not StringInStr($Userlist, $User) Then;Greet users as they enter
							$Userlist &= "," & $User
							$Random = Random(1, 4, 1)
							If StringInStr($Message, "http:") Then;Ban Links
							  If $banlinks = 1 Then
									_IRCSendMessage($Sock, ".timeout " & $User & " 1", $channel)
							  EndIf
									$Random = 0
						    EndIf
							If $User = StringRight($channel, StringLen($channel) - 1) Then
								$Random = 0
						    ElseIf $User = "jtv" Then
								If StringInStr($Message,"the moderators of this room are:") Then
									$Modlist = "1337kobzinfinity, "&StringRight($Message,StringLen($Message)-33)
								EndIf
							ElseIf $User = "brooky120" And $GreetPeople = 1 Then
								_IRCSendMessage($Sock, FileReadLine(@desktopdir & "\TwitchBot\ASCII.txt", 1), $channel)
							ElseIf $User = "Seki_Banki" And $GreetPeople = 1 Then
								_IRCSendMessage($Sock, "What's a seki?", $channel)
							ElseIf $GreetPeople = 1 Then
								If $Random = 1 Then
									_IRCSendMessage($Sock, "Hi " & $User, $channel)
								ElseIf $Random = 2 Then
									_IRCSendMessage($Sock, "Hey " & $User, $channel)
								ElseIf $Random = 3 Then
									_IRCSendMessage($Sock, "Greetings " & $User, $channel)
								ElseIf $Random = 4 Then
									_IRCSendMessage($Sock, "Sup " & $User, $channel)
								EndIf
							EndIf
						EndIf
				EndSwitch
			Case "004"
				_IRCJoinChannel($Sock, $channel)
				_IRCChangeMode($Sock, "+i", $Nick)
			Case "443"
				MsgBox(1, "irc.au3", "IRC username in use")
			Case Else
				ConsoleWrite($sTemp[2] & " - " & $sData[$i] & @CRLF) ;Write all unhandled packets to STDOUT
		EndSwitch
	 Next
WEnd

Func _IRCConnect($server, $Port, $Nick, $token)
	Local $i = TCPConnect(TCPNameToIP($server), $Port)
	If $i = -1 Then Exit MsgBox(1, "irc.au3 Error", "Server " & $server & " is not responding.")
	TCPSend($i, "PASS " & $token & @CRLF)
	TCPSend($i, "NICK " & $Nick & @CRLF)
	TCPSend($i, "USER " & $Nick & " 0 0 " & $Nick & @CRLF)


	Return $i
EndFunc   ;==>_IRCConnect
Func _IRCJoinChannel($irc, $chan)
	If $irc = -1 Then Return 0
	TCPSend($irc, "JOIN " & $chan & @CRLF)
	If @error Then
		MsgBox(1, "irc.au3", "Server has disconnected.")
		Return -1
	EndIf
	Return 1
EndFunc   ;==>_IRCJoinChannel
Func _IRCSendMessage($irc, $msg, $chan = "")
	If $irc = -1 Then Return 0
	If $chan = "" Then
		TCPSend($irc, $msg & @CRLF)
		If @error Then
			MsgBox(1, "irc.au3", "Server has disconnected.")
			Return -1
		EndIf
		Return 1
	EndIf
	TCPSend($irc, "PRIVMSG " & $chan & " :" & $msg & @CRLF)
	If @error Then
		MsgBox(1, "irc.au3", "Server has disconnected.")
		Return -1
	EndIf
	Return 1
EndFunc   ;==>_IRCSendMessage
Func _IRCChangeMode($irc, $mode, $chan = "")
	If $irc = -1 Then Return 0
	If $chan = "" Then
		TCPSend($irc, "MODE " & $mode & @CRLF)
		If @error Then
			MsgBox(1, "irc.au3", "Server has disconnected.")
			Return -1
		EndIf
		Return 1
	EndIf
	TCPSend($irc, "MODE " & $chan & " " & $mode & @CRLF)
	If @error Then
		MsgBox(1, "irc.au3", "Server has disconnected.")
		Return -1
	EndIf
	Return 1
EndFunc   ;==>_IRCChangeMode
Func Override()
   $Prompt = InputBox($channel,"Enter a message to send","Thanks for watching everyone o/")
   If $Prompt <> "" Then
	  _IRCSendMessage($Sock, $Prompt, $channel)
   EndIf
EndFunc
Func Extra()
   $ini = IniRead(@DesktopDir & "\TwitchBot\Commands.ini", $channel, $Message, "")
   If $ini <> "" Then
	  _IRCSendMessage($Sock, $ini, $channel)
   EndIf
EndFunc
Func Automessage()
   $TimeNow=(@HOUR*60)+@MIN
   If $TimeNow >= $TimeNext And $automsg <> "" Then
	  $TimeNext=$TimeNow+$Delay
	  _IRCSendMessage($Sock, $automsg, $channel)
   EndIf
EndFunc
