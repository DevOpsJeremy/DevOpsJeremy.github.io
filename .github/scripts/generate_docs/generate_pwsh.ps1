[CmdletBinding()]
param (
    [string[]] $Modules
)
Install-PSResource platyPS -TrustRepository
Import-Module platyPS -Force
Import-Module $Modules -Force
foreach ($module in $Modules) {
    $fname = [IO.Path]::GetFileNameWithoutExtension($module)
    "--- $fname ---"
    Get-Module $fname
    Get-Command -Module $fname
}
