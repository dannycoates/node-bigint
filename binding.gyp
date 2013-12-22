{
  'targets': [
    {
      'target_name': 'bigint',
      'sources': [ 'bigint.cc' ],
      'conditions': [
        ['OS=="solaris"',
          {
            'link_settings': {
              'libraries': [
                '-lgmp'
              ]
            }
          }
        ],
        ['OS=="linux"',
          {
            'link_settings': {
              'libraries': [
                '-lgmp'
              ]
            }
          }
        ],
        ['OS=="mac"',
          {
            'link_settings': {
              'libraries': [
                '-lgmp'
              ]
            }
          }
        ],
        ['OS=="win"',
          {
            'link_settings': {
              'libraries': [
                '-lgmp.lib'
              ],
            }
          }
        ]
      ]
    }
  ]
}
