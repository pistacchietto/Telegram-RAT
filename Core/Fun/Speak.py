# Speaks text

def SpeakText(Text):
 from win32com.client import Dispatch
 speaker = Dispatch('SAPI.SpVoice')
 speaker.Speak(Text)
 del speaker