# Sets up your client SSH configuration file to use a private key
include stdlib

file_line { 'USE private key':
  path  =>  '/etc/ssh/ssh_config',
  line  =>  'IdentityFile ~/.ssh/school',
}

file_line { 'TURN OFF Password Auth':
  path  =>  '/etc/ssh/ssh_config',
  line  =>  'PasswordAuthentication no',
}
