#User limit

augeas { 'limits_nofile_1':
  context => '/files/etc/security/limits.conf',
  changes => [
    'set *[*="nofile"][position()=1]/#attribute/name "nofile"',
    'set *[*="nofile"][position()=1]/#attribute/value "50000"',
  ],
  notify => Exec['limits_nofile_2'],
}

augeas { 'limits_nofile_2':
  context => '/files/etc/security/limits.conf',
  changes => [
    'set *[*="nofile"][position()=2]/#attribute/name "nofile"',
    'set *[*="nofile"][position()=2]/#attribute/value "40000"',
  ],
}
