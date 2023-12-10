rem Set the target device ID
set DEVICE_ID="HID\VID_12D1&PID_10B8&MI_00&COL01\7&1B1790C4&0&0000"
start /b "" cmd.exe /c pnputil /enable-device %DEVICE_ID%

