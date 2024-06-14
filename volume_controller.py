from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import math

# Get the default audio device
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

# Define the minimum and maximum volume levels in dB
MIN_VOLUME_DB = -70.0
MAX_VOLUME_DB = 0.0

def increase_volume():
    # Get the current volume level
    currentVolume = volume.GetMasterVolumeLevel()

    # Increase volume by 5 dB
    newVolume = currentVolume + 5

    # Ensure the new volume does not exceed the maximum
    if newVolume > MAX_VOLUME_DB:
        newVolume = MAX_VOLUME_DB

    # Set the new volume level
    volume.SetMasterVolumeLevel(newVolume, None)
    print(f"Volume increased from {currentVolume:.2f} dB to {newVolume:.2f} dB")

def decrease_volume():
    # Get the current volume level
    currentVolume = volume.GetMasterVolumeLevel()

    # Decrease volume by 5 dB
    newVolume = currentVolume - 5

    # Ensure the new volume does not go below the minimum
    if newVolume < MIN_VOLUME_DB:
        newVolume = MIN_VOLUME_DB

    # Set the new volume level
    volume.SetMasterVolumeLevel(newVolume, None)
    print(f"Volume decreased from {currentVolume:.2f} dB to {newVolume:.2f} dB")

# Example usage
# increase_volume()
# decrease_volume()
