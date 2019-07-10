# UpdateCommonMap.py
#
#    Map of GitHub project names to clone target paths, relative to the GPUPerfAPI
#    project root on the local disk.
#    This script is used by the UpdateCommon.py script

# GitHub GPUOpen-Tools projects map
# Define a set of dependencies that exist as separate git projects. The parameters are:
# "git repo name"  : ["Directory for clone relative to parent project directory",  "branch or commit to checkout (or None for top of tree)"]
gitMapping = {
 # Lib.
    "common-lib-amd-ADL"                  : ["../Common/Lib/AMD/ADL",               "da98d7a9d2b8a6222d32c82952ee44bdfc827b2e"],
    "common-lib-amd-APPSDK-3.0"           : ["../Common/Lib/AMD/APPSDK",            "4fad89c430a886d2e4723e617d821386eb634ec7"],
    "common-lib-ext-OpenGL"               : ["../Common/Lib/Ext/OpenGL",            "63cd62c8b25e165b0e6f3307b998ed0cf3810edf"],
    "common-lib-ext-WindowsKits"          : ["../Common/Lib/Ext/Windows-Kits",      "2c99b88d6a8a9b672464436dad771b9799056a8a"],
    "googletest"                          : ["../Common/Lib/Ext/GoogleTest",        "542e057c6c5bf45454b43764b881397b71164d62"],
# Src.
    "common-src-ADLUtil"                  : ["../Common/Src/ADLUtil",               "d62c94514326775c83fc129bb89d299c8749ebd1"],
    "common-src-AmdDxExt"                 : ["../Common/Src/AmdDxExt",              "9caab274b792ecb3a8d0db4b03315d6564a12eca"],
    "common-src-AmdVkExt"                 : ["../Common/Src/AmdVkExt",              "95c1039d849f2a61ba61facf175b866175169819"],
    "common-src-DeviceInfo"               : ["../Common/Src/DeviceInfo",            "8f62f981b950d052fe2549bfc9c3b678f3160c13"],
    "common-src-DynamicLibraryModule"     : ["../Common/Src/DynamicLibraryModule",  "ab1e854a6596e2f4d01c0b99096be11bbcd57ab8"],
    "common-src-TSingleton"               : ["../Common/Src/TSingleton",            "02e8fa7d98f33cdbd0e1f77d1a8a403a32e35882"],
    "common-src-CMakeModules"             : ["../Common/Src/CMakeModules",          "4d593266f3bb8916b15834050744659d0b86fc65"],
}

# Name : Source , Destination, version, Copied/Installation location wrt to Script root
downloadWin = {
    "Vulkan" : [ "https://sdk.lunarg.com/sdk/download/1.0.68.0/windows/VulkanSDK-1.0.68.0-Installer.exe", "default", "1.0.68.0", "default"],
    "GPADX11GetDeviceInfo" : [ "https://github.com/GPUOpen-Tools/GPA/releases/download/v3.2/GPUPerfAPI-3.2.623.0.zip" , "default", "3_2", "../Common/Lib/AMD/GPUPerfAPI"]
}

# Name : Source , Destination, version, Copied/Installation location wrt to Script root
downloadLinux = {
    "Vulkan" : [ "https://sdk.lunarg.com/sdk/download/1.0.68.0/linux/Vulkansdk-linux-x86_64-1.0.68.0.run", "default", "1.0.68.0", "default"]
}
