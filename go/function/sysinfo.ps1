"write-Output  \"[+][Info] 计算机制造商和型号\";
write-Output   \"=============================  \"; 
Get-CimInstance -ClassName Win32_ComputerSystem;
write-Output   \"  \"; 
write-Output    \"[+][Info] 处理器信息   \";
write-Output   \"=============================  \";  
Get-CimInstance -ClassName Win32_Processor | Select-Object -ExcludeProperty    \"CIM*   \"; 
write-Output   \"  \"; write-Output    \"[+][Info] 已安装的修补程序   \"; 
write-Output   \"=============================  \";  
Get-CimInstance -ClassName Win32_QuickFixEngineering; write-Output   \"  \"; 
write-Output    \"[+][Info] 可用磁盘空间   \"; 
write-Output   \"=============================  \";  
Get-CimInstance -ClassName Win32_LogicalDisk -Filter    \"DriveType=3   \";
write-Output   \"  \"; write-Output    \"[+][Info] BIOS 信息   \";
write-Output   \"=============================  \";  
Get-CimInstance -ClassName Win32_BIOS; 
write-Output   \"\"; 
write-Output    \"[+][Info] 登录会话信息   \"; 
write-Output   \"=============================  \";  
Get-CimInstance -ClassName Win32_LogonSession; \""

# "write-Output  \"[+][Info] 计算机制造商和型号 \"; write-Output \"=============================\"; Get-CimInstance -ClassName Win32_ComputerSystem; write-Output \"\"; write-Output  \"[+][Info] 处理器信息 \"; write-Output \"=============================\";  Get-CimInstance -ClassName Win32_Processor | Select-Object -ExcludeProperty  \"CIM* \"; write-Output \"\"; write-Output  \"[+][Info] 已安装的修补程序 \"; write-Output \"=============================\";  Get-CimInstance -ClassName Win32_QuickFixEngineering; write-Output \"\"; write-Output  \"[+][Info] 可用磁盘空间 \"; write-Output \"=============================\";   Get-CimInstance -ClassName Win32_LogicalDisk -Filter  \"DriveType=3 \"; write-Output \"\"; write-Output  \"[+][Info] BIOS 信息 \"; write-Output \"=============================\";  Get-CimInstance -ClassName Win32_BIOS; write-Output \"\"; write-Output  \"[+][Info] 登录会话信息 \";  write-Output \"=============================\";  Get-CimInstance -ClassName Win32_LogonSession;"
