; AUTOHOTKEY SCRIPT TO RUN THIS. FEEL FREE TO CHANGE THIS ACCORDING TO REQUIREMENT.
; ! - Alt, q - Q, :: - execute the following code.

; Press "Alt + Q" to run the sequence
!q::
{
    ; Open Windows power menu
    Send("#x")
    Sleep(300)

    ; Press i
    Send("i")
    Sleep(1000)   ; wait for terminal to open

    ; Navigate directories
    Send("cd..{Enter}")
    Sleep(300)

    Send("cd..{Enter}")
    Sleep(300)

    Send("cd{Enter}")
    Sleep(300)

    ; Run dock.cmd
    Send("cd dock.cmd{Enter}")
    Sleep(500)
	
	; Run clear screen
    Send("cls{Enter}")
    Sleep(200)

    ; Run Python app
    Send("python app.py{Enter}")
}