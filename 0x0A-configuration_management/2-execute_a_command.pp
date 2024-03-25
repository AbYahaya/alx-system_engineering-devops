# Define exec resource to kill process named killmenow
exec { 'kill_process':
  command => 'pkill -f killmenow',
  # Ensure that the command is only executed if the process exists
  onlyif  => 'pgrep -f killmenow',
}
