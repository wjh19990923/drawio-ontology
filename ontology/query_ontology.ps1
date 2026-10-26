param([Parameter(ValueFromRemainingArguments=$true)][string[]]$QueryArgs)
$script = Join-Path $PSScriptRoot 'query_ontology.py'
$python = Get-Command python -ErrorAction SilentlyContinue
if ($python -and $python.Source -notmatch 'WindowsApps') { & $python.Source $script @QueryArgs; exit $LASTEXITCODE }
$launcher = Get-Command py -ErrorAction SilentlyContinue
if ($launcher) { & $launcher.Source -3 $script @QueryArgs; exit $LASTEXITCODE }
$bundled = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
if (Test-Path -LiteralPath $bundled) { & $bundled $script @QueryArgs; exit $LASTEXITCODE }
throw 'Python 3 was not found. Use a Codex workspace dependency runtime or install Python.'
