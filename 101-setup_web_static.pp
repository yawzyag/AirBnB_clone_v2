# soy un comentario cool
exec {'update':
command  => 'sudo apt update',
provider => shell,
} -> package {'nginx':
ensure => 'installed',
} ->file { [ '/data/',
  '/data/web_static/',
  '/data/web_static/releases/',
  '/data/web_static/shared/',
  '/data/web_static/releases/test/', ]:
  ensure => directory,
} -> file { '/data/web_static/releases/test/index.html':
      ensure  => 'present',
      content => 'testing',
}
-> exec {'link':
command  => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
provider => shell,
}
-> exec {'chown':
command  => 'chown ubuntu:ubuntu -R /data/',
provider => shell,
}
-> exec {'sed':
command  => "sed -i '52i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/defaul",
provider => shell,
}
-> exec { 'restart':
command => '/usr/sbin/service nginx restart',
}
