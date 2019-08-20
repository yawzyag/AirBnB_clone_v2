# soy un comentario cool
exec {'update':
command  => 'sudo apt update',
provider => shell,
} -> package {'nginx':
ensure => 'installed',
} -> file { '/data/web_static/shared/':
    ensure => 'directory',
} -> file { '/data/web_static/releases/test/':
    ensure => 'directory',
} -> file { '/data/web_static/releases/test/index.html':
      content => "test",
} ->   file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test/',
  } -> file { '/data/':
    ensure    => directory,
    owner     => 'ubuntu',
    group      => 'ubuntu',
    require     => [ User['ubuntu'], Group['ubuntu'], ],
    recurse    => true,
} -> -> file_line { 'Edit redirect':
ensure => present,
path   => '/etc/nginx/sites-enable/default',
line   => "       location / {
       add_header X-Served-By ${hostname};",
match  => '^\tlocation / {',
}

