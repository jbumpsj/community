from dataclasses import dataclass
import os
from talon import app

# This is a list of known "modern" windows applications where we can't access the executable
@dataclass
class WindowsApplication:
    """Class for tracking properties of known applications"""
    display_name: str
    unique_identifier: str
    executable_path: str
    executable_name: str
    is_uwp: bool = False

@dataclass
class WindowsShortcut:
    display_name: str
    full_path: str
    target_path: str
    arguments: str

    def __str__(self) -> str:
        return f"{self.display_name} {self.full_path} {self.target_path} {self.arguments}"
    
if app.platform == "windows":
    explorer_path = str(os.path.expandvars(os.path.join("%WINDIR%", "explorer.exe")))
    settings_path = str(os.path.expandvars(os.path.join("%WINDIR%", "ImmersiveControlPanel", "SystemSettings.exe")))
    windows_speech_recognition = str(os.path.expandvars(os.path.join("%WINDIR%", "speech", "Common", "sapisvr.exe")))
    mmc = str(os.path.expandvars(os.path.join("%WINDIR%", "system32", "mmc.exe"))) 
    windows_applications = [
        WindowsApplication(display_name="Control Panel", 
                        unique_identifier="Microsoft.Windows.ControlPanel",
                        executable_path=explorer_path,
                        executable_name="explorer.exe"),
        WindowsApplication(display_name="File Explorer", 
                        unique_identifier="Microsoft.Windows.Explorer", 
                        executable_path=explorer_path,
                        executable_name="explorer.exe"),  
        WindowsApplication(display_name="Run", 
                        unique_identifier="Microsoft.Windows.Shell.RunDialog", 
                        executable_path=explorer_path,
                        executable_name="explorer.exe"),       
        WindowsApplication(display_name="Settings", 
                        unique_identifier="windows.immersivecontrolpanel_cw5n1h2txyewy!microsoft.windows.immersivecontrolpanel", 
                        executable_path=settings_path,
                        executable_name="SystemSettings.exe"), 
        WindowsApplication(display_name="Windows Speech Recognition", 
                        unique_identifier="Microsoft.AutoGenerated.{DAA168DE-4306-C8BC-8C11-B596240BDDED}", 
                        executable_path=windows_speech_recognition,
                        executable_name="sapisvr.exe"),                         
    ]

    windows_application_dict = {}
    for application in windows_applications:
        unique_identifier = application.unique_identifier
        windows_application_dict[unique_identifier.lower()] = application
else:
    mmc = "INVALID"
    windows_application_dict = {}
    explorer_path = None

def get_known_windows_application(uuid) -> WindowsApplication:
    if uuid.lower() in windows_application_dict:
        return windows_application_dict[uuid.lower()]
    else:
        return None